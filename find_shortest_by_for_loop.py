"""
Solve the deck by finding the lowest number of turns using a for-loop.
It is highly time-inefficient way of finding the solution.
This algorithm is like to work well for finding solutions for deck with up to 6 cards.
"""

import cards
import handybrawl as hb
import pprint
import time

# record start time
start = time.time()


# start_hash = '1A2A3A4A6A9A8A5A7A'
# start_hash = '6A7A8A9A1A2A3A4A5A'
# start_hash = '1A2A3A4A5A6A7A8A9A'
deck_start_hash = '1A6A2A8A3A'
# start_hash = '2A3A4A5A6A7A8A'
# start_hash = '1A2A3A4A6A9A8A5A7A'
# start_hash = '1A6A2A8A3A'
# start_hash = '9b2b6d5c'

deck_start = hb.create_deck(deck_start_hash, cards.cards)

winner_game_length = 13
winner_hash = None

decks_new_main = [deck_start]
i = 0

while not winner_hash:
    i += 1
    print("Turn:", i)
    decks_i_new = []
    if i == 6:
        pass
    for deck_i in decks_new_main:
        if hb.get_deck_hash(deck_i) == '1D3A6C2C8D':
            pass
        # do not execute play_card() if the deck had been an origin previously
        if hb.get_deck_hash(deck_i) not in hb.game_turns.values():
            decks_i_new.extend(hb.play_card(deck_i))

            for deck_i_new in decks_i_new:
                deck_i_new_hash = hb.get_deck_hash(hb.back_shift(deck_i[:]))
                if deck_i_new_hash == '3A6C2C8C1D':
                    pass
                if deck_i_new_hash not in hb.game_turns:
                    hb.game_turns[deck_i_new_hash] = hb.get_deck_hash(deck_i)

    # the for cycle needs to get rid of duplicates and optionally sort the list of decks
    decks_i_new = hb.get_unique_items(decks_i_new[:])
    decks_i_new.sort(key=lambda d: (hb.get_status(d).get("hero"), -hb.get_status(d).get("monster")), reverse=True)

    print("Number of results:", len(decks_i_new))

    decks_i_new_A = []
    for deck_i in decks_i_new:
        deck_i_new = hb.back_shift(deck_i[:])
        if hb.get_deck_hash(deck_i_new) == '3A4A5A7A6A8A2A':
            pass
        if hb.get_deck_hash(deck_i_new) == '3B7A2A4B8C5A6C':
            pass
        if hb.get_deck_hash(deck_i_new) == '6D3B7A2A4A8C5A':
            pass
        if hb.get_deck_hash(deck_i_new) == '5A6A7A2A3B4A8C':
            pass
        if hb.get_deck_hash(deck_i_new) == '8C6A7A2A3B4A5A':
            pass
        if hb.get_deck_hash(deck_i_new) == '5A6A8D7A2A3B4A':
            pass
        if hb.get_deck_hash(deck_i_new) == '4A5A6A8A7A2A3B':
            pass
        deck_i_new_hash = hb.get_deck_hash(deck_i_new)
        status = hb.get_status(deck_i_new)
        # do not count the deck if the deck had been any result previously
        if deck_i_new_hash not in hb.game_turns and deck_i_new_hash != hb.get_deck_hash(deck_start):
            # hb.game_turns[deck_i_new_hash] = hb.get_deck_hash(deck_i)
            game_deck_i_new = hb.recreate_game(deck_i_new_hash)
            decks_i_new_A.append(deck_i_new)
            if status.get("monster") == 0 and status.get("hero") != 0:
                hb.report_game_status(game_deck_i_new)
                winner_game_length = len(game_deck_i_new) - 1
                winner_hash = deck_i_new_hash

    decks_new_main = decks_i_new_A

pass

winner_game = hb.recreate_game(winner_hash)
print("The game with the least turns and the highest hero life flows the following:")
pprint.pprint(winner_game)

# record end time
end = time.time()

# print the difference between start and end time in milliseconds
print("The time of execution of above program is :", (end-start) * 10**3, "ms")