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
    d_new = d
    if d[i][1][0].get("life") == "healthy":
        expected_life = "wounded"
    else:
        expected_life = "exhausted"
    for j in range(1, 5):
        if deck[i][j][0].get("life") == expected_life:
            expected_face = deck[i][j][0].get("face")
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
    return d_new


def deck_changed(d, d_new):
    if not check_cards_unique(d):
        pass
    if not check_cards_unique(d_new):
        pass

    return d[1:] != d_new[1:]


def swap(d, i, j):
    if not check_cards_unique(d):
        pass
#     d[i], d[j] = d[j], d[i]
    # # TODO check the code
    if i < j:
        d[i:j] = leftShift(d[i:j])
    else:
        d[j:i] = leftShift(d[j:i], len(d[i:j]))
    return d

    return d


def move_card(d, a, r):
    if not check_cards_unique(d):
        pass
    ds_new = []
    if ' ' in a:
        t = a.split()[1]
    else:
        t = "any"
    m = None
    if r > 0:
        for i in reversed(range(1, r+1)):
            if t == "self":
                if d[0][0].get("type") == d[i][0].get("type") and d[i][1][0].get("life") != "exhausted":
                    m = i
                    break
            elif t == "enemy":
                if d[0][0].get("type") != d[i][0].get("type") and d[i][1][0].get("life") != "exhausted":
                    m = i
                    break
            else:
                if d[i][1][0].get("life") != "exhausted":
                    m = i
                    break
        if m:
            ds_new.append(swap(d, m, 1))
    elif r < 0:
        for i in range(1, abs(r)+1):
            if t == "self":
                if d[0][0].get("type") == d[i][0].get("type") and d[i][1][0].get("life") != "exhausted":
                    m = i
                    break
            elif t == "enemy":
                if d[0][0].get("type") != d[i][0].get("type") and d[i][1][0].get("life") != "exhausted":
                    m = i
                    break
            else:
                if d[i][1][0].get("life") != "exhausted":
                    m = i
                    break
        if m:
            ds_new.append(swap(d[:], m, len(d)-1))
    if ds_new:
        return ds_new
    else:
        return [d[:]]


def rotate_top(d):
    if not check_cards_unique(d):
        pass
    d_new = d
    d_new[0] = rotate(d[0])
    ds_new = [d_new]
    return ds_new


def use_shield(d, i):
    if not check_cards_unique(d):
        pass
    d_new = d

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
    for i in range(1, n+1):
        if d[i][1][0].get("reaction") == "shield":
            shield_found = True
            d_new = use_shield(d[:], i)
            if not check_cards_unique(d_new):
                pass
            ds_new.append(d_new)
    if not shield_found:
        for i in range(1, n+1):
            if d[0][0].get("type") != d[i][0].get("type") and d[i][1][0].get("life") != "exhausted":
                d_new = deal_damage(d[:], i)
                if not check_cards_unique(d_new):
                    pass
                ds_new.append(d_new)
    if ds_new:
        return ds_new
    else:
        return [d]  # ds_new.append(d)


def get_unique_items(list):
    unique = []
    for item in list:
        if item not in unique:
            unique.append(item)
    return unique


# noinspection PyShadowingNames
def victory_status(deck):
    status_hero = 0
    status_monster = 0
    score = dict(healthy=1, wounded=0.5, exhausted=0)
    for card in deck:
        card_score = score.get(card[1][0].get("life"))
        if card[0].get("type") == "hero":
            status_hero += card_score
        else:
            status_monster += card_score
    if status_monster == 0:
        status = (status_hero - status_monster, "hero won, monster lost")
    elif status_hero == 0:
        status = (status_hero - status_monster, "hero lost, monster won")
    else:
        status = (status_hero - status_monster, None)
    return status_hero, status_monster


def delay_card(d, a, p):
    if ' ' in a:
        t = a.split()[1]
    else:
        t = "any"
    ds_new = []
    m = None
    for i in range(1, len(d)):
        for j in range(1, abs(p)+1):
            if t == "self":
                if d[0][0].get("type") == d[i][0].get("type"):  # and d[i][1][1].get("life") != "exhausted":
                    m = i
            elif t == "enemy":
                if d[0][0].get("type") != d[i][0].get("type"):  # and d[i][1][1].get("life") != "exhausted":
                    m = i
            else:
                # if d[i][1][1].get("life") != "exhausted":
                m = i
            if p > 0:
                end_position = m + j
            else:
                end_position = m - j
            if len(d) > end_position >= 1:
                d_new = swap(d[:], m, end_position)
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
    for i in range(1, len(d)-1):
        if d[0][0].get("type") == d[i][0].get("type") and d[i][1][0].get("life") == "exhausted":
            d_new = d
            d_new[i] = refresh(d[i])
            ds_new.append(d_new)
            if not check_cards_unique(d_new):
                pass
    if ds_new:
        return ds_new
    else:
        return [d]


def maneuver_deck(d):
    ds_new = []
    for i in range(1, len(d)+1):
        if (d[0][0].get("type") == d[i][0].get("type") and
                d[i][1][0].get("life") == d[i][2][0].get("life") and
                d[i][1][0].get("life") == "healthy" and d[i][2][0].get("life") == "wounded" and
                d[i][1][0].get("life") == "healthy" and d[i][2][0].get("life") == "exhausted" and
                d[i][1][0].get("life") == "wounded" and d[i][2][0].get("life") == "exhausted"):
            d_new = d
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
    for i, row in enumerate(deck[0][1][1:]):
        decks = [deck]
        decks_new_i = []
        decks_new_j = []
        for j, action in enumerate(row):
            if j > 0:
                decks = decks_new
                decks_new_j = []
            for deck_j in decks:
                if not check_cards_unique(deck_j):
                    pass
                action_raw = action[0]
                decks_new_j = switcher.get(action_raw.split()[0])(deck_j[:], action_raw, action[1])
                if len(decks_new_j) == 9:
                    pass
                for d in decks_new_j:
                    if not check_cards_unique(d):
                        pass
                decks_new_i.extend(decks_new_j)

            # remove duplicates and remove the original deck, if others could be created
            decks_new_i = get_unique_items(decks_new_i[:])
            if len(decks_new_i) == 1:
                pass
            if len(decks_new_i) > 1 and deck in decks_new_i:
                decks_new_i.remove(deck)
        decks_new.extend(decks_new_i)

        for deck_i in decks_new:
            if deck_i in global_list:
                decks_new.remove(deck_i)
            else:
                global_list.append(deck_i)


        if decks_new:
            for deck_i in decks_new:
                stati = victory_status(deck_i)
                deck_i_id = get_deck_setup(deck_i)
                deck_id = get_deck_setup(deck)
                if (stati[0] != 0 and stati[1] != 0) and deck_changed(deck, deck_i):
                    # no win or defeat, and deck changed, or it is the last action row iteration anyway
                    try:
                        deck_i = leftShift(deck_i)
                        play_card(deck_i)
                    except RecursionError as re:
                        pass
                        # TODO correct the deck rotation by -1
                        deck_i_id = get_deck_setup(deck_i)
                        print(stati, ":", deck_i_id)
                        # print("For deck", deck_i_id, "status:", status, "the max depth of recursion has been reached...")
                elif stati[0] == 0 or stati[1] == 0:
                    print(stati, ":", deck_i_id)


def get_deck_setup(d):
    d_id = []
    for card in d:
        d_id.append(str(card[0].get("number")) + card[1][0].get("face"))
    return d_id


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


def get_deck(d_items):
    deck = []
    for number_face in d_items:
        for card in all_cards.cards:
            number = int(number_face[:-1])
            face = number_face[-1]
            if card[0].get("number") == number:
                c_new = rotate_card_to_face(card[:], face)
                deck.append(c_new)
    return deck


deck_items = ["1A", "6A", "2A", "7A", "3A", "8A", "4A", "9A", "5A"]
deck = get_deck(deck_items)

global_list = []

print(deck[0])
play_card(deck)

new_card = flip(deck[0])
print(new_card)
