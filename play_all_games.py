"""
Solve the deck for zero (0) monster life by finding the lowest number of turns
and so the highest life score for hero using recursion.

It takes about 10 minutes to find the lowest maximum on
- Intel® Core™ i5-5300U CPU @ 2.30GHz × 4
"""
import pprint

import cards
import handybrawl as hb
import pprint


def play_card_recursive(deck):
    decks_new = hb.play_card(deck)

    decks_new.sort(key=lambda d: (hb.get_status(d).get("hero"), -hb.get_status(d).get("monster")), reverse=True)

    if hb.get_deck_hash(deck) == '3A7C2A4B8C5A6C':
        pass

    global first_winner_length, game_bits, first_winner_hash
    for deck_i in decks_new:
        if hb.get_deck_hash(deck_i) == '3A7C2A4B8C5A6C':
            pass
        deck_i_new = hb.back_shift(deck_i[:])
        deck_i_new_hash = hb.get_deck_hash(deck_i_new)
        status = hb.get_status(deck_i)
        if deck_i_new_hash not in hb.game_bits and deck_i_new_hash != hb.get_deck_hash(deck_start):
            hb.game_bits[deck_i_new_hash] = hb.get_deck_hash(deck)
            game_deck_i_new = hb.recreate_game(deck_i_new_hash)
            if status.get("hero") == 0 or status.get("monster") == 0:
                if status.get("monster") == 0:
                    print(len(hb.game_bits), ":",
                          deck_i_new_hash, ":",
                          status,
                          'start deck:', game_deck_i_new[-1],
                          'length of game:', len(game_deck_i_new) - 1)
                    if len(game_deck_i_new) - 1 < first_winner_length:
                        first_winner_length = len(game_deck_i_new) - 1
                        first_winner_hash = deck_i_new_hash
            elif len(game_deck_i_new) < first_winner_length:
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
    return first_winner_hash


# deck_start_hash = '1A6A2A7A3A8A4A9A5A'
# deck_start_hash = '6A7A8A9A1A2A3A4A5A'
# deck_start_hash = '1A2A3A4A5A6A7A8A9A'
# deck_start_hash = '2A3A4A5A6A7A8A'
deck_start_hash = '1A2A3A4A6A9A8A5A7A'
# deck_start_hash = '1A6A2A8A3A'
# deck_start_hash = '9b2b6d5c'

deck_start = hb.create_deck(deck_start_hash, cards.cards)

game_bits = dict()
first_winner_length = 20
first_winner_hash = None
print("Searching for the first possible winning outcome. "
      "Then searching further for the solution with the highest hero's life.")

winner_hash = play_card_recursive(deck_start)
winner_game = hb.recreate_game(winner_hash)
winner_game.reverse()
print("The game with the least turns and the highest hero life flows the following:")
pprint.pprint(winner_game)

# lst = list(permutations(range(1, 10)))
# print(len(lst))
#
# for k in lst:
#     s = [str(j) for j in k]
#     deck_start_hash = 'A'.join(s) + 'A'
#     deck_start = hb.create_deck(deck_start_hash, all_cards.cards)
#     game_bits = dict()
#     first_winner_length = 111
#     first_winner_hash = None
#     play_card_recursive(deck_start)
#     print(len(game_bits))

pass

#
# for key, value in game_bits.items():  # iter on both keys and values
#     if key.endswith('5A') or key.startswith('5A'):
#         print(key, value)
