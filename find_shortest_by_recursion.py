"""
Solve the deck for zero (0) monster life by finding the lowest number of turns
and so the highest life score for hero using recursion.

It takes about 10 minutes to find the lowest maximum on
    - Intel® Core™ i5-5300U CPU @ 2.30GHz × 4
"""
import copy

from cards import cards
import handybrawl as hb
import pprint
import time
import deck


def play_card_recursive(deck):
    deck_test = hb.make_copy(deck)
    decks_new = hb.play_card(deck)

    decks_new.sort(key=lambda d: (hb.get_status(d).get("hero"), -hb.get_status(d).get("monster")), reverse=True)

    if deck.hash_str == '3A7C2A4B8C5A6C':
        pass

    global winner_game_length, game_turns, winner
    for deck_i in decks_new:
        if deck_i.hash_str == '3A7C2A4B8C5A6C':
            pass
        # todo: deepcopy issue: it copies also the prev attributes recursively.
        #   Find the way to reduce the load.
        deck_i_new = hb.make_copy(deck_i)
        # todo: change the hash as well, not only the deck
        deck_i_new.cards = hb.back_shift(deck_i_new.cards)
        status = hb.get_status(deck_i)
        if deck_test != deck:
            pass

        if deck_i_new.hash_str not in hb.game_turns and deck_i_new.hash_str != start.hash_str:
            hb.game_turns[deck_i_new.hash_str] = deck.hash_str
            game_deck_i_new = hb.recreate_game(deck_i_new.hash_str)
            # hb.report_game_status(game_deck_i_new)

            if status.get("hero") == 0 or status.get("monster") == 0:
                if status.get("monster") == 0:
                    hb.report_game_status(game_deck_i_new)
                    if len(game_deck_i_new) - 1 < winner_game_length:
                        winner_game_length = len(game_deck_i_new) - 1
                        winner = hb.make_copy(deck_i_new)
            elif len(game_deck_i_new) < winner_game_length:
                # print(len(game_deck_i_new) - 1)
                try:
                    # make a new turn with the deck, expect +1 on len(recreate_game())
                    play_card_recursive(deck_i_new)
                except RecursionError:
                    print(deck_i_new.hash_str, ":", status, "recursion overflow")
            else:
                pass
        else:
            pass
    return winner


# record start time
t_start = time.time()

# start_hash = '1A6A2A7A3A8A4A9A5A'
# start_hash = '5A9A4A8A3A7A2A6A1A'
# start_hash = '6A7A8A9A1A2A3A4A5A'
# start_hash = '1A2A3A4A5A6A7A8A9A'
# start_hash = '9A8A7A6A5A4A3A2A1A' # no winning game
# start_hash = '2A3A4A5A6A7A8A'
# start_hash = '1A2A3A4A6A9A8A5A7A'
# start_hash = '1A6A2A7A3A8A4A'
start_hash = '1A6A2A9A3A'
# start_hash = '10A15A11A16A12A17A13A18A14A'
# start_hash = '9b2b6d5c'

# deck_start = hb.create_deck(start_hash, cards)

start = deck.Deck(start_hash)

game_turns = dict()
winner_game_length = 20
winner = deck.Deck()
print("Searching for the first possible winning outcome. "
      "Then searching further for the solution with the highest hero's life.")

winner = play_card_recursive(start)

winner_game = hb.recreate_game(winner.hash_str)
print("The game with the least turns and the highest hero life flows the following:")
pprint.pprint(winner_game)

# record end time
t_end = time.time()

# print the difference between start and end time in milliseconds
print("The time of execution of above program is :", (t_end-t_start) * 10**3, "ms")
