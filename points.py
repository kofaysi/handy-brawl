#!/usr/bin/env python

import itertools
from collections import deque

my_tuple = ("attack", "push", "")

cards = []
cards.append([
    [
        [],  # first one is always passive
        [("attack", 2)],
        [("push", 2), ("rotate", 0)]
    ],
    [
        [("shield", 2), ("rotate", 0)],
        [("push", 1), ("attack", 2)],
        [("push", 2)]
    ],
    [
        [],
        [("attack", 5)],
        [("push", 1)]
    ],
    [
        [],
        [("attack", 2)],
        [("push", 2)]
    ]
])
cards.append([
    [
        [],  # first one is always passive
        [("attack", 2), ("rotate", 0)],
        [("push", 2)]
    ],
    [
        [("shield", 0), ("rotate", 0)],
        [("heal", 0), ("rotate", 0)],
        [("push", 2)]
    ],
    [
        [],
        [("heal", 0), ("rotate", 0)],
        [("push", 2)]
    ],
    [
        [],
        [("pull", 2)],
        [("push", 2)]
    ]
])
cards.append([
    [
        [],  # first one is always passive
        [("push", 2), ("rotate", 0)],
        [("pull", 2), ("rotate", 0)]
    ],
    [
        [],
        [("attack", 4), ("attack", 4), ("rotate", 0)]
    ],
    [
        [],
        [("attack", 5)],
        [("push", 1)]
    ],
    [
        [],
        [("pull", 2)],
        [("push", 2)]
    ]
])
cards.append([
    [
        [("shield", 0), ("rotate", 0)],  # first one is always passive
        [("attack", 4)],
        [("push", 2)]
    ],
    [
        [],
        [("attack", 2)],
        [("push", 2), ("pull", 2), ("rotate", 0)]
    ],
    [
        [],
        [("attack", 5)],
        [("pull", 2)]
    ],
    [
        [],
        [("attack", 4)],
        [("heal", 0)]
    ]
])
cards.append([
    [
        [("shield", 0), ("rotate", 0)],  # first one is always passive
        [("pull", 2), ("attack", 2)]
    ],
    [
        [],
        [("attack", 2), ("rotate", 0)],
        [("pull", 2), ("rotate", 0)]
    ],
    [
        [],
        [("push", 3), ("attack", 2), ("attack", 2), ("rotate", 0)],
        [("pull", 2)]
    ],
    [
        [],
        [("attack", 3)],
        [("pull", 2)]
    ]
])
paladin = cards

# **************************************************
# Archer
# **************************************************
archer = []
archer.append([
    [
        [("trap", 0)],  # first one is always passive
        [("arch", 0), ("rotate", 0)],
        [("push-hero", 2), ("rotate-other", 0)]
    ],
    [
        [("trap", 0)],
        [("pull-enemy", 2), ("rotate-other", 0), ("rotate", 0)],
        [("heal", 0)]
    ],
    [
        [("trap", 0)],
        [("arch", 0), ("arch-other", 0)],
        [("rotate-other", 0)],
        [("pull", 1)]
    ],
    [
        [("trap", 0)],
        [("rotate-other", 0)],
        [("attack", 1)],
        [("push", 1)]
    ]
])
archer.append([
    [
        [("run", 0), ("rotate", 0)],  # first one is always passive
        [("arch", 0), ("rotate", 0)],
        [("pull-enemy", 2), ("rotate-other", 0), ("rotate", 0)],
        [("attack", 1), ("rotate", 0)]
    ],
    [
        [],
        [("push-hero", 2)],
        [("pull-enemy", 2)],
        [("rotate-other", 0), ("rotate-other", 0)]
    ],
    [
        [],
        [("attack", 1), ("attack", 1), ("rotate", 0)],
        [("pull-enemy", 1), ("rotate-other", 0)]
    ],
    [
        [],
        [("attack", 1), ("rotate-other", 0), ("push-hero", 2)]
    ]
])
archer.append([
    [
        [("run", 0), ("rotate", 0)],  # first one is always passive
        [("rotate-other", 0), ("pull-enemy", 2), ("rotate", 0)],
        [("push", 1), ("rotate", 0)]
    ],
    [
        [("trap", 0)],
        [("arch", 0), ("arch-other", 0)],
        [("push-hero", 2), ("rotate-other", 0)]
    ],
    [
        [("trap", 0)],
        [("push-hero", 2), ("arch", 0)],
        [("rotate-other", 0)]
    ],
    [
        [],
        [("push-hero", 2), ("pull-enemy", 2)],
        [("rotate-other", 0), ("attack", 1)]
    ]
])
archer.append([
    [
        [("trap", 0)],  # first one is always passive
        [("rotate-other", 0), ("rotate", 0)],
        [("attack", 1)],
        [("push", 1)]
    ],
    [
        [],
        [("arch", 0), ("rotate", 0)],
        [("rotate-other", 0), ("attack", 1), ("rotate", 0)],
        [("pull-enemy", 2)]
    ],
    [
        [],
        [("arch", 0)],
        [("pull-enemy", 2), ("rotate-other", 0)]
    ],
    [
        [("trap", 0)],
        [("arch", 0)],
        [("rotate-other", 0)],
        [("push", 1)]
    ]
])
archer.append([
    [
        [("run", 0), ("rotate", 0)],  # first one is always passive
        [("aarch", 0), ("rotate", 0)],
        [("pull-enemy", 1), ("rotate", 0)]
    ],
    [
        [],
        [("arch", 0), ("arch-other", 0)],
        [("push-hero", 2), ("rotate-other", 0)],
        [("heal", 0)]
    ],
    [
        [("trap", 0)],
        [("push-hero", 2), ("pull-enemy", 2)],
        [("rotate-other", 0), ("attack", 1)]
    ],
    [
        [],
        [("arch", 0)],
        [("push-hero", 2)],
        [("heal", 0)]
    ]
])


def count_moving_actions(cards):
    res = 0
    for card in cards:
        for face in card:
            for option in face:
                for (op, value) in option:
                    if op == "push" or op == "pull":
                        res += value
                    elif op == "push-hero" or op == "pull-enemy":
                        res += value*0.75
    return res


def score_action(action, cards, icard, iface, rec=False):
    # card = cards[icard]
    (op, value) = action
    if op == "attack":
        return value*2
    elif op == "push":
        return value
    elif op == "pull":
        return value
    elif op == "shield":
        return 5
    elif op == "run":
        return 2
    elif op == "heal":
        return 8
    elif op == "rotate" and iface == 2:
        return -5
    elif op == "rotate" and not rec:
        return 0
    elif op == "rotate" and rec:
        this_face = score_face(cards, icard, iface)
        other_face = score_face(cards, icard, (iface+1) % 2)
        return (other_face - this_face)/4.0
    elif op == "trap":
        return count_moving_actions(cards[:icard] + cards[icard + 1:])/10.0
    elif op == "arch":
        return 3*2+2
    elif op == "arch-other":
        return 2*2+1
    elif op == "push-hero":
        return value * 0.5
    elif op == "pull-enemy":
        return value * 0.5
    elif op == "rotate-other":
        return 1
    return 0


def score_option(option, cards, icard, iface, rec=False):
    # card = cards[icard]
    value = 0
    for action in option:
        value += score_action(action, cards, icard, iface, rec)
    # if rec:
    #    print(">>", option, value)
    return value


def score_face(cards, icard, iface, rec=False):
    card = cards[icard]
    value_act = 0
    for option in card[iface][1:]:
        value_act += score_option(option, cards, icard, iface, rec)
    value_act = float(value_act)/len(card[iface][1:]) + len(card[iface][1:])/2.0
    value_pass = score_option(card[iface][0], cards, icard, iface, rec)
    value = value_act + value_pass
    # if rec:
    #    print(card[iface], value)
    return value


def countDeck(cards):
    deck = 0
    for icard in range(len(cards)):
        value = 0
        for iface in range(len(cards[icard])):
            value += score_face(cards, icard, iface, True)
        print(">>>>>> %f" % value)
        deck += value
    return deck


print("paladin %f" % countDeck(paladin))
print("archer %f" % countDeck(archer))
print("mix %f" % countDeck([
    paladin[0],
    paladin[1],
    paladin[2],
    archer[0],
    paladin[4]
]))


def findsubsets(s, n):
    return list(itertools.combinations(s, n))


paladin = [("P-%d" % (i+1), paladin[i]) for i in range(len(paladin))]
archer = [("A-%d" % (i+1), archer[i]) for i in range(len(archer))]

possibleDecks = findsubsets(paladin + archer, 5)
print(len(possibleDecks))


def get_cards(deck):
    return [card for (name, card) in deck]


ranked = [(countDeck(get_cards(deck)), deck) for deck in possibleDecks]


# sort list with key
def takeFirst(elem):
    (a, b) = elem
    return a


ranked.sort(key=takeFirst)


def printDeck(deck):
    (point, cards) = deck
    print(point)
    for (name, faces) in cards:
        print(name)


printDeck(ranked[0])
printDeck(ranked[-1])
printDeck(ranked[101])
printDeck(ranked[60])
