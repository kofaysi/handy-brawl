"""
Solve the deck by finding the lowest number of turns using recursion.
"""

import cards
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
        "push": lambda d, a, r: hb.move_deck(d, a, r),  # deck, action, range
        "pull": lambda d, a, r: hb.move_deck(d, a, -r),  # deck, action, range
        "delay": lambda d, a, p: hb.delay_deck(d, a, p),  # deck, action, by positions
        "quicken": lambda d, a, p: hb.delay_deck(d, a, -p),  # deck, action, by positions
        "rotate": lambda d, a, n: hb.rotate_top_card(d),  # deck
        "heal": lambda d, a, n: hb.heal_deck(d),  # deck
        "arrow": lambda d, a, nt: hb.arrow_deck(d, a, nt),  # deck, action, number of targets
        "maneuver": lambda d, a, n: hb.maneuver_deck(d),  # deck
    }
    decks_new_i = []
    decks_new_i_prev_unchanged_rows = []
    for i, row in enumerate(deck[0][1][1:]):
        decks = [deck[:]]
        decks_new_j = []
        for j, action in enumerate(row):
            if deck[0][0].get("type") == "hero":
                # for the hero, it is allowed not make some actions,
                # we will drop decks which have not changed at the end of the action row
                decks.extend(decks_new_j[:])
            else:
                # the monster shall make all the available actions
                if decks_new_j:
                    decks = decks_new_j[:]
                # else decks have not changed by the previous action and are going to suffer the next action
            for deck_j in decks:
                # debug test
                deck_j_hash = hb.get_deck_hash(deck_j)
                if deck_j_hash == '6C7C8C4D9C3C2C5D1D':
                    pass
                switcher_action = action[0].split()[0]
                decks_new_j.extend(switcher.get(switcher_action)(deck_j[:], action[0], action[1]))
            decks_new_j = hb.get_unique_items(decks_new_j)

        # collect deck_changed bools
        decks_new_j_changed = [hb.deck_changed(d, deck) for d in decks_new_j]
        # decks_new_i = [m for m in decks_new_j if hb.deck_changed(m, deck)]

        # if any deck changed
        if any(decks_new_j_changed):
            if not all(decks_new_j_changed):
                decks_new_j = [deck_new_j for m, deck_new_j in enumerate(decks_new_j) if decks_new_j_changed[m]]
            decks_new_i.extend(decks_new_j)
            decks_new_i = hb.get_unique_items(decks_new_i[:])
            if deck[0][0].get('type') == 'monster':
                break
        # all the decks stale, no new deck show new configuration
        else:
            decks_new_i_prev_unchanged_rows.extend(decks_new_j)
        # if the last row has been reached
        if not decks_new_i and i == len(deck[0][1][1:]) - 1:
            decks_new_i = hb.get_unique_items(decks_new_i_prev_unchanged_rows[:])

        # remove duplicates and remove the original deck, if others could be created

        # decks_new_i = [i for i in decks_new_i if deck_changed(i, deck)]
        # if len(decks_new_i) == 0:
        #    decks_new_i.append(deck)

    decks_new = hb.get_unique_items(decks_new_i[:])

    # sort results by their decreasing her status, and increasing monster status
    decks_new.sort(key=lambda d: (hb.get_status(d).get("hero"), -hb.get_status(d).get("monster")), reverse=True)

    if hb.get_deck_hash(deck) == '3A7C2A4B8C5A6C':
        pass

    global first_winner_length, decks_list, first_winner_hash
    for deck_i in decks_new:
        if hb.get_deck_hash(deck_i) == '3A7C2A4B8C5A6C':
            pass
        deck_i_new = hb.back_shift(deck_i[:])
        deck_i_new_hash = hb.get_deck_hash(deck_i_new)
        status = hb.get_status(deck_i)
        if deck_i_new_hash not in decks_list and deck_i_new_hash != hb.get_deck_hash(deck_start):
            decks_list[deck_i_new_hash] = hb.get_deck_hash(deck)
            game_deck_i_new = recreate_game(deck_i_new_hash)
            if status.get("hero") == 0 or status.get("monster") == 0:
                if status.get("monster") == 0:
                    print(len(decks_list), ":",
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
                    play_card(deck_i_new[:])
                except RecursionError:
                    print(deck_i_new_hash, ":", status, "recursion overflow")
            else:
                pass
        else:
            pass


# deck_start_hash = '1A6A2A7A3A8A4A9A5A'
# deck_start_hash = '6A7A8A9A1A2A3A4A5A'
# deck_start_hash = '1A2A3A4A5A6A7A8A9A'
deck_start_hash = '2A3A4A5A6A7A8A'
# deck_start_hash = '1A2A3A4A6A9A8A5A7A'
# deck_start_hash = '1A6A2A8A3A'
# deck_start_hash = '9b2b6d5c'

deck_start = hb.create_deck(deck_start_hash, cards.cards)

decks_list = dict()
first_winner_length = 20
first_winner_hash = None

play_card(deck_start)

# lst = list(permutations(range(1, 10)))
# print(len(lst))
#
# for k in lst:
#     s = [str(j) for j in k]
#     deck_start_hash = 'A'.join(s) + 'A'
#     deck_start = hb.create_deck(deck_start_hash, all_cards.cards)
#     decks_list = dict()
#     first_winner_length = 111
#     first_winner_hash = None
#     play_card(deck_start)
#     print(len(decks_list))

pass

#
# for key, value in decks_list.items():  # iter on both keys and values
#     if key.endswith('5A') or key.startswith('5A'):
#         print(key, value)
