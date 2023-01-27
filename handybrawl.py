"""
Functions to manipulate the virtual deck of cards according to the Handy Brawl game rules.

The deck is represented as a list with lists (cards) from top (start=0) to bottom (end=len(deck)-1). 

Functions:

- rotate_card_to_face(c : list, f : str) -> list:
- flip(c : list) -> list:
- rotate(c : list) -> list:
- rotate_flip(c : list) -> list:
- back_shift(tup : tuple, n=1 : int) -> tuple:
- check_cards_unique(d : list) -> bool:
- unzip_hash(d_hash : str) -> list, list:
- deck_changed(d1 : list, d2 : list, i=1 : int) -> bool:
- adjust_deck(d : list, a : str, p : str) -> list:
- move_deck(d : list, a : str, r : str) -> list:
- move_card(d : list, i : int, j : int) -> list:
- rotate_top_card(d : list, i=0 : int) -> list:
- hit_deck(d : list, n : int) -> list:
- intercept(d : list, i : int, reaction) -> list:
- hit_card(d : list, i : int) -> list:
- revive_deck(d : list, a : str) -> list:
- revive_card(c : list) -> list:
- get_unique_items(lst : list) -> list:
- get_status(d : list) -> dict:
- maneuver_deck(d : list) -> list:
- iter_combs(n : int, k : int) -> list:
- arrow_deck(d : list, t=1 : int, e=-3 : int) -> list:
- teleport_deck(d : list, t : int) -> list:
- inspire_deck(d : list) -> list:
- get_deck_hash(d : list) -> list:
- create_deck(d_hash : str, cards) -> list:
- recreate_game(d_hash : str) -> list:
- play_card(deck : list): -> list:

Variables:

- game_turns : dict
    Dictionary to store the hashes of the game turns, game_turns[result] = origin.
    There can be multiple origins, but only one result is counted, when executing or comparing multiple games.
    The deck hash with no existing key with the same name, is the starting/first deck.
- card_status_symbols : dict
    Dictionary of status names and symbols for displaying in terminal.
- card_colours : dict
    Dictionary of card names and colours for displaying in terminal.
"""

from colorama import Fore, Style  # , Back
from cards import cards
import copy
import deck

game_turns = dict()


class CountCalls:
    """
    Use @CountCalls as a decorator to add a new method/property to a function
    """
    def __init__(self, func):
        self._count = 0
        self._func = func

    def __call__(self, *args, **kwargs):
        self._count += 1
        return self._func(*args, **kwargs)

    @property
    def call_count(self):
        return self._count


faces = ["A", "B", "C", "D"]


# @CountCalls
def rotate_card_to_face(c, f):
    """
    rotate a card c to a desired face f

    :param c: a card
    :param f: a face ["A", "B", "C", "D"]
    :return: the new card
    """
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
    # todo transcribe a werewolf feature of the face into the head of the card
    return c_new


# @CountCalls
def flip(c):
    """
    Flip the card, back side becomes the front and front side becomes the back (back-flip)

    Game rules applicable:
        Flip: Flip this card along the long edge.

    :param c: a card
    :return: a new card
    """
    # todo transcribe a werewolf feature of the face into the head of the card
    return [c[0], c[3], c[4], c[1], c[2]]


# @CountCalls
def rotate(f):
    """
    rotate the card, top side becomes the bottom and the bottom side becomes the top, sides do not change

    Game rules applicable:
        Rotate: Rotate this card 180° without changing the side. This action is mandatory.

    :param c: a card
    :return: a new card
    """
    # todo transcribe a werewolf feature of the face into the head of the card
    faces_rotated = ["B", "A", "D", "C"]
    return faces_rotated[faces.index(f)]


# @CountCalls
def back_shift(tup, n=1):
    """
    Send n (int) top cards to the bottom of the deck, one-by-one
    By default, a single (the top) card goes to the bottom of the deck

    :param tup: the current deck
    :param n: the number of positions to backshift by
    :return: the new deck
    """
    try:
        n = n % len(tup)
    except ZeroDivisionError:
        return tuple()
    return tup[n:] + tup[0:n]


# @CountCalls
def check_cards_unique(d) -> bool:
    """
    check cards in the deck are unique, only numbers are checked for uniqueness, faces are ignored

    :param d: a deck
    :return: bool True if card numbers in the deck are unique
        bool False if card numbers in the deck are not unique
    """
    return len(d.cards) == len({c[0] for c in d.cards})


def unzip_hash(d_hash):
    """
    process the hash char by char and collect the numbers and faces in two individual lists

    :param d_hash: the hash of a deck
    :return: two lists, a list of numbers and a list of faces
    """
    faces = []
    numbers = []
    hash_new = ''
    # create a new has in which train of alphas are separated by a separator ' ' (blank space) from train of numerics
    # import re is avoided on purpose. the function runs seldom.
    for i, s in enumerate(d_hash):
        if i > 0 and d_hash[i - 1].isalpha() ^ s.isalpha():
            hash_new += ' '
        hash_new += s

    # split the string by the separator ' '
    hash_list = hash_new.split(' ')

    # collect str and int to separate lists
    for item in hash_list:
        if item.isalpha():
            faces.append(item)
        else:  # elif item.isnumeric()
            numbers.append(int(item))
    return numbers, faces


# @CountCalls
def deck_changed(d1, d2, i=1) -> bool:
    """
    Check whether two decks are unique or differing, all cards are check except the top card

    :param d1: a deck of cards
    :param d2: a deck of cards
    :param i: a start index to slice the lists for comparison d[start:]
    :return: bool True if decks are differing
    """
    return d1.cards[i:] != d2.cards[i:]


# @CountCalls
def adjust_deck(d, p, t):
    """
    move_card() any possible card by p (int) positions within the deck

    Game rules applicable:
    hero:
        Quicken: Move any card up to X spaces towards top of the deck.
        Delay: Move any card up to X spaces towards top of the deck.
        Feature: Trap Master
            If an enemy card moves over a card with this feature, deal damage to it.
        Feature: Venom
            Prevents an enemy card directly in front of this card from performing actions that change cards position:
            DELAY, QUICKEN, TELEPORT.

    :param d: the current deck
    :param p: number of position to take the action by
    :param t: target side
    :return: new decks
    """
    is_venom = cards[d.cards[1][0]][d.cards[1][1]][0].get("feature") == "venom"
    first_card_type = cards[d.cards[0][0]]['header']["type"]

    # the next card displays feature "venom" and prevents from activating the top hero card
    if first_card_type == "hero" and is_venom:
        return []

    # t = a.split()[1] if ' ' in a else "any"
    ds_new = []
    # adjust_list = list(range(1, abs(p) + 1))
    step_j = 1 if p > 0 else -1
    for i in range(1, len(d.cards)):
        if ((t == "ally" or t == "any") and cards[d.cards[0][0]]['header']["type"] == cards[d.cards[i][0]]['header']["type"]) \
                or ((t == "enemy" or t == "any")
                    and cards[d.cards[0][0]]['header']["type"] != cards[d.cards[i][0]]['header']["type"]
                    and not ("heavy" in cards[d.cards[i][0]][d.cards[i][1]][0].get("feature", {}))):
            d_new = copy.deepcopy(d)
            j = i
            for _ in range(1, abs(p) + 1):
                if 0 < j + step_j < len(d.cards):
                    d_new = move_card(d_new, j, j + step_j)
                    trap_exist = "traps" in cards[d.cards[j][0]][d.cards[j][1]][0].get("feature", {})
                    if cards[d.cards[0][0]]['header']["type"] != cards[d.cards[j][0]]['header']["type"] and trap_exist:
                        d_new = hit_card(d_new[:], j+step_j)
                    ds_new.append(d_new)
                j += step_j
    ds_new = get_unique_items(ds_new)
    return ds_new


# @CountCalls
def move_deck(d, r, t):
    """
    move_card() any possible card within the deck

    Game rules applicable:
    (all needs rewording)
    hero:
        Pull: Move the furthest card in range X behind the active card.
        Push: Move the closest enemy card in range X to the bottom of the deck. (needs rewording)
    monster:
        Pull: Move the furthest card in range X behind the active card.
              Don't target enemy cards. (needs rewording)
        Push: Move the closest enemy card in range to the bottom of the deck.

    :param d: current deck
    :param r: range
    :param t: target side
    :return: new collected decks
    """
    ds_new = []
    # t = a.split()[1] if ' ' in a else "any"
    move_range = range(1, min(abs(r) + 1, len(d)))
    if r < 0:
        move_range = reversed(move_range)
    for i in list(move_range):
        if (
                (t == "ally" or t == "any") and
                cards[d.cards[0][0]]['header']["type"] == cards[d.cards[i][0]]['header']["type"]
        ) or (
                    (
                            (t == "enemy" or t == "any") and
                            cards[d.cards[0][0]]['header']["type"] != cards[d.cards[i][0]]['header']["type"]
                            # Heavy card cannot be moved by any enemy action.
                            and "heavy" not in cards[d.cards[i][0]][d.cards[i][1]][0].get("feature", {})
                    ) and
                    # for monster: do not pull exhausted enemies
                    not (cards[d.cards[0][0]]['header']["type"] == "monster"
                         and r < 0
                         and cards[d.cards[i][0]][d.cards[i][1]][0]["life"] == "exhausted")
        ):
            end_position = 1 if r < 1 else len(d) - 1
            ds_new.append(move_card(d, i, end_position))
            if cards[d.cards[0][0]]['header']["type"] == "monster":
                break
    return ds_new if ds_new != [d] else []


# @CountCalls
def move_card(d, i, j):
    """
    move the i-th card to the j-th position in the deck, shift the cards inbetween

    Game rules applicable:
        Pull: Move the closest enemy card in range X to the bottom of the deck.
        Push: Move the furthest card in range X behind the active card.

    :param d: the current deck
    :param i: the i-the card to be moved
    :param j: the j-the position to be moved to
    :return: the new deck
    """
    d_new = copy.deepcopy(d)
    if not check_cards_unique(d):
        pass
    if i < j:
        d_new.cards[i:j + 1] = back_shift(d_new.cards[i:j + 1])
    else:
        d_new.cards[j:i + 1] = back_shift(d.cards[j:i + 1], len(d_new.cards[j:i + 1]) - 1)
    return d_new


# @CountCalls
def rotate_top_card(d, i=0):
    """
    rotate() the i-th card in the deck, default is the top card (i=0)

    Game rules applicable:
        Rotate: Rotate this card 180° without changing the side. This action is mandatory.
        (rewording) This action cannot be skipped.

    :param d: the current deck
    :param i: the i-th card in the deck
    :return: list of multiple new decks
    """
    d_new = copy.deepcopy(d)
    d_new.cards[i][1] = rotate(d_new.cards[i][1])
    return [d_new]


# @CountCalls
def hit_deck(d, r=0):
    """
    Deal damage to a card in the deck d within range n.
    Collect every possible optional result (new deck).

    Game rules applicable:
        Hit:
        Reaction: Shield:
            Don't target
        Feature: Webs
            Prevents an enemy card directly in front of this card from performing actions
            that change cards rotation: HIT, ARROW, MANEUVER, HEAL, REVIVE (reword) RESURRECT, FIREBALL, ABLAZE.

    :param d: the current deck
    :param r: the hit range, int
    :return: the new decks
    """
    is_webs = cards[d.cards[1][0]][d.cards[1][1]][0].get("feature") == "webs"
    first_card_type = cards[d.cards[0][0]]['header']["type"]

    # the next card displays feature "venom" and prevents from activating the top hero card
    if first_card_type == "hero" and is_webs:
        return []

    if not check_cards_unique(d):
        pass
    if d.hash_str == '5A6D7A9A8A1B4A2A3B':
        pass

    ds_new = []
    if r == 0 or r > len(d.cards) - 1:  # 0 is a substitute for the infinite hit range
        r = len(d.cards) - 1
    if cards[d.cards[0][0]]['header']["type"] == "hero":
        # for hero targeting monster, use the furthest shield first
        hit_list = list(reversed(range(1, r + 1)))
    else:
        # for monster targeting hero, follow hit order
        hit_list = list(range(1, r + 1))

    shield_found = False
    for i in hit_list:
        # Reaction: Shield: Don't target
        shield_reaction = cards[d.cards[i][0]][d.cards[i][1]][0].get("shield")
        if cards[d.cards[0][0]]['header']["type"] != cards[d.cards[i][0]]['header']["type"] \
                and shield_reaction:
            d_new = intercept(d, i, shield_reaction)
            shield_found = True
            if not check_cards_unique(d_new):
                pass
            if d_new != d:
                ds_new.append(d_new)
                # if monster's shield has been found and activated, break
                if cards[d.cards[0][0]]['header']["type"] == "hero":
                    break

    dodge_found = False
    found_hero = False
    for i in hit_list:
        # Reaction: Dodge: Don't target
        dodge_reaction = cards[d.cards[i][0]][d.cards[i][1]][0].get("dodge")
        if not found_hero and cards[d.cards[0][0]]['header']["type"] != cards[d.cards[i][0]]['header']["type"] \
                and dodge_reaction:
            if cards[d.cards[0][0]]['header']["type"] == "monster":
                found_hero = True
            dodge_found = True
            d_new = intercept(d, i, dodge_reaction)
            if not check_cards_unique(d_new):
                pass
            if d_new != d:
                ds_new.append(d_new)
                # if monster's shield has been found and activated, break
                if cards[d.cards[0][0]]['header']["type"] == "hero":
                    break

    # Continue collecting new deck outcomes by applying hit_card(), if it is a monster's turn,
    # or it is a hero's turn and no shield or no dodge has been found.
    # Activating ally's shield is not mandatory for the hero.
    if cards[d.cards[0][0]]['header']["type"] == "monster" \
            or (cards[d.cards[0][0]]['header']["type"] == "hero"
                and not (shield_found
                         or dodge_found)):
        for i in hit_list:
            if cards[d.cards[0][0]]['header']["type"] != cards[d.cards[i][0]]['header']["type"] \
                    and cards[d.cards[i][0]][d.cards[i][1]][0]["life"] != "exhausted":
                # even if it is mostly not effective,
                # hero may refuse to activate the shield or dodge and take damage instead
                d_new = hit_card(d, i)
                if not check_cards_unique(d_new):
                    pass
                if d_new != d:
                    ds_new.append(d_new)
                    # if closest hero has been hit, break
                    if cards[d.cards[0][0]]['header']["type"] == "monster":
                        break
    return ds_new


# @CountCalls
def intercept(d, i, reaction):
    """
    rotate() the i-th card in the deck as a result of the shield property/reaction of the card

    Game rules applicable:
    hero:
        Reaction: Shield
            If in range of you MAY intercept and negate the damage.
            (rewording) If in range of DAMAGE, you MAY intercept and negate the damage.
            If you do so, activate all icons after the arrow.
            (rewording) If you do so, activate all actions after the arrow.
        Reaction: Dodge
            If targeted by an enemy action, you MAY negate it.
            (rewording) If targeted by an enemy action, you MAY intercept and negate it.
            If you do so, activate all actions after the arrow.
    monster:
        Reaction: Block (reword or use a different icon)
            If in range of targeting an ally card, intercept and negate the damage.
            If you do so, activate all icons after the arrow.
            If multiple BLOCKS available, use the furthest.

    :param d: the current deck
    :param i: the i-th card
    :param reaction: a string describing the action after activating the intercept()
    :return: the new deck
    """
    if not check_cards_unique(d):
        pass
    d_new = copy.deepcopy(d)

    switcher = {
        "rotate": lambda f: rotate(f)
    }

    # try:
    #     action = cards[d.cards[i][0]][d.cards[i][1]]['header'].get(reaction)
    # except KeyError:
    #     # reaction to intercept does not exist
    #     action = None

    if reaction or reaction != "None":
        # a switcher construction used for multiple possible shield or dodge reactions
        d_new.cards[i][1] = switcher.get(reaction)(d.cards[i][1])
        if not check_cards_unique(d_new):
            pass
    return d_new


# @CountCalls
def hit_card(d, i):
    """
    Changes the life status of the i-th card in the deck to "wounded" if it is "healthy"
    and "exhausted" if it is "wounded"

    Game rules applicable:
    hero:
        Hit: Damage any non-[empty heart] (unexhausted) card in range X
    monster:
        Hit: Damage closest non-[empty heart] (unexhausted) enemy card in range X.

    :param d: the current deck
    :param i: the i-th card in the deck [0, 1...]
    :return: new deck (single)
    """
    # expected_face = ''
    expected_life = "wounded" if cards[d.cards[i][0]][d.cards[i][1]][0]["life"] == "healthy" else "exhausted"

    d_new = copy.deepcopy(d)
    d_new.cards[i][1] = faces[[cards[d.cards[i][0]][f][0]["life"] for f in faces].index(expected_life)]
    return d_new
    # expected_card = rotate_card_to_face(d[i][:], expected_face)


# noinspection PyShadowingNames
# @CountCalls
def revive_deck(d, a):
    """
    Heal or resurrect a card in the deck.
    Collect every possible optional result (new deck).

    Game rules applicable:
        Heal: Return any [half leaf] (wounded) to its starting position.
        Resurrect: Return closest ally card to its starting position.
        Feature: Webs
            Prevents an enemy card directly in front of this card from performing actions
            that change cards rotation: HIT, ARROW, MANEUVER, HEAL, REVIVE (reword) RESURRECT, FIREBALL, ABLAZE.

    :param d: the current deck
    :param a: action "resurrect" or "heal"
    :return: new decks
    """
    is_webs = cards[d.cards[1][0]][d.cards[1][1]][0].get("feature") == "webs"
    first_card_type = cards[d.cards[0][0]]['header']["type"]

    # the next card displays feature "venom" and prevents from activating the top hero card
    if first_card_type == "hero" and is_webs:
        return []

    if not check_cards_unique(d):
        pass
    ds_new = []
    for i in range(1, len(d.cards)):
        if cards[d.cards[0][0]]['header']["type"] == cards[d.cards[i][0]]['header']["type"]:
            if (a == "heal" and cards[d.cards[i][0]][d.cards[i][1]][0]["life"] == "wounded") \
                    or (a == "resurrect" and cards[d.cards[i][0]][d.cards[i][1]][0]["life"] == "exhausted"):
                d_new = copy.deepcopy(d)
                # was revive_card(d.cards[i])
                d_new.cards[i][1] = 'A'
                ds_new.append(d_new)
                if not check_cards_unique(d_new):
                    pass
                if cards[d.cards[0][0]]['header']["type"] == "monster":
                    break

    return ds_new


def revive_card(c):
    """
    Turn the card to its starting ("A") position.

    Game rules applicable:
        Heal: Return any [half leaf] (wounded) to its starting position.
        Resurrect: Return closest ally card to its starting position.

    :param c: a card
    :return: a new card
    """
    return rotate_card_to_face(c[:], 'A')


# @CountCalls
def get_unique_items(lst) -> "list":
    """
    Get unique items out of the lst (list).

    :param lst: a list of items possibly containing duplicates
    :return: a list of unique items
    """
    uniques = []
    for item in lst:
        if item not in uniques:
            uniques.append(item)
    return uniques


score = {"healthy": 1., "wounded": 0.5, "exhausted": 0.}


# @CountCalls
def get_status(d):
    """
    Check on the health status of the hero(s) and  monster(s).
    Calculate a simple numerical health score.

    :param d: the deck
    :return: the health status (dict('hero'=float, 'monster'=float))
    """
    status = {"hero": 0., "monster": 0.}
    for card in d.cards:
        card_type = cards[card[0]]['header'].get("type")
        card_score = score.get(cards[card[0]][card[1]][0].get("life"))
        status[card_type] += card_score

    return status


lives = ['healthy', 'wounded', 'exhausted']


# noinspection PyShadowingNames
# @CountCalls
def maneuver_deck(d):
    """
    Rotate an ally card in the deck, without increasing its life level.
    Collect every possible optional result (new deck).

    Game rules applicable:
        Maneuver: Rotate other ally card in a way that its health level doesn't increase.
        Feature: Webs
            Prevents an enemy card directly in front of this card from performing actions
            that change cards rotation: HIT, ARROW, MANEUVER, HEAL, REVIVE (reword) RESURRECT, FIREBALL, ABLAZE.

    :param d: the current deck
    :return: list of new decks
    """
    is_webs = cards[d.cards[1][0]][d.cards[1][1]][0].get("feature") == "webs"
    first_card_type = cards[d.cards[0][0]]['header']["type"]

    # the next card displays feature "venom" and prevents from activating the top hero card
    if first_card_type == "hero" and is_webs:
        return []

    ds_new = []
    for i in range(1, len(d.cards) - 1):
        face_rotated = rotate(d.cards[i][1])
        if cards[d.cards[0][0]]['header']["type"] == cards[d.cards[i][0]]['header']["type"]:
            life_rotated = cards[d.cards[i][0]][face_rotated]['header']['life']
            life_current = cards[d.cards[i][0]][d.cards[i][1]]['header']['life']
            if lives.index(life_current) <= lives.index(life_rotated):
                d_new = copy.deepcopy(d)
                d_new[i] = rotate(d[i])
                ds_new.append(d_new)
    return ds_new


def iter_combs(n, k):
    """
    Collect all combinations of k numbers using the first n numbers, $C_n^k$.
    Inspired by https://stackoverflow.com/questions/127704/algorithm-to-return-all-combinations-of-k-elements-from-n

    :param n:
    :param k:
    :return: list of C_n^k combinations
    """
    comb = []

    def itr(v, s, j):
        nonlocal comb
        if j == k:
            comb.append(v)
        else:
            for i in range(s, n):
                itr(v+[i], i+1, j+1)

    itr([], 0, 0)

    return comb


# @CountCalls
def arrow_deck(d, n=1, e=-3):
    """
    Deal damage to a card at the end of the deck.
    Collect every possible optional result (new deck).
    Only a hero action.

    Game rules applicable:
    hero:
        Arrow: Deal damage to any one of the 3 (and) bottom cards.
        Double arrow: Two arrow actions that cannot target the same card (you may still skip one of them).
        (rewording) Two arrow actions that shall target different cards (targeting only one card is allowed).
        Feature: Webs
            Prevents an enemy card directly in front of this card from performing actions
            that change cards rotation: HIT, ARROW, MANEUVER, HEAL, REVIVE (reword) RESURRECT, FIREBALL, ABLAZE.

    :param d: the current deck
    :param n: the number of targets, different cards targets are targeted
    :param e: number (int) of the cards att the end of the deck to be targeted possibly
    :return: new decks
    """
    # the next card displays feature "webs" and prevents from activating the top hero card
    if cards[d.cards[0][0]]['header']["type"] == "hero" \
            and "feature" in cards[d.cards[1][0]][d.cards[1][1]]['header'] \
            and "webs" in cards[d.cards[1][0]][d.cards[1][1]][0].get("feature"):
        return []

    ds_new = []
    # if targeting positions at the end of the deck
    if e < 0:
        target_list = list(range(len(d) + e - 1, len(d) + 1))
    else:  # target positions at the beginning of the deck (exercise)
        target_list = list(range(1, e + 1))
    # a targeted monster shall apply the shield

    for i in target_list:
        d_new = copy.deepcopy(d)
        if cards[d.cards[i][0]]['header']["type"] == "monster":
            # todo: rewrite using check for "reaction" existence
            # also consider "dodge" as a reaction
            shield_reaction = cards[d.cards[i][0]][d.cards[i][1]][0].get("shield")
            if shield_reaction:
                d_new = intercept(d_new[:], i, shield_reaction)
            else:
                d_new = hit_card(d_new[:], i)
            if n == 2:  # double arrow
                for j in target_list:
                    if i < j \
                            and cards[d.cards[j][0]]['header']["type"] == "monster":
                        shield_reaction = cards[d.cards[j][0]][d.cards[j][1]][0].get("shield")
                        if shield_reaction:
                            d_new = intercept(d_new[:], j, shield_reaction)
                        else:
                            d_new = hit_card(d_new[:], j)
                        ds_new.append(d_new)
            else:
                ds_new.append(d_new)
    return ds_new


def teleport_deck(d, t):
    """
    Swap any of two cards (of corresponding sides, target).
    Collect every possible optional result (new deck).

    Game rules applicable:
        Teleport: Swap places of 2 cards (of corresponding sides)
        Feature: Venom
            Prevents an enemy card directly in front of this card from performing actions that change cards position:
            DELAY, QUICKEN, TELEPORT.

    :param d: the current deck
    # todo change "any" to "both" for teleporting one enemy and one ally, correct the code accordingly
    :param t: the target of teleport ("ally", "enemy", "any")
    """
    ds_new = []
    is_venom = cards[d.cards[1][0]][d.cards[1][1]][0].get("feature") == "venom"
    first_card_type = cards[d.cards[0][0]]['header']["type"]

    # the next card displays feature "venom" and prevents from activating the top hero card
    if first_card_type == "hero" and is_venom:
        return []

    for i in range(len(d)):
        for j in range(i+1, len(d)):
            if (t == "any"
                    or (t == "ally" and first_card_type == cards[d.cards[i][0]]['header']["type"] == cards[d.cards[j][0]]['header']["type"])
                    or (t == "enemy" and first_card_type != cards[d.cards[i][0]]['header']["type"] == cards[d.cards[j][0]]['header']["type"])):
                d_new = d.copy()
                d_new[i], d_new[j] = d_new[j], d_new[i]
                ds_new.append(d_new)
    return ds_new


def inspire_deck(d):
    """
    Apply play_card() for the part of the deck and concatenate results with the origin

    Game rules applicable:
        Inspire: Activate other closest ally card from the middle of the deck.
            Treat all the cards above it as if they didn't exist.

    :param d: the current deck
    """
    ds_new = []
    is_monster_turn = cards[d.cards[0][0]]['header']["type"] == "monster"
    for i, _ in enumerate(d):
        ds_new_i = play_card(d[i:])
        for d_new_i in ds_new_i:
            d_new = d[:i] + d_new_i
            if d_new != d:
                ds_new.append(d_new)
        if is_monster_turn:
            return ds_new
    return ds_new


# @CountCalls
def get_deck_hash(d):
    """
    Create a unique string identifying the deck.
    The string consists of numbers and faces in the order of the cards appearing in the deck.

    :param d: the deck
    :return: the hash (str)
    """
    d_id = [f"{card[0]}{card[1]}" for card in d.cards]
    return ''.join(d_id)


# @CountCalls
def create_deck(d_hash, cards=cards):
    """
    Create a deck consisting of cards based on the hash.

    :param d_hash: the unique hash (str)
    :param cards: the definition of all the available cards (list)
    :return: a deck, a list of cards, (list of lists)
    """
    # # d_numbers, d_faces = unzip_hash(d_hash)
    # # deck = [rotate_card_to_face(cards[n-1], d_faces[i].upper()) if cards[n-1][0].get("number") == n else None
    # #        for i, n in enumerate(d_numbers)]
    #
    # if None in deck:
    #     print("Wrong card order definition in Cards")
    #     return None
    # return deck
    return None


def recreate_game(d_hash):
    """
    Recreate the game sequence of the given deck hash.
    The global dict game_hase is used to collect the deck chain.
    The deck hash with no existing key with the same name, is the starting/first deck.

    :param d_hash: a hash of the deck
    :return: list of hashes of decks starting by d_hash and ending by the hash of the start deck.
    """
    game = []
    while d_hash:
        game.append(d_hash)
        d_hash = game_turns.get(d_hash)
    return game[::-1]


def report_game_status(game):
    temp_deck = deck.Deck(game[-1])
    print(len(game_turns), ":",
          game[-1], ":",
          get_status(temp_deck),
          'start deck:', game[0],
          'length of game:', len(game) - 1)


def play_card(deck):
    """
    Activate all icons/action on the top card of the deck.
    Manipulate all the possible cards and collect every possible optional result (new decks).

    :param deck: input deck
    :return: list of decks
    """
    # todo:
    #   To optimize this function, you could consider the following:
    #   Use list comprehension instead of for loops, as it is more efficient
    #   Use built-in python functions like filter() and map() to process the data
    #   Use local variable instead of appending to list and in the end returning it
    #   Remove unnecessary if conditions, as they can slow down the function
    #   Use set or frozenset instead of list to keep track of unique items
    #   Use a more efficient data structure like a numpy array instead of a nested list
    #   Use Cython or Numba to speed up the function if it's still slow after trying the above suggestions.
    switcher = {
        "hit": lambda d, a: hit_deck(d, r=a[1]),  # deck, range,
        "push": lambda d, a: move_deck(d, r=a[1], t=a[2]),  # deck, range, target
        "pull": lambda d, a: move_deck(d, r=-a[1], t=a[2]),  # deck, range, target
        "delay": lambda d, a: adjust_deck(d, p=a[1], t=a[2]),  # deck, by positions, target
        "quicken": lambda d, a: adjust_deck(d, p=-a[1], t=a[2]),  # deck, by positions, target
        "rotate": lambda d, a: rotate_top_card(d),  # deck
        "heal": lambda d, a: revive_deck(d, a[0]),  # deck, action
        "resurrect": lambda d, a: revive_deck(d, a[0]),  # deck, action
        "arrow": lambda d, a: arrow_deck(d, n=a[1]),  # deck, number of targets
        "maneuver": lambda d, a: maneuver_deck(d),  # deck
    }
    decks_new_i = []
    decks_new_i_prev_unchanged_rows = []

    for i, row in enumerate(cards[deck.cards[0][0]][deck.cards[0][1]][1:]):
        decks = [deck]
        decks_new_j = []
        for j, action in enumerate(row):
            if cards[deck.cards[0][0]]['header']["type"] == "hero":
                # for the hero, it is allowed not make some actions,
                # we will drop decks which have not changed at the end of the action row
                decks.extend(decks_new_j[:])
            elif decks_new_j:
                # the monster shall make all the available actions
                decks = decks_new_j[:]
                # else decks have not changed by the previous action and are going to suffer the next action
            decks_new_j = [d
                           for deck_j in decks
                           for d in switcher.get(action[0])(deck_j, action)]

            # if no valid result has been generated, use the input as the outcome
            # todo: check on the following algo
            if not decks_new_j:
                decks_new_j = decks[:]
            # todo: the rotate is mandatory, but not all last actions are mandatory;
            # check, whether outcomes are generated with and without the last action, for hero only
            decks_new_j = get_unique_items(decks_new_j)
        # collect deck_changed bools
        decks_new_j_changed = [deck_changed(d, deck) for d in decks_new_j]
        # decks_new_i = [m for m in decks_new_j if deck_changed(m, deck)]

        # if any deck changed
        if any(decks_new_j_changed):
            if not all(decks_new_j_changed):
                decks_new_j = [deck_new_j for m, deck_new_j in enumerate(decks_new_j) if decks_new_j_changed[m]]
            decks_new_i.extend(decks_new_j)
            decks_new_i = get_unique_items(decks_new_i[:])
            if cards[deck.cards[0][0]]['header']['type'] == 'monster':
                break
        # all the decks stale, no new deck show new configuration
        else:
            decks_new_i_prev_unchanged_rows.extend(decks_new_j)
        # if the last row has been reached
        if not decks_new_i and i == len(cards[deck.cards[0][0]][deck.cards[0][1]][1:]) - 1:
            if decks_new_i_prev_unchanged_rows:
                decks_new_i = get_unique_items(decks_new_i_prev_unchanged_rows[:])
            else:
                # when no row generated a valid results, turn back to the original deck, the input
                # todo: check on the algo
                decks_new_i = [deck]

                # remove duplicates and remove the original deck, if others could be created

        # decks_new_i = [i for i in decks_new_i if deck_changed(i, deck)]
        # if len(decks_new_i) == 0:
        #    decks_new_i.append(deck)

    # sort results by their decreasing her status, and increasing monster status
    decks_new_i.sort(key=lambda d: (get_status(d).get("hero"), -get_status(d).get("monster")), reverse=True)

    return get_unique_items(decks_new_i[:])


card_colours = dict(warrior=Fore.BLUE,
                    ogre=Fore.GREEN,
                    huntress=Fore.LIGHTGREEN_EX,
                    vampire=Fore.LIGHTBLUE_EX,
                    pyromancer=Fore.LIGHTYELLOW_EX,
                    spider=Fore.LIGHTMAGENTA_EX,
                    werewolf=Fore.LIGHTBLACK_EX,
                    demon=Fore.LIGHTCYAN_EX)

card_status_symbols = dict(healthy="◼", wounded="⬓", exhausted="◻")


def colour_card_hash(c):
    # Style.BRIGHT \
    s_out = '' \
            + card_colours[cards[c[0]]['header'].get("name")] \
            + "{:2d}".format(c[0]) \
            + c[1] \
            + card_status_symbols[cards[c[0]][c[1]][0].get("life")] \
            + Style.RESET_ALL \
            + ' '
    return s_out


"""
pyromancer
Condition: Fire Cost
    Pay the cost by rotating X cards with Reaction: Fire Cost to activate the actions pointed by the arrow.
"""

# def fireball:
"""
Game rules applicable:
    Fireball: Choose 1 card that was used to pay the Condition: Fire Cost cost and damage both cards adjacent to it.
    Feature: Webs
        Prevents an enemy card directly in front of this card from performing actions
        that change cards rotation: HIT, ARROW, MANEUVER, HEAL, REVIVE, FIREBALL, ABLAZE.
    
    # the next card displays feature "webs" and prevents from activating the top hero card
    if cards[d.cards[0][0]]['header']["type"] == "hero" \
            and "feature" in cards[d.cards[1][0]][d.cards[1][1]]['header'] \
            and "webs" in cards[d.cards[1][0]][d.cards[1][1]][0].get("feature"):
        return []
"""

# def set_ablaze:
"""
Game rules applicable:
    Set ablaze: Choose 2 different cards that was used to pay the cost and damage all cards in between them.
    Condition: Fire Cost
    Feature: Webs
        Prevents an enemy card directly in front of this card from performing actions
        that change cards rotation: HIT, ARROW, MANEUVER, HEAL, REVIVE, FIREBALL, ABLAZE.
        
    # the next card displays feature "webs" and prevents from activating the top hero card
    if cards[d.cards[0][0]]['header']["type"] == "hero" \
            and "feature" in cards[d.cards[1][0]][d.cards[1][1]]['header'] \
            and "webs" in cards[d.cards[1][0]][d.cards[1][1]][0].get("feature"):
        return []
"""

"""
Reaction: Paying Fire Cost
    Used to pay [fire]. Is always followed by an action
"""

"""
venomous:
Activate icons to the right of the arrow only if there is enough ally cards in the deck.
rewording: ...in the deck -> ...on the top of the deck 
"""


"""
Condition: Spider Swarm
If the top card of the deck is a ally and a continuous group of 1+ Spider Swarm cards is positioned directly behind it
    Activate all SPIDER SWARM rows of cards in that group starting from the most distant one
    Continue towards the top of the deck, before you activate the top card of the deck in a normal manner.
    (Don't activate a SPIDER SWARM row of a top card of the deck).
"""
