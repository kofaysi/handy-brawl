"""
Solve the deck for zero (0) monster life by finding the lowest number of turns
and so the highest life score for hero using recursion.

It takes about 10 minutes to find the lowest maximum on
    - Intel® Core™ i5-5300U CPU @ 2.30GHz × 4
"""

import cards
import handybrawl as hb
import pprint
import time


def play_card_recursive(deck):
    decks_new = hb.play_card(deck)

    decks_new.sort(key=lambda d: (hb.get_status(d).get("hero"), -hb.get_status(d).get("monster")), reverse=True)

    if hb.get_deck_hash(deck) == '3A7C2A4B8C5A6C':
        pass

    global winner_game_length, game_turns, winner_deck_hash
    for deck_i in decks_new:
        if hb.get_deck_hash(deck_i) == '3A7C2A4B8C5A6C':
            pass
        deck_i_new = hb.back_shift(deck_i[:])
        deck_i_new_hash = hb.get_deck_hash(deck_i_new)
        status = hb.get_status(deck_i)
        if deck_i_new_hash not in hb.game_turns and deck_i_new_hash != hb.get_deck_hash(deck_start):
            hb.game_turns[deck_i_new_hash] = hb.get_deck_hash(deck)
            game_deck_i_new = hb.recreate_game(deck_i_new_hash)
            if status.get("hero") == 0 or status.get("monster") == 0:
                if status.get("monster") == 0:
                    hb.report_game_status(game_deck_i_new)
                    if len(game_deck_i_new) - 1 < winner_game_length:
                        winner_game_length = len(game_deck_i_new) - 1
                        winner_deck_hash = deck_i_new_hash
            elif len(game_deck_i_new) < winner_game_length:
                # print(len(game_deck_i_new) - 1)
                try:
                    # make a new turn with the deck, expect +1 on len(recreate_game())
                    play_card_recursive(deck_i_new[:])
                except RecursionError:
                    print(deck_i_new_hash, ":", status, "recursion overflow")
            else:
                pass
        else:
            pass
    return winner_deck_hash


# record start time
start = time.time()

deck_start_hash = '1A6A2A7A3A8A4A9A5A'
# deck_start_hash = '5A9A4A8A3A7A2A6A1A'
# deck_start_hash = '6A7A8A9A1A2A3A4A5A'
# deck_start_hash = '1A2A3A4A5A6A7A8A9A'
# deck_start_hash = '9A8A7A6A5A4A3A2A1A' # no winning game
# deck_start_hash = '2A3A4A5A6A7A8A'
# deck_start_hash = '1A2A3A4A6A9A8A5A7A'
# deck_start_hash = '1A6A2A8A3A'
# deck_start_hash = '9b2b6d5c'

deck_start = hb.create_deck(deck_start_hash, cards.cards)

game_turns = dict()
winner_game_length = 15
winner_deck_hash = None
print("Searching for the first possible winning outcome. "
      "Then searching further for the solution with the highest hero's life.")

winner_hash = play_card_recursive(deck_start)

winner_game = hb.recreate_game(winner_hash)
print("The game with the least turns and the highest hero life flows the following:")
pprint.pprint(winner_game)

# record end time
end = time.time()

# print the difference between start and end time in milliseconds
print("The time of execution of above program is :", (end-start) * 10**3, "ms")
