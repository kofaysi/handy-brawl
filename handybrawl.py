"""
functions to manipulate the deck according to the Handy Brawl game project
"""


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
    return [c[0], c[3], c[4], c[1], c[2]]


# @CountCalls
def rotate(c):
    """
    rotate the card, top side becomes the bottom and the bottom side becomes the top, sides do not change

    Game rules applicable:
        Rotate: Rotate this card 180° without changing the side. This action is mandatory.

    :param c: a card
    :return: a new card
    """
    return [c[0], c[2], c[1], c[4], c[3]]


# @CountCalls
def rotate_flip(c):
    """
    rotate() and flip() the same card

    :param c: a card
    :return: a new card
    """
    return flip(rotate(c[:]))


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
def check_cards_unique(d) -> "bool":
    """
    check cards in the deck are unique, only numbers are checked for uniqueness, faces are ignored

    :param d: a deck
    :return: bool True if card numbers in the deck are unique
        bool False if card numbers in the deck are not unique
    """
    numbers = set()
    for c in d:
        number = c[0].get("number")
        if number in numbers:
            return False
        numbers.add(number)
    return True


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
def deck_changed(d, d_new):
    """
    check whether two decks are unique or differing, all cards are check except the top card

    :param d_new: a deck of cards
    :param d: a deck of cards
    :return: bool True if decks are differing
    """
    if not check_cards_unique(d):
        pass
    if not check_cards_unique(d_new):
        pass
    return d[1:] != d_new[1:]


# @CountCalls
def delay_deck(d, a, p):
    """
    move_card() any possible card by p (int) positions within the deck

    Game rules applicable:
        Quicken: Move any card up to X spaces towards top of the deck.
        Delay: Move any card up to X spaces towards top of the deck.

    :param d: the current deck
    :param a: action
    :param p: number of position to take the action by
    :return: new decks
    """
    if get_deck_hash(d) == '1A6C2B3A7A9C8B4D5A':
        pass
    if ' ' in a:
        t = a.split()[1]
    else:
        t = "any"
    ds_new = []
    delay_range = list(range(1, abs(p) + 1))
    if p < 0:
        delay_range = [-i for i in delay_range]
    for i in range(1, len(d)):
        for j in delay_range:
            if (
                    (t == "ally" or t == "any") and
                    d[0][0].get("type") == d[i][0].get("type")
            ) or (
                    (t == "enemy" or t == "any") and
                    d[0][0].get("type") != d[i][0].get("type")
            ):
                if p < 0:
                    j = -j
                end_position = i + j
                if len(d) > end_position >= 1:
                    d_new = move_card(d[:], i, end_position)
                    ds_new.append(d_new)
    return ds_new


# @CountCalls
def move_deck(d, a, r):
    """
    move_card() any possible card within the deck

    Game rules applicable:
    (all needs rewording)
    hero:
        Pull: Move the furthest card in range X behind the active card.
        Push: Move the closest enemy card in range X to the bottom of the deck. (needs rewording)
    monster:
        Pull: Move the furthest card in range X behind the active card. Don't target enemy cards. (needs rewording)
        Push: Move the closest enemy card in range to the bottom of the deck.

    :param d:
    :param a:
    :param r:
    :return:
    """
    if not check_cards_unique(d):
        pass
    if get_deck_hash(d) == '7D3A8A4B9A5B1A6C2B':
        pass
    ds_new = []
    if ' ' in a:
        t = a.split()[1]
    else:
        t = "any"
    move_range = range(1, min(abs(r) + 1, len(d)))
    if r < 0:
        move_range = reversed(move_range)
    for i in move_range:
        if (
                (t == "ally" or t == "any") and
                d[0][0].get("type") == d[i][0].get("type")
        ) or (
                    (
                            (t == "enemy" or t == "any") and
                            d[0][0].get("type") != d[i][0].get("type") and
                            # Heavy card cannot be moved by any enemy action.
                            d[i][1][0].get("feature") != "heavy"
                    ) and
                    # do not pull exhausted enemies
                    not (r < 0 and
                         d[i][1][0].get("life") != "exhausted")
        ):
            end_position = 1 if r < 1 else len(d) - 1
            ds_new.append(move_card(d[:], i, end_position))
            if d[0][0].get("type") == "monster":
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
    if not check_cards_unique(d):
        pass
    if i < j:
        d[i:j + 1] = back_shift(d[i:j + 1])
    else:
        d[j:i + 1] = back_shift(d[j:i + 1], len(d[j:i + 1]) - 1)
    return d


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
    if not check_cards_unique(d):
        pass
    d_new = d[:]
    d_new[i] = rotate(d[i])
    ds_new = [d_new]
    return ds_new


# @CountCalls
def hit_deck(d, n):
    """
    hit_card() every possible card in the deck d within range n

    Game rules applicable:
        Hit:
        Reaction: Shield: Don't target

    :param d: the current deck
    :param n: the hit range, int
    :return: the new decks
    """
    if not check_cards_unique(d):
        pass
    # shield_found = False
    ds_new = []
    if n == 0 or n > len(d) - 1:  # 0 is a substitute for the infinite hit range
        n = len(d) - 1
    for i in reversed(range(1, n + 1)):
        # Reaction: Shield: Don't target
        if d[0][0].get("type") != d[i][0].get("type") and d[i][1][0].get("reaction") == "shield":
            # shield_found = True
            d_new = use_shield(d[:], i)
            if not check_cards_unique(d_new):
                pass
            ds_new.append(d_new)
            if d[0][0].get("type") == "monster":
                break
    # if not shield_found:  # Using shield is not mandatory
    for i in range(1, n + 1):
        if d[0][0].get("type") != d[i][0].get("type") and d[i][1][0].get("life") != "exhausted":
            d_new = hit_card(d[:], i)
            if not check_cards_unique(d_new):
                pass
            ds_new.append(d_new)
            if d[0][0].get("type") == "monster":
                break
    return ds_new


# @CountCalls
def use_shield(d, i):
    """
    rotate() the i-th card in the deck as a result of the shield property/reaction of the card

    Game rules applicable:
    hero:
        Reaction Shield:
        If in range of you MAY intercept and negate the damage. If you do so, activate all icons after the arrow.
    monster:
        Reaction: Block (reword or use a different icon)
        If in range of targeting an ally card, intercept and negate the damage.
        If you do so, activate all icons after the arrow.
        If multiple BLOCKS available, use the furthest.

    :param d: the current deck
    :param i: the i-th card
    :return: the new deck
    """
    if not check_cards_unique(d):
        pass
    d_new = d[:]

    switcher = {
        "rotate": lambda c: rotate(c[:])
    }

    action = d[i][1][0].get("shield")
    if action:
        # todo possible replacement not to use lambda: d_new[i] = rotate(d[i])
        d_new[i] = switcher.get(action)(d[i][:])
        if not check_cards_unique(d_new):
            pass
    return d_new


# @CountCalls
def hit_card(d, i):
    """
    Change the life status to the i-th card in the deck

    Game rules applicable:
    hero:
        Hit: Damage any non-[empty heart] (unexhausted) card in range X
    monster:
        Hit: Damage closest non-[empty heart] (unexhausted) enemy card in range X.

    :param d: the current deck
    :param i: the i-the card in the deck [0, 1...]
    :return: new deck (single)
    """
    expected_face = ''
    if not check_cards_unique(d):
        pass
    if d[i][1][0].get("life") == "healthy":
        expected_life = "wounded"
    else:
        expected_life = "exhausted"
    for j in range(1, 5):
        if d[i][j][0].get("life") == expected_life:
            expected_face = d[i][j][0].get("face")
            break
    expected_card = rotate_card_to_face(d[i][:], expected_face)
    d_new = d[:]
    d_new[i] = expected_card
    return d_new  # if d != d_new else []
# noinspection PyShadowingNames


# @CountCalls
def heal_deck(d):
    """
    heal_card() every possible card in the current deck

    Game rules applicable:
        Heal: Return any [half leaf] (wounded) to its starting position.

    :param d: the current deck
    :return: new decks
    """
    if not check_cards_unique(d):
        pass
    ds_new = []
    for i in range(1, len(d)):
        if d[0][0].get("type") == d[i][0].get("type") and d[i][1][0].get("life") == "wounded":
            d_new = d[:]
            d_new[i] = heal_card(d[i])
            ds_new.append(d_new)
            if not check_cards_unique(d_new):
                pass
            if d[0][0].get("type") == "monster":
                break
    return ds_new


def heal_card(c):
    """
    Turn the card to its starting ("A") position.

    Game rules applicable:
        Heal: Return any [half leaf] (wounded) to its starting position.

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


# @CountCalls
def get_status(d):
    """
    Check on the health status of the hero(s) and  monster(s).
    Calculate a simple numerical health score.

    :param d: the deck
    :return: the health status (tuple(bool, float))
    """
    status = dict(hero=0.0, monster=0.0)
    score = dict(healthy=1, wounded=0.5, exhausted=0)
    deck = d[:]
    for card in deck:
        card_score = score.get(card[1][0].get("life"))
        if card[0].get("type") == "hero":
            temp_score = status.get("hero") + card_score
            status.update(hero=temp_score)
        else:
            temp_score = status.get("monster") + card_score
            status.update(monster=temp_score)
    return status


# noinspection PyShadowingNames
# @CountCalls
def maneuver_deck(d):
    """
    rotate() every possible ally card in the deck, without increasing its health level

    Game rules applicable:
        Maneuver: Rotate other ally card in a way that its health level doesn't increase.

    :param d: the current deck
    :return: list of new decks
    """
    ds_new = []
    for i in range(1, len(d) + 1):
        if (d[0][0].get("type") == d[i][0].get("type") and
                (d[i][1][0].get("life") == d[i][2][0].get("life") or
                 (d[i][1][0].get("life") == "healthy" and d[i][2][0].get("life") == "wounded") or
                 (d[i][1][0].get("life") == "healthy" and d[i][2][0].get("life") == "exhausted") or
                 (d[i][1][0].get("life") == "wounded" and d[i][2][0].get("life") == "exhausted"))):
            d_new = d[:]
            d_new[i] = rotate(d[i])
            ds_new.append(d_new)
    return ds_new


# @CountCalls
def arrow_deck(d, t=1, end=3):
    """
    hit_card() every possible card in the deck.

    Game rules applicable:
        Arrow: Deal damage to any one of the 3 (and) bottom cards.
        Double arrow: Two arrow actions that cannot target the same card (you may still skip one of them).
            (rewording) Two arrow actions that shall target different cards (targeting only one card is allowed).

    :param d: the current deck
    :param t: the number of targets, different cards targets are targeted
    :param end: number (int) of the cards att the end of the deck to be targeted possibly
    :return: new decks
    """
    ds_new = []
    m = len(d)
    d_new = []
    # TODO: check out the requirement or conditions for the shield, when hitting a card with an arrow
    for i in range(m - end - 1, m + 1):
        if d[0][0].get("type") != d[i][0].get("type"):  # and d[i][0].get("reaction") != "shield":
            d_new = hit_card(d, i)
            if t == 2:
                for j in range(m - end - 1, m + 1):
                    if j != i and d[0][0].get("type") != d[i][0].get("type"):
                        # and d[i][0].get("reaction") != "shield":
                        d_new = hit_card(d_new, i)
        ds_new.append(d_new)
    return ds_new


# @CountCalls
def get_deck_hash(d):
    """
    Create a unique string identifying the deck.
    The string consists of numbers and faces in the order of the cards appearing in the deck.

    :param d: the deck
    :return: the hash (str)
    """
    d_id = [str(card[0].get("number")) + card[1][0].get("face") for card in d]
    return ''.join(d_id)


# @CountCalls
def create_deck(d_hash, cards):
    """
    create a deck consisting of cards based on the hash

    :param d_hash: the unique hash (str)
    :param cards: the definition of all the available cards (list)
    :return: a deck, a list of cards, (list of lists)
    """
    # todo use unzip_hash() instead of re.
    # d_numbers = re.sub(r"[a-zA-Z]+", ' ', d_hash).strip().split(' ')
    # d_numbers = [int(i) for i in d_numbers]
    # d_faces = re.sub(r"\d+", ' ', d_hash).strip().split(' ')

    d_numbers, d_faces = unzip_hash(d_hash)
    deck = [[]]*len(d_faces)
    for i, number in enumerate(d_numbers):
        if cards[number - 1][0].get("number") == number:
            c_new = rotate_card_to_face(cards[number - 1][:], d_faces[i].upper())
            deck[i] = c_new
        else:
            print("Wrong card order definition in Cards")
            print(f"The card listed as {str(number)} displays number={cards[number - 1][0].get('number')}")
            for card in cards:
                if card[0].get("number") == number:
                    c_new = rotate_card_to_face(card[:], d_faces[i].upper())
                    deck[i] = c_new
            else:
                print(f"The card number {str(number)} couldn't be found in the card list.")
                return None
    return deck


"""
pyromancer
Condition: Fire Cost
Pay the cost by rotating X cards with Reaction: Fire Cost to activate the actions pointed by the arrow.
"""

# def fireball:
"""
Game rules applicable:
    Fireball: Choose 1 card that was used to pay the Condition: Fire Cost cost and damage both cards adjacent to it.
"""

# def set_ablaze:
"""
Game rules applicable:
    Set ablaze: Choose 2 different cards that was used to pay the cost and damage all cards in between them.
    Condition: Fire Cost
"""

"""
Reaction: Paying Fire Cost Used to pay
Is always followed by an action:
"""

"""
venomous:
Activate icons to the right of the arrow only if there is enough ally cards in the deck.
rewording: ...in the deck -> ...on the top of the deck 
"""


# def inspire(d):
"""
Game rules applicable:
    Inspire: Activate other closest ally card from the middle of the deck.
        Treat all the cards above it as if they didn't exist.
"""


# def revive(d):
"""
Game rules applicable:
    Revive: Return closest ally card to its starting position.
"""

"""
Condition: Spider Swarm
If the top card of the deck is a ally and a continuous group of 1+ Spider Swarm cards is positioned directly behind it
    Activate all SPIDER SWARM rows of cards in that group starting from the most distant one
    Continue towards the top of the deck, before you activate the top card of the deck in a normal manner.
    (Don't activate a SPIDER SWARM row of a top card of the deck).

Feature: Venom
Prevents an enemy card directly in front of this card from performing actions that change cards position:
    DELAY, QUICKEN, TELEPORT. Feature: Webs
Feature: Sticky web: (missing name) Prevents an enemy card directly in front of this card from performing actions
    that change cards rotation: HIT, ARROW, MANEUVER, HEAL, REVIVE, FIREBALL, ABLAZE.
"""

"""
Reaction: Block
    If in range of targeting an ally card, intercept and negate the damage. 
    If you do so, activate all icons after the arrow. 
    If multiple BLOCKS available, use the furthest.
"""

# def teleport(d):
"""
    Swap any places of two cards (of corresponding sides), apply for every combination
    
    Game rules applicable:
        Teleport: Swap places of 2 cards (of corresponding sides)
"""

"""
Feature: Trap Master
If an enemy card moves over a card with this feature, deal damage to it.
"""

"""
Reaction: Dodge
If targeted by an enemy action, you MAY negate it. If you do so, activate all actions after the arrow.
"""
