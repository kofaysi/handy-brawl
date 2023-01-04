"""
functions to manipulate the deck according to the Handy Brawl game project
"""


import re


class CountCalls:
    def __init__(self, func):
        self._count = 0
        self._func = func

    def __call__(self, *args, **kwargs):
        self._count += 1
        return self._func(*args, **kwargs)

    @property
    def call_count(self):
        return self._count


@CountCalls
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


@CountCalls
def flip(c):
    return [c[0], c[3], c[4], c[1], c[2]]


@CountCalls
def rotate(c):
    return [c[0], c[2], c[1], c[4], c[3]]


@CountCalls
def rotate_flip(c):
    return flip(rotate(c))


@CountCalls
def back_shift(tup, n=1):  # by default, the top card goes to the bottom of the deck
    try:
        n = n % len(tup)
    except ZeroDivisionError:
        return tuple()
    return tup[n:] + tup[0:n]


@CountCalls
def check_cards_unique(d):
    d_hash = get_deck_hash(d)
    d_numbers = re.sub(r"[a-zA-Z]+", ' ', d_hash).strip().split(' ')
    return len(set(d_numbers)) == len(d)


@CountCalls
def deck_changed(d, d_new):
    if not check_cards_unique(d):
        pass
    if not check_cards_unique(d_new):
        pass
    return d[1:] != d_new[1:]


@CountCalls
def delay_deck(d, a, p):
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
                    (t == "self" or t == "any") and
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


@CountCalls
def move_deck(d, a, r):
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
                (t == "self" or t == "any") and
                d[0][0].get("type") == d[i][0].get("type")
        ) or (
                (
                        (
                                (t == "enemy" or t == "any") and
                                d[0][0].get("type") != d[i][0].get("type") and
                                d[i][1][0].get("feature") != "heavy"
                        ) and
                        r < 0 and
                        d[i][1][0].get("life") != "exhausted"
                )
        ):
            end_position = 1 if r < 1 else len(d) - 1
            ds_new.append(move_card(d[:], i, end_position))
            if d[0][0].get("type") == "monster":
                break
    return ds_new if ds_new != d else []


@CountCalls
def move_card(d, i, j):
    if not check_cards_unique(d):
        pass
    if i < j:
        d[i:j + 1] = back_shift(d[i:j + 1])
    else:
        d[j:i + 1] = back_shift(d[j:i + 1], len(d[j:i + 1]) - 1)
    return d


@CountCalls
def rotate_top_card(d):
    if not check_cards_unique(d):
        pass
    d_new = d[:]
    d_new[0] = rotate(d[0])
    ds_new = [d_new]
    return ds_new


@CountCalls
def hit_deck(d, n):
    if not check_cards_unique(d):
        pass
    # shield_found = False
    ds_new = []
    if n == 0 or n > len(d) - 1:  # 0 is a substitute for the infinite hit range
        n = len(d) - 1
    for i in reversed(range(1, n + 1)):
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


@CountCalls
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


@CountCalls
def hit_card(d, i):
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


@CountCalls
def heal_deck(d):
    if not check_cards_unique(d):
        pass
    ds_new = []
    for i in range(1, len(d)):
        if d[0][0].get("type") == d[i][0].get("type") and d[i][1][0].get("life") == "wounded":
            d_new = d[:]
            d_new[i] = rotate_card_to_face(d[i], 'A')
            ds_new.append(d_new)
            if not check_cards_unique(d_new):
                pass
            if d[0][0].get("type") == "monster":
                break
    return ds_new


@CountCalls
def get_unique_items(items):
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique


@CountCalls
def get_status(d, cards):
    status = dict(hero=0.0, monster=0.0)
    score = dict(healthy=1, wounded=0.5, exhausted=0)
    if isinstance(d, str):
        deck = create_deck(d[:], cards)
    else:
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


@CountCalls
def maneuver_deck(d):
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


@CountCalls
def arrow_deck(d, a):
    try:
        t = a.split()[1]
    except IndexError:
        t = "single"
    ds_new = []
    m = len(d)
    d_new = []
    for i in range(m - 2, m + 1):
        if d[0][0].get("type") != d[i][0].get("type"):  # and d[i][0].get("reaction") != "shield":
            d_new = hit_card(d, i)
            if t == "double":
                for j in range(m - 2, m + 1):
                    if j != i and d[0][0].get("type") != d[i][0].get("type"):  # and d[i][0].get("reaction") != "shield":
                        d_new = hit_card(d_new, i)
        ds_new.append(d_new)
    return ds_new


@CountCalls
def get_deck_hash(d):
    d_id = []
    for card in d:
        d_id.append(str(card[0].get("number")) + card[1][0].get("face"))
    return ''.join(d_id)


@CountCalls
def create_deck(d_hash, cards):
    d_numbers = re.sub(r"[a-zA-Z]+", ' ', d_hash).strip().split(' ')
    d_numbers = [int(i) for i in d_numbers]
    d_faces = re.sub(r"\d+", ' ', d_hash).strip().split(' ')
    deck = [[]]*len(d_faces)
    for card in cards:
        try:
            i = d_numbers.index(card[0].get("number"))
            c_new = rotate_card_to_face(card[:], d_faces[i].upper())
            deck[i] = c_new
        except ValueError:
            pass
    return deck
