"""
Solve the deck by finding the lowest number of turns using a for-cycle.
It is highly time-inefficient way of finding the solution.
"""

import cards
import handybrawl as hb


# deck_start_hash = '1A6A2A7A3A8A4A9A5A'
# deck_start_hash = '6A7A8A9A1A2A3A4A5A'
# deck_start_hash = '1A2A3A4A5A6A7A8A9A'
deck_start_hash = '1A6A2A8A3A'
# deck_start_hash = '2A3A4A5A6A7A8A'
# deck_start_hash = '1A2A3A4A6A9A8A5A7A'
# deck_start_hash = '1A6A2A8A3A'
# deck_start_hash = '9b2b6d5c'

deck_start = hb.create_deck(deck_start_hash, cards.cards)

first_winner_length = 32
first_winner_hash = None

decks_new_main = [deck_start]
i = 0

while not first_winner_hash:
    i += 1
    print("Turn:", i)
    decks_i_new = []
    for deck_i in decks_new_main:
        decks_i_new.extend(hb.play_card(deck_i))

    decks_i_new = hb.get_unique_items(decks_i_new[:])
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
        status = hb.get_status(deck_i)
        if deck_i_new_hash not in hb.game_bits and deck_i_new_hash != hb.get_deck_hash(deck_start):
            hb.game_bits[deck_i_new_hash] = hb.get_deck_hash(deck_i)
            game_deck_i_new = hb.recreate_game(deck_i_new_hash)
            decks_i_new_A.append(deck_i_new)
            if status.get("monster") == 0 and status.get("hero") != 0:
                print(len(hb.game_bits), ":",
                      deck_i_new_hash, ":",
                      status,
                      'start deck:', game_deck_i_new[-1],
                      'length of game:', len(game_deck_i_new) - 1)
                first_winner_length = len(game_deck_i_new) - 1
                first_winner_hash = deck_i_new_hash

    decks_new_main = decks_i_new_A

pass
