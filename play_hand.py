import all_cards

deck = all_cards.paladin


def rotate_card_vertically(c):
    return [c[0], c[3], c[4], c[1], c[2]]


def rotate_card_horizontally(c):
    return [c[0], c[2], c[1], c[4], c[3]]


def rotate_card_flip(c):
    return rotate_card_vertically(rotate_card_horizontally(c))


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
        d_new[i] = rotate_card_horizontally(d[i])
    else:
        if rotate_card_vertically(d[i])[1][1][0][1] == 0.5:
            d_new[i] = rotate_card_vertically(d[i])
        else:
            d_new[i] = rotate_card_flip(d[i])
    return d_new


def deck_changed(d, d_new):
    return d[1:] != d_new[1:]


def push_card(d, p):
    for i in range(len(d)-1):
        if d[0][0][0] != d[i+1][0][0] and d[i+1][1][1][0][1] != 0:
            d_new = deal_damage(d, i+1)
        return d_new
    return d


def rotate_top_vertical(d):
    return d


def use_shield(d, i):
    return d


def top_card_to_bottom(d):
    d_new = []
    return d_new


def attack_card(d, n):
    for i in range(n-1):
        if d[0][0].get("type") != d[i+1][0].get("type") and d[i+1][1][0].get("health") != 0:
            d_new = deal_damage(d, i+1)
        return d_new
    for i in range(n-2):
        if d[i+1][1][0].get("shield") is not None:
            d_new = use_shield(d, i+1)
            return d_new


def victory_status(deck):
    status_hero = []
    status_monster = []
    for card in deck:
        if card[0].get("type") == "hero":
            status_hero += card[0][1].get("health")
        else:
            status_monster += card[0][1].get("health")
        if status_hero == 0:
            return "lost"
        if status_monster == 0:
            return "won"


def play_card(deck):

    switcher = {
        "attack": lambda d, n: attack_card(d, n),
        "push": lambda d, p: push_card(d, p),
        "rotate_vertical": lambda d, n: rotate_top_vertical(d)
    }
    for i, row in enumerate(deck[0][1][1:]):
        for action in row:
            deck_new = switcher.get(action[0])(deck, action[1])
            status = victory_status(deck_new)
            if status is None or deck_changed(deck, deck_new) or i == len(deck[0][1][1:]):  # deck changed or the last iteration anyway
                try:
                    deck_new = leftShift(deck)
                    play_card(deck_new)
                except RecursionError as re:
                    pass
    return deck_new, status


def print_actions(deck):
    switcher = {
        "attack": lambda d: leftShift(d[0][1]),
        "push": lambda d: d,
        "rotate_vertical": lambda d: d
    }

    for row in deck[0][1][1:]:
        print(row)
        for action in row:
            print(action)
            return switcher.get(action[0])(deck)


print(deck[0])
play_card(deck)

new_card = rotate_card_vertically(deck[0])
print(new_card)
