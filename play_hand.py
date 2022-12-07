import all_cards

deck = all_cards.paladin


def rotateCardVertically(c):
    return [c[0], c[3], c[4], c[1], c[2]]


def rotateCardHorizontally(c):
    return [c[0], c[2], c[1], c[4], c[3]]


def rotateCardFlip(c):
    return rotateCardVertically(rotateCardHorizontally(c))


def leftShift(tup, n=1):  # by default, the top card goes to the bottom of the deck
    try:
        n = n % len(tup)
    except ZeroDivisionError:
        return tuple()
    return tup[n:] + tup[0:n]

# def push(hand_of_cards, card_to_push, steps_to_push):
#     print()


def whatever():
    print("whatever")


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


def attack_card(d, i):
    return d


def deck_changed(d, d_new):
    return d[1:] == d_new[1:]


def make_push(d, p):
    return d


def rotate_top_vertical(d):
    return d


def use_shield(d, i):
    return d


def play_card(deck):

    def attack_deck(d, n):
        for i in range(n-1):
            d_new = attack_card(d, i+1)
            if deck_changed(d, d_new):
                try:
                    play_card(d_new)
                    print("attack")
                except RecursionError as re:
                    pass

        for i in range(n-2):
            if "shield" == d[i+1][0]:
                d_new = use_shield(d, i+1)
                if deck_changed(d, d_new):
                    try:
                        play_card(d_new)
                        print("shield")
                    except RecursionError as re:
                        pass
    switcher = {
        "attack": lambda d, n: attack_deck(d, n),
        "push": lambda d, p: make_push(d, p),
        "rotate_vertical": lambda d, n: rotate_top_vertical(d)
    }
    for row in deck[0][1][1:]:
        for action in row:
            return switcher.get(action[0])(deck, action[1])
    return deck


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

new_card = rotateCardVertically(deck[0])
print(new_card)
