import all_cards
import handybrawl as hb


def recreate_game(d_hash):
    global decks_list
    game = []
    d_i_hash = d_hash[:]
    key_found = True
    game.append(d_i_hash)
    while key_found:
        d_prev_hash = decks_list.get(d_i_hash)
        if d_prev_hash:
            game.append(d_prev_hash)
            d_i_hash = d_prev_hash[:-2] + d_prev_hash[-2:]
        else:
            key_found = False
    return game


def play_card(deck):
    switcher = {
        "hit": lambda d, a, n: hb.hit_deck(d, n),  # deck, action,
        "arrow": lambda d, a, nt: hb.arrow_deck(d, a, nt),  # deck, action, number of targets
        "push": lambda d, a, r: hb.move_deck(d, a, r),  # deck, action, range
        "pull": lambda d, a, r: hb.move_deck(d, a, -r),  # deck, action, range
        "delay": lambda d, a, p: hb.delay_deck(d, a, p),  # deck, action, by positions
        "quicken": lambda d, a, p: hb.delay_deck(d, a, -p),  # deck, action, by positions
        "rotate": lambda d, a, n: hb.rotate_top_card(d),  # deck
        "heal": lambda d, a, n: hb.heal_deck(d),  # deck
        "maneuver": lambda d, a, n: hb.maneuver_deck(d),  # deck
    }
    decks_new_i = []
    decks_new_j_prev_unchanged_rows = []
    for i, row in enumerate(deck[0][1][1:]):
        decks = [deck[:]]
        decks_new_j = []
        for j, action in enumerate(row):
            if j > 0 and decks_new_j:
                decks = decks_new_j[:]
                decks_new_j = []
            for deck_j in decks:
                # deck_j_sign = get_deck_hash(deck_j)
                if not hb.check_cards_unique(deck_j):
                    pass
                action_raw = action[0]
                deck_j_hash = hb.get_deck_hash(deck_j)
                if deck_j_hash == '6A8A2A1B':
                    pass
                decks_new_j = switcher.get(action_raw.split()[0])(deck_j[:], action_raw, action[1])
                duplicates = [deck for deck in decks_new_j if decks_new_j.count(deck) > 1]
                if len(duplicates):
                    pass
                for deck_new_j in decks_new_j:
                    if hb.get_deck_hash(deck_new_j) == '9C2C3C4D6A7D8A5D1C':
                        pass
                    if not hb.check_cards_unique(deck_new_j):
                        pass
            decks_new_j = hb.get_unique_items(decks_new_j[:])
            # decks_new_j = [i for i in decks_new_j if deck_changed(i, deck) or j == len(row)]
        #            if len(decks_new_j) == 0:
        #                decks_new_j.append(deck)

        decks_new_j_changed = [hb.deck_changed(i, deck) for i in decks_new_j]
        if True in decks_new_j_changed:
            decks_new_j = [deck_new_j for i, deck_new_j in enumerate(decks_new_j) if decks_new_j_changed[i]]
            decks_new_i.extend(decks_new_j)
            decks_new_i = hb.get_unique_items(decks_new_i[:])
            if deck[0][0].get('type') == 'monster':
                break
        else:
            decks_new_j_prev_unchanged_rows.extend(decks_new_j)
            if i == len(deck[0][1][1:]) - 1:
                if deck[0][0].get('type') == 'monster' or not decks_new_i:
                    decks_new_i = hb.get_unique_items(decks_new_j_prev_unchanged_rows[:])

        # remove duplicates and remove the original deck, if others could be created

        # decks_new_i = [i for i in decks_new_i if deck_changed(i, deck)]
        # if len(decks_new_i) == 0:
        #    decks_new_i.append(deck)

    decks_new = hb.get_unique_items(decks_new_i[:])

    for deck_i in decks_new:
        status_i = hb.get_status(deck_i)

    if hb.get_deck_hash(deck) == '3B1A6B2A8B':
        pass

    if decks_new:
        global first_winner_length
        global decks_list
        global first_winner_hash
        for deck_i in decks_new:
            deck_i_new = hb.back_shift(deck_i[:])
            deck_i_new_hash = hb.get_deck_hash(deck_i_new)
            status = hb.get_status(deck_i)
            if deck_i_new_hash not in decks_list and deck_i_new_hash != hb.get_deck_hash(deck_start):
                decks_list[deck_i_new_hash] = hb.get_deck_hash(deck)
                game_deck_i_new = recreate_game(deck_i_new_hash)
                if status.get("hero") != 0 \
                        and status.get("monster") != 0 \
                        and len(game_deck_i_new) <= 1 * first_winner_length \
                        and not first_winner_hash:
                    # no win or defeat, and deck changed, or it is the last action row iteration anyway
                    try:
                        play_card(deck_i_new[:])
                    except RecursionError:
                        print(deck_i_new_hash, ":", status, "recursion overflow")
                elif status.get("hero") == 0 or status.get("monster") == 0:
                    # game_deck_i_new = recreate_game(deck_i_new_hash)
                    # print(len(decks_list), ":",
                    #       deck_i_new_hash, ":",
                    #       status,
                    #       'start deck:', game_deck_i_new[-1],
                    #       'length of game:', len(game_deck_i_new) - 1)
                    # print("hb.rotate_card_to_face", ":", hb.rotate_card_to_face.call_count)
                    if status.get("monster") == 0:
                        print(len(decks_list), ":",
                              deck_i_new_hash, ":",
                              status,
                              'start deck:', game_deck_i_new[-1],
                              'length of game:', len(game_deck_i_new) - 1)
                        if len(game_deck_i_new) < first_winner_length:
                            first_winner_length = len(game_deck_i_new)
                            first_winner_hash = deck_i_new_hash
    else:
        pass


# deck_start_hash = '1A6A2A7A3A8A4A9A5A'
# deck_start_hash = '6A7A8A9A1A2A3A4A5A'
deck_start_hash = '1A9A3A4A5A6A2A8A7A'
# deck_start_hash = '1A6A2A8A3A'
# deck_start_hash = '9b2b6d5c'

deck_start = hb.create_deck(deck_start_hash, all_cards.cards)

# decks_list = dict()
# first_winner_length = 111
# first_winner_hash = None
#
# play_card(deck_start)

from itertools import permutations
from array import *

l = list(permutations(range(1, 10)))
print(len(l))

for i in l:
    s = [str(j) for j in i]
    deck_start_hash = 'A'.join(s) + 'A'
    deck_start = hb.create_deck(deck_start_hash, all_cards.cards)
    decks_list = dict()
    first_winner_length = 111
    first_winner_hash = None
    play_card(deck_start)
#
# for key, value in decks_list.items():  # iter on both keys and values
#     if key.endswith('5A') or key.startswith('5A'):
#         print(key, value)
