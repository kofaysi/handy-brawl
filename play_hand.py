import all_cards
# import numpy as np


def rotate_card_to_face(c, f):
    c_new = c
    face_current = c_new[1][0].get("face")
    if face_current != f:
        c_new = rotate(c[:])
        face_current = c_new[1][0].get("face")
        if face_current != f:
            c_new = flip(c[:])
            face_current = c_new[1][0].get("face")
            if face_current != f:
                c_new = flip(rotate(c[:]))
    return c_new


def flip(c):
    return [c[0], c[3], c[4], c[1], c[2]]


def rotate(c):
    return [c[0], c[2], c[1], c[4], c[3]]


def rotate_flip(c):
    return flip(rotate(c))


def leftShift(tup, n=1):  # by default, the top card goes to the bottom of the deck
    try:
        n = n % len(tup)
    except ZeroDivisionError:
        return tuple()
    return tup[n:] + tup[0:n]

# def push(hand_of_cards, card_to_push, steps_to_push):
#     print()


# def read_card(card):
#     action = None
#     for row in card[1][1:]:
#         if row[0]:
#             action = row[0]
#             return action
#         else:
#             leftShift(row)
#             card = card[:][:][1:] + card[:][0]
#
#     return card, action


def deal_damage(d, i):
    if not check_cards_unique(d):
        pass
    d_new = d[:]
    if d[i][1][0].get("life") == "healthy":
        expected_life = "wounded"
    else:
        expected_life = "exhausted"
    for j in range(1, 5):
        if d[i][j][0].get("life") == expected_life:
            expected_face = d[i][j][0].get("face")
            break
    expected_card = rotate_card_to_face(d[i][:], expected_face)
    d_new[i] = expected_card
    # test_card = rotate(d[i][:])
    # if d[i][1][0].get("life") == "wounded":
    #     d_new[i] = rotate(d[i])
    # elif flip(d[i])[1][0].get("life") == "wounded":
    #     d_new[i] = flip(d[i])
    # else:
    #    d_new[i] = rotate_flip(d[i])
    if d == d_new:
        pass
    return d_new


def deck_changed(d, d_new):
    if not check_cards_unique(d):
        pass
    if not check_cards_unique(d_new):
        pass
    return d[1:] != d_new[1:]


def move_card_to_position(d, i, j):
    if not check_cards_unique(d):
        pass
#     d[i], d[j] = d[j], d[i]
    # # TODO check the code
    if i < j:
        d[i:j+1] = leftShift(d[i:j+1])
    else:
        d[j:i+1] = leftShift(d[j:i+1], len(d[j:i+1])-1)
    return d


def move_card(d, a, r):
    if not check_cards_unique(d):
        pass
    if get_deck_hash(d) == '7D3A8A4B9A5B1A6C2B':
        pass
    ds_new = []
    if ' ' in a:
        t = a.split()[1]
    else:
        t = "any"
    if r < 0:
        move_range = reversed(range(1, abs(r) + 1))
    else:
        move_range = range(1, r + 1)
        for i in move_range:
            m = None
            if (t == "self" or t == "any") and d[0][0].get("type") == d[i][0].get("type"):
                m = i
            elif (t == "enemy" or t == "any") and \
                d[0][0].get("type") != d[i][0].get("type") and \
                d[i][1][0].get("feature") != "heavy":
                if r < 0 and d[i][1][0].get("life") != "exhausted":
                    m = i
            if m:
                if r < 0:
                    ds_new.append(move_card_to_position(d[:], m, 1))
                if r > 0:
                    ds_new.append(move_card_to_position(d[:], m, len(d)))
                if d[0][0].get("type") == "monster":
                    break
    return ds_new


def rotate_top(d):
    if not check_cards_unique(d):
        pass
    d_new = d[:]
    d_new[0] = rotate(d[0])
    ds_new = [d_new]
    return ds_new


def use_shield(d, i):
    if not check_cards_unique(d):
        pass
    d_new = d[:]

    switcher = {
        "rotate": lambda c: rotate(c)
    }

    action = d[i][1][0].get("shield")
    if action:
        d_new[i] = switcher.get(action)(d[i])
        if not check_cards_unique(d_new):
            pass
    return d_new


def top_card_to_bottom(d):
    if not check_cards_unique(d):
        pass
    d_new = leftShift(d[:])
    return d_new


def hit_card(d, n):
    if not check_cards_unique(d):
        pass
    shield_found = False
    ds_new = []
    if n == 0:  # substitute for the infinite hit range
        n = len(d)-1
    if n > len(d)-1:
        n = len(d)-1
    for i in reversed(range(1, n+1)):
        if d[0][0].get("type") != d[i][0].get("type") and d[i][1][0].get("reaction") == "shield":
            shield_found = True
            d_new = use_shield(d[:], i)
            if not check_cards_unique(d_new):
                pass
            ds_new.append(d_new)
            if d[0][0].get("type") == "monster":
                break
    if not shield_found:
        for i in range(1, n+1):
            if d[0][0].get("type") != d[i][0].get("type") and d[i][1][0].get("life") != "exhausted":
                d_new = deal_damage(d[:], i)
                if not check_cards_unique(d_new):
                    pass
                ds_new.append(d_new)
                if d[0][0].get("type") == "monster":
                    break
    return ds_new

def get_unique_items(list):
    unique = []
    for item in list:
        if item not in unique:
            unique.append(item)
    return unique


# noinspection PyShadowingNames
def get_status(deck_var):
    status = dict(hero=0.0, monster=0.0)
    score = dict(healthy=1, wounded=0.5, exhausted=0)
    if isinstance(deck_var, str):
        deck = get_deck(deck_var[:])
    else:
        deck = deck_var[:]
    for card in deck:
        card_score = score.get(card[1][0].get("life"))
        if card[0].get("type") == "hero":
            temp_score = status.get("hero") + card_score
            status.update(hero=temp_score)
        else:
            temp_score = status.get("monster") + card_score
            status.update(monster=temp_score)
    return status


def delay_card(d, a, p):
    if get_deck_hash(d) == '1A6C2B3A7A9C8B4D5A':
        pass
    if ' ' in a:
        t = a.split()[1]
    else:
        t = "any"
    ds_new = []
    delay_range = range(1, abs(p)+1)
    if p < 0:
        delay_range = [-i for i in list(delay_range)]
    for i in range(1, len(d)):
        for j in delay_range:
            m = None
            if t == "self":
                if d[0][0].get("type") == d[i][0].get("type"):  # and d[i][1][1].get("life") != "exhausted":
                    m = j
            elif t == "enemy":
                if d[0][0].get("type") != d[i][0].get("type"):  # and d[i][1][1].get("life") != "exhausted":
                    m = j
            else:
                # if d[i][1][1].get("life") != "exhausted":
                m = j
            if m:
                if p < 0:
                    m = -m
                end_position = i + m
                if len(d) > end_position >= 1:
                    d_new = move_card_to_position(d[:], i, end_position)
                    ds_new.append(d_new)
    return ds_new


# noinspection PyShadowingNames
def refresh(c):
    for card in all_cards.cards:
        if card[0].get("number") == c[0].get("number"):
            return card


def heal_deck(d):
    if not check_cards_unique(d):
        pass
    ds_new = []
    for i in range(1, len(d)):
        if d[0][0].get("type") == d[i][0].get("type") and d[i][1][0].get("life") == "wounded":
            d_new = d[:]
            d_new[i] = refresh(d[i])
            ds_new.append(d_new)
            if not check_cards_unique(d_new):
                pass
            if d[0][0].get("type") == "monster":
                break
    return ds_new


def maneuver_deck(d):
    ds_new = []
    for i in range(1, len(d)+1):
        if (d[0][0].get("type") == d[i][0].get("type") and
                (d[i][1][0].get("life") == d[i][2][0].get("life") or
                 (d[i][1][0].get("life") == "healthy" and d[i][2][0].get("life") == "wounded") or
                 (d[i][1][0].get("life") == "healthy" and d[i][2][0].get("life") == "exhausted") or
                 (d[i][1][0].get("life") == "wounded" and d[i][2][0].get("life") == "exhausted"))):
            d_new = d[:]
            d_new[i] = rotate(d[i])
            ds_new.append(d_new)
    return ds_new


def arrow_deck(d, a):
    try:
        t = a.split()[1]
    except IndexError:
        t = "single"
    ds_new = []
    m = len(d)
    for i in range(m-2, m + 1):
        if d[0][0].get("type") != d[i][0].get("type") and d[i][0].get("reaction") != "shield":
            d_new = deal_damage(d, i)
        if t == "double":
            for j in range(m - 2, m + 1):
                if j != i and d[0][0].get("type") != d[i][0].get("type") and d[i][0].get("reaction") != "shield":
                    # TODO check, if enemy shield on earlier position can protect also
                    d_new = deal_damage(d_new, i)
        ds_new.append(d_new)
    return ds_new


def check_cards_unique(d):
    for i1, c1 in enumerate(d):
        for i2, c2 in enumerate(d):
            if i1 != i2:
                if c1[0].get("number") == c2[0].get("number"):
                    return False
    return True


def play_card(deck):
    decks = [deck]
    status = []
    switcher = {
        "hit": lambda d, a, n: hit_card(d, n),
        "arrow": lambda d, a, n: arrow_deck(d, a),
        "push": lambda d, a, r: move_card(d, a, r),
        "pull": lambda d, a, r: move_card(d, a, -r),
        "delay": lambda d, a, p: delay_card(d, a, p),
        "quicken": lambda d, a, p: delay_card(d, a, -p),
        "rotate": lambda d, a, n: rotate_top(d),
        "heal": lambda d, a, n: heal_deck(d),
        "maneuver": lambda d, a, n: maneuver_deck(d),
    }
    decks_new = []
    decks_new_i = []
    decks_new_j_prev_nonchanged_rows = []
    for i, row in enumerate(deck[0][1][1:]):
        # TODO monsters shall not run next row unless no results achieved in the first run
        decks = [deck[:]]
        decks_new_j = []
        for j, action in enumerate(row):
            if j > 0 and decks_new_j:
                decks = decks_new_j[:]
                decks_new_j = []
            for deck_j in decks:
                #deck_j_sign = get_deck_hash(deck_j)
                if not check_cards_unique(deck_j):
                    pass
                action_raw = action[0]
                deck_j_hash = get_deck_hash(deck_j)
                if deck_j_hash == '6A8A2A1B':
                    pass
                decks_new_j = switcher.get(action_raw.split()[0])(deck_j[:], action_raw, action[1])
                duplicates = [deck for deck in decks_new_j if decks_new_j.count(deck) > 1]
                if len(duplicates):
                    pass
                # for deck_new_j in decks_new_j:
                #    deck_new_j[0].update("history") += int(''.join(deck_j_sign), 16)
                # TODO allow None (no deck, the action had no effect, could not be validly executed) switcher output and deal with it accordingly
                for deck_new_j in decks_new_j:
                    if get_deck_hash(deck_new_j) == '9C2C3C4D6A7D8A5D1C':
                        pass
                    if not check_cards_unique(deck_new_j):
                        pass
            decks_new_j = get_unique_items(decks_new_j[:])
            # decks_new_j = [i for i in decks_new_j if deck_changed(i, deck) or j == len(row)]
#            if len(decks_new_j) == 0:
#                decks_new_j.append(deck)

        decks_new_j_changed = [deck_changed(i, deck) for i in decks_new_j]
        if True in decks_new_j_changed:
            decks_new_j = [deck_new_j for i, deck_new_j in enumerate(decks_new_j) if decks_new_j_changed[i]]
            decks_new_i.extend(decks_new_j)
            decks_new_i = get_unique_items(decks_new_i[:])
            if deck[0][0].get('type') == 'monster':
                break
        else:
            decks_new_j_prev_nonchanged_rows.extend(decks_new_j)
            if i == len(deck[0][1][1:]) - 1:
                if deck[0][0].get('type') == 'monster' or not decks_new_i:
                    decks_new_i = get_unique_items(decks_new_j_prev_nonchanged_rows[:])

        # remove duplicates and remove the original deck, if others could be created

        # decks_new_i = [i for i in decks_new_i if deck_changed(i, deck)]
        # if len(decks_new_i) == 0:
        #    decks_new_i.append(deck)

    decks_new = get_unique_items(decks_new_i[:])

    for deck_i in decks_new:
        status_i = get_status(deck_i)

    if decks_new:
        for deck_i in decks_new:
            deck_i_new = leftShift(deck_i[:])
            deck_i_new_hash = get_deck_hash(deck_i_new)
            status = get_status(deck_i)
            if deck_i_new_hash not in global_decks_list:
                global_decks_list[deck_i_new_hash] = get_deck_hash(deck)
                if status.get("hero") != 0 and status.get("monster") != 0:
                    # no win or defeat, and deck changed, or it is the last action row iteration anyway
                    try:
                        play_card(deck_i_new[:])
                    except RecursionError as re:
                        print(deck_i_new_hash, ":", status, "recursion overflow")
                elif status.get("hero") == 0 or status.get("monster") == 0:
                    game_deck_i_new = get_game(deck_i_new_hash)
                    print(len(global_decks_list), ":", deck_i_new_hash, ":", status, 'start deck:', game_deck_i_new[-1], 'length of game:', len(game_deck_i_new)-1)
                    if status.get("monster") == 0:
                        pass
    else:
        pass

def get_deck_hash(d):
    d_id = []
    for card in d:
        d_id.append(str(card[0].get("number")) + card[1][0].get("face"))
    return ''.join(d_id)


def get_game(d_hash):
    game_hash = []
    d_i_hash = d_hash[:]
    key_found = True
    game_hash.append(d_i_hash)
    while key_found:
        d_prev_hash = global_decks_list.get(d_i_hash)
        if d_prev_hash:
            game_hash.append(d_prev_hash)
            d_i_hash = d_prev_hash[:-2] + d_prev_hash[-2:]
        else:
            key_found = False
    return game_hash


def print_actions(deck):
    switcher = {
        "hit": lambda d: leftShift(d[0][1]),
        "push": lambda d: d,
        "rotate": lambda d: d
    }

    for row in deck[0][1][1:]:
        print(row)
        for action in row:
            print(action)
            return switcher.get(action[0])(deck)


def get_deck(d_hash):
    deck = []
    d_items = [d_hash[i:i + 2] for i in range(0, len(d_hash), 2)]
    for number_face in d_items:
        for card in all_cards.cards:
            number = int(number_face[:-1])
            face = number_face[-1]
            if card[0].get("number") == number:
                c_new = rotate_card_to_face(card[:], face)
                deck.append(c_new)
    return deck


# deck_hash = '1A6A2A7A3A8A4A9A5A'
deck_hash = '1A6A2A8A'
deck = get_deck(deck_hash)

global_decks_list = dict()

play_card(deck)
