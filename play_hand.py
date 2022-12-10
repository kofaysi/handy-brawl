import all_cards
import numpy as np

deck_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
deck = []
for number in deck_numbers:
    for card in all_cards.cards:
        if card[0].get("number") == number:
            deck.append(card)


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
    d_new = d
    if d[i][1][1][0][1] == 0.5:
        d_new[i] = rotate(d[i])
    else:
        if flip(d[i])[1][1][0][1] == 0.5:
            d_new[i] = flip(d[i])
        else:
            d_new[i] = rotate_flip(d[i])
    return d_new


def deck_changed(d, d_new):
    return d[1:] != d_new[1:]


def move(d, i, p):
    if i > p:
        d_new = d[:i+1] + d[i-1:p] + d[i] + d[p-1:]
    else:
        d_new = d[:p] + d[i] + d[p-1:i+1] + d[i-1:]
    return d_new


def move_card(d, t, r):
    ds_new = []
    m = None
    if r > 0:
        for i in reversed(range(r-1)):
            if t == "self":
                if d[0][0].get("type") == d[i+1][0].get("type") and d[i+1][1][1].get("life") != "exhausted":
                    m = i + 1
                    break
            elif t == "enemy":
                if d[0][0].get("type") != d[i+1][0].get("type") and d[i+1][1][1].get("life") != "exhausted":
                    m = i + 1
                    break
            else:
                if d[i+1][1][1].get("life") != "exhausted":
                    m = i+1
                    break
        ds_new.append(move(d, m, 1))
    elif r < 0:
        for i in range(r-1):
            if t == "self":
                if d[0][0].get("type") == d[i+1][0].get("type") and d[i+1][1][1].get("life") != "exhausted":
                    m = i + 1
                    break
            elif t == "enemy":
                if d[0][0].get("type") != d[i+1][0].get("type") and d[i+1][1][1].get("life") != "exhausted":
                    m = i + 1
                    break
            else:
                if d[i+1][1][1].get("life") != "exhausted":
                    m = i + 1
                    break
        ds_new.append(move(d, m, len(d)))
    return ds_new


def rotate_top(d):
    d_new = d
    d_new[0] = rotate(d[0])
    return d_new


def use_shield(d, i):
    d_new = d

    switcher = {
        "rotate": lambda c: rotate(c),
        "do_nothing": lambda c: c
    }

    action = d[i][1][0].get("shield")
    d_new[i] = switcher.get(action)(deck[i])
    return d_new


def top_card_to_bottom(d):
    d_new = leftShift(d)
    return d_new


def hit_card(d, n):
    shield_found = False
    ds_new = []
    for i in range(1, n-1):
        if d[i+1][1][0].get("reaction") == "shield":
            shield_found = True
            ds_new.append(use_shield(d, i+1))
    if not shield_found:
        for i in range(1, n):
            if d[0][0].get("type") != d[i][0].get("type") and d[i][1][0].get("life") != "exhausted":
                ds_new.append(deal_damage(d, i))
    return ds_new


def victory_status(deck):
    status_hero = 0
    status_monster = 0
    for card in deck:
        if card[0].get("type") == "hero":
            status_hero += card[0][1].get("life") != "exhausted"
        else:
            status_monster += card[0][1].get("life") != "exhausted"
        if status_hero == 0:
            return "lost"
        if status_monster == 0:
            return "won"


def delay_card(d, t, p):
    ds_new = []
    m = None
    for i in range(1, len(d)):
        for j in range(1, abs(p)):
            if t == "self":
                if d[0][0].get("type") == d[i][0].get("type"):  # and d[i][1][1].get("life") != "exhausted":
                    m = i
            elif t == "enemy":
                if d[0][0].get("type") != d[i][0].get("type"):  # and d[i][1][1].get("life") != "exhausted":
                    m = i
            else:
                # if d[i][1][1].get("life") != "exhausted":
                m = i
            end_position = m-np.signum(p)*j
            if len(d) >= end_position >= 1:
                ds_new.append(move(d, m, end_position))
    return ds_new


def refresh(c):
    card_new = None
    for card in all_cards.cards:
        if card[0].get("number") == c[0].get("number"):
            card_new = card
            break
    return card_new


def heal_deck(d):
    ds_new = []
    for i in range(1, len(d)):
        if d[0][0].get("type") == d[i][0].get("type") and d[i][1][0].get("life") == "exhausted":
            d_new = d
            d_new[i] = refresh(d[i])
            ds_new.append(d_new)
    return ds_new


def maneuver_deck(d):
    ds_new = []
    for i in range(1, len(d)):
        if d[0][0].get("type") == d[i][0].get("type") and d[i][1][0].get("life") == "healthy":
            d_new = d
            d_new[i] = rotate(d[i])
            ds_new.append(d_new)
    return ds_new


def arrow_deck(d, n):
    ds_new = []
    m = len(d)
    for i in range(m-2, m):
        if d[0][0].get("type") != d[i][0].get("type") and d[i][0].get("reaction") != "shield":
            d_new = deal_damage(d, i)
        if n == "double":
            for j in range(m - 2, m):
                if j != i and d[0][0].get("type") != d[i][0].get("type") and d[i][0].get("reaction") != "shield":
                    d_new = deal_damage(d_new, i)
        ds_new.append(d_new)
    return ds_new


def play_card(deck):
    decks = []
    decks.append(deck)
    status = []
    switcher = {
        "hit": lambda d, a, n: hit_card(d, n),
        "arrow": lambda d, a, n: arrow_deck(d, a.split[1]),
        "push*": lambda d, a, r: move_card(d, a.split[1], r),
        "pull*": lambda d, a, r: move_card(d, a.split[1], -r),
        "delay*": lambda d, a, p: delay_card(d, a.split[1], p),
        "quicken*": lambda d, a, p: delay_card(d, a.split[1], -p),
        "rotate": lambda d, a, n: rotate_top(d),
        "heal": lambda d, a, n: heal_deck(d),
        "maneuver": lambda d, a, n: maneuver_deck(d),
    }
    for i, row in enumerate(deck[0][1][1:]):
        for action in row:
            for deck_i in decks:
                if i == 0:
                    decks == []
                decks.append(switcher.get(action[0])(deck_i, action[0], action[1]))
            if decks:
                for deck_i in decks:
                    status = victory_status(deck_i)
                    if status is None and \
                            (deck_changed(deck, deck_i) or i == len(deck[0][1][1:])):
                        # no win or defeat, deck changed, or it is the last iteration anyway
                        try:
                            deck_i = leftShift(deck_i)
                            play_card(deck_i)
                        except RecursionError as re:
                            pass
    return status


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


print(deck[0])
play_card(deck)

new_card = flip(deck[0])
print(new_card)