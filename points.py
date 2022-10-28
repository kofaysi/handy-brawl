#!/usr/bin/env python
cards = []
cards.append([
    [
        [], # first one is always passive
        [("attack", 2)],
        [("push", 2), ("rotate", 0) ]
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
        [], # first one is always passive
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
        [], # first one is always passive
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
        [("shield", 0), ("rotate", 0)], # first one is always passive
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
        [("shield", 0), ("rotate", 0)], # first one is always passive
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
        [("trap", 0)], # first one is always passive
        [("arch", 0), ("rotate", 0)],
        [("push-hero", 2), ("rotate-other", 0) ]
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
        [("run", 0), ("rotate", 0)], # first one is always passive
        [("arch", 0), ("rotate", 0)],
        [("pull-enemy", 2), ("rotate-other", 0), ("rotate", 0) ],
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
        [("run", 0), ("rotate", 0)], # first one is always passive
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
        [("trap", 0)], # first one is always passive
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
        [("run", 0), ("rotate", 0)], # first one is always passive
        [("aarch", 0), ("rotate", 0)],
        [("pull-emeny", 1), ("rotate", 0)]
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

def countMovingActions(cards):
    res = 0
    for card in cards:
        for face in card:
            for option in face:
                for (op, value) in option:
                    if (op == "push" or op == "pull"):
                        res += value
                    elif (op == "push-hero" or op == "pull-enemy"):
                        res += value*0.75
    return res

def scoreAction(action, cards, icard, iface, rec=False):
    card = cards[icard]
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
        thisFace = scoreFace(cards, icard, iface)
        otherFace = scoreFace(cards, icard, (iface+1)%2)
        return (otherFace - thisFace)/4.0
    elif op == "trap":
        return countMovingActions(cards[:icard]+cards[icard+1:])/10.0
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

def scoreOption(option, cards, icard, iface, rec=False):
    card = cards[icard]
    value = 0
    for action in option:
        value += scoreAction(action, cards, icard, iface, rec)
    #if rec:
    #    print(">>", option, value)
    return value;


def scoreFace(cards, icard, iface, rec=False):
    card = cards[icard]
    valueAct = 0
    for option in card[iface][1:]:
        valueAct += scoreOption(option, cards, icard, iface, rec)
    valueAct = float(valueAct)/len(card[iface][1:]) + len(card[iface][1:])/2.0
    valuePass = scoreOption(card[iface][0], cards, icard, iface, rec)
    value = valueAct + valuePass
    #if rec:
    #    print(card[iface], value)
    return value;

def countDeck(cards):
    deck = 0
    for icard in range(len(cards)):
        value = 0
        for iface in range(len(cards[icard])):
            value += scoreFace(cards, icard, iface, True)
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

import itertools

def findsubsets(s, n):
    return list(itertools.combinations(s, n))

paladin = [("P-%d"%(i+1), paladin[i]) for i in range(len(paladin))]
archer = [("A-%d"%(i+1), archer[i]) for i in range(len(archer))]

possibleDecks = findsubsets(paladin + archer, 5)
print(len(possibleDecks))

def get_cards(deck):
    return [card for (name, card) in deck]

ranked = [(countDeck(get_cards(deck)), deck) for deck in possibleDecks]

# sort list with key
def takeFirst(elem):
    (a,b) = elem
    return a
ranked.sort(key=takeFirst)

def printDeck(deck):
    (point, cards) = deck
    print(point)
    for (name, faces) in cards:
        print(name)

printDeck(ranked[0])
printDeck(ranked[1])
printDeck(ranked[-1])
