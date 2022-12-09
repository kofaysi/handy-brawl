import all_cards

deck = all_cards.warrior


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


def move_card(d, p):
    ds_new = []
    # TODO refactor method
    for i in range(len(d)-1):
        if d[0][0].get("type") != d[i+1][0].get("type") and d[i+1][1][1].get("life") != "exhausted":
            ds_new.append = deal_damage(d, i+1)
    return ds_new


def rotate_top_vertical(d):
    d_new = d
    d_new[0] = rotate_card_vertically(d[0])
    return d_new


def use_shield(d, i):
    d_new = d

    switcher = {
        "rotate_horizontally": lambda c: rotate_card_horizontally(c),
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
    for i in range(n-2):
        if d[i+1][1][0].get("shield") is not None:
            shield_found = True
            ds_new.append = use_shield(d, i+1)
    if not shield_found:
        for i in range(n - 1):
            if d[0][0].get("type") != d[i + 1][0].get("type") and d[i + 1][1][0].get("life") != "exhausted":
                ds_new.append = deal_damage(d, i + 1)
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


def delay_card(d, p):
    pass


def heal(d):
    pass


def maneuver(d):
    pass


def arrow_deck(d, n):
    pass


def play_card(deck):
    status = []
    switcher = {
        "hit": lambda d, a, n: hit_card(d, n),
        "arrow": lambda d, a, n: arrow_deck(d, a.split[1]),
        "push*": lambda d, a, p: move_card(d, a.split[1], p),
        "pull*": lambda d, a, p: move_card(d, a.split[1], -p),
        "delay*": lambda d, a, p: delay_card(d, a.split[1], p),
        "quicken*": lambda d, a, p: delay_card(d, a.split[1], -p),
        "rotate": lambda d, a, n: rotate_top_vertical(d),
        "heal": lambda d, a, n: heal(d),
        "maneuver": lambda d, a, n: maneuver(d),
    }
    for i, row in enumerate(deck[0][1][1:]):
        for action in row:
            decks_new = switcher.get(action[0])(deck, action[0], action[1])
            if decks_new:
                for deck_new in decks_new:
                    status = victory_status(deck_new)
                    if status is None and \
                            (deck_changed(deck, deck_new) or i == len(deck_new[0][1][1:])):
                        # no win or defeat, deck changed, or it is the last iteration anyway
                        try:
                            deck_new = leftShift(deck_new)
                            play_card(deck_new)
                        except RecursionError as re:
                            pass
    return status


def print_actions(deck):
    switcher = {
        "hit": lambda d: leftShift(d[0][1]),
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
