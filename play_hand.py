import all_cards


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


def check_cards_unique(d):
    for i1, c1 in enumerate(d):
        for i2, c2 in enumerate(d):
            if i1 != i2:
                if c1[0].get("number") == c2[0].get("number"):
                    return False
    return True


def deck_changed(d, d_new):
    if not check_cards_unique(d):
        pass
    if not check_cards_unique(d_new):
        pass
    return d[1:] != d_new[1:]


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


def move_card(d, i, j):
    if not check_cards_unique(d):
        pass
    # TODO check the code
    if i < j:
        d[i:j + 1] = leftShift(d[i:j + 1])
    else:
        d[j:i + 1] = leftShift(d[j:i + 1], len(d[j:i + 1]) - 1)
    return d


def rotate_top_card(d):
    if not check_cards_unique(d):
        pass
    d_new = d[:]
    d_new[0] = rotate(d[0])
    ds_new = [d_new]
    return ds_new


def hit_deck(d, n):
    if not check_cards_unique(d):
        pass
    shield_found = False
    ds_new = []
    if n == 0 or n > len(d) - 1:  # 0 is a substitute for the infinite hit range
        n = len(d) - 1
    for i in reversed(range(1, n + 1)):
        if d[0][0].get("type") != d[i][0].get("type") and d[i][1][0].get("reaction") == "shield":
            shield_found = True
            d_new = use_shield(d[:], i)
            if not check_cards_unique(d_new):
                pass
            ds_new.append(d_new)
            if d[0][0].get("type") == "monster":
                break
    if not shield_found:
        for i in range(1, n + 1):
            if d[0][0].get("type") != d[i][0].get("type") and d[i][1][0].get("life") != "exhausted":
                d_new = hit_card(d[:], i)
                if not check_cards_unique(d_new):
                    pass
                ds_new.append(d_new)
                if d[0][0].get("type") == "monster":
                    break
    return ds_new


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


def get_unique_items(items):
    unique = []
    for item in items:
        if item not in unique:
            unique.append(item)
    return unique


def get_status(d):
    status = dict(hero=0.0, monster=0.0)
    score = dict(healthy=1, wounded=0.5, exhausted=0)
    if isinstance(d, str):
        deck = create_deck(d[:])
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


def arrow_deck(d, a):
    try:
        t = a.split()[1]
    except IndexError:
        t = "single"
    ds_new = []
    m = len(d)
    d_new = []
    for i in range(m - 2, m + 1):
        if d[0][0].get("type") != d[i][0].get("type") and d[i][0].get("reaction") != "shield":
            d_new = hit_card(d, i)
            if t == "double":
                for j in range(m - 2, m + 1):
                    if j != i and d[0][0].get("type") != d[i][0].get("type") and d[i][0].get("reaction") != "shield":
                        # TODO check, if enemy shield on earlier position can protect also
                        d_new = hit_card(d_new, i)
        ds_new.append(d_new)
    return ds_new


def get_deck_hash(d):
    d_id = []
    for card in d:
        d_id.append(str(card[0].get("number")) + card[1][0].get("face"))
    return ''.join(d_id)


def create_deck(d_hash):
    deck = []
    d_items = [d_hash[i:i + 2] for i in range(0, len(d_hash), 2)]
    for number_face in d_items:
        for card in all_cards.cards:
            number = int(number_face[:-1])
            face = number_face[-1]
            if card[0].get("number") == number:
                c_new = rotate_card_to_face(card[:], face)
                deck.append(c_new)
    return deck


def recreate_game(d_hash):
    game_hash = []
    d_i_hash = d_hash[:]
    key_found = True
    game_hash.append(d_i_hash)
    while key_found:
        d_prev_hash = global_decks_list.get(d_i_hash)
        if d_prev_hash:
            game_hash.append(d_prev_hash)
            d_i_hash = d_prev_hash[:-2] + d_prev_hash[-2:]
        else:
            key_found = False
    return game_hash


def play_card(deck):
    switcher = {
        "hit": lambda d, a, n: hit_deck(d, n),
        "arrow": lambda d, a, n: arrow_deck(d, a),
        "push": lambda d, a, r: move_deck(d, a, r),
        "pull": lambda d, a, r: move_deck(d, a, -r),
        "delay": lambda d, a, p: delay_deck(d, a, p),
        "quicken": lambda d, a, p: delay_deck(d, a, -p),
        "rotate": lambda d, a, n: rotate_top_card(d),
        "heal": lambda d, a, n: heal_deck(d),
        "maneuver": lambda d, a, n: maneuver_deck(d),
    }
    decks_new_i = []
    decks_new_j_prev_unchanged_rows = []
    for i, row in enumerate(deck[0][1][1:]):
        # TODO monsters shall not run next row unless no results achieved in the first run
        decks = [deck[:]]
        decks_new_j = []
        for j, action in enumerate(row):
            if j > 0 and decks_new_j:
                decks = decks_new_j[:]
                decks_new_j = []
            for deck_j in decks:
                # deck_j_sign = get_deck_hash(deck_j)
                if not check_cards_unique(deck_j):
                    pass
                action_raw = action[0]
                deck_j_hash = get_deck_hash(deck_j)
                if deck_j_hash == '6A8A2A1B':
                    pass
                decks_new_j = switcher.get(action_raw.split()[0])(deck_j[:], action_raw, action[1])
                duplicates = [deck for deck in decks_new_j if decks_new_j.count(deck) > 1]
                if len(duplicates):
                    pass
                # for deck_new_j in decks_new_j:
                #    deck_new_j[0].update("history") += int(''.join(deck_j_sign), 16)
                # TODO allow None (no deck, the action had no effect, could not be validly executed) switcher output and
                # deal with it accordingly
                for deck_new_j in decks_new_j:
                    if get_deck_hash(deck_new_j) == '9C2C3C4D6A7D8A5D1C':
                        pass
                    if not check_cards_unique(deck_new_j):
                        pass
            decks_new_j = get_unique_items(decks_new_j[:])
            # decks_new_j = [i for i in decks_new_j if deck_changed(i, deck) or j == len(row)]
        #            if len(decks_new_j) == 0:
        #                decks_new_j.append(deck)

        decks_new_j_changed = [deck_changed(i, deck) for i in decks_new_j]
        if True in decks_new_j_changed:
            decks_new_j = [deck_new_j for i, deck_new_j in enumerate(decks_new_j) if decks_new_j_changed[i]]
            decks_new_i.extend(decks_new_j)
            decks_new_i = get_unique_items(decks_new_i[:])
            if deck[0][0].get('type') == 'monster':
                break
        else:
            decks_new_j_prev_unchanged_rows.extend(decks_new_j)
            if i == len(deck[0][1][1:]) - 1:
                if deck[0][0].get('type') == 'monster' or not decks_new_i:
                    decks_new_i = get_unique_items(decks_new_j_prev_unchanged_rows[:])

        # remove duplicates and remove the original deck, if others could be created

        # decks_new_i = [i for i in decks_new_i if deck_changed(i, deck)]
        # if len(decks_new_i) == 0:
        #    decks_new_i.append(deck)

    decks_new = get_unique_items(decks_new_i[:])

    for deck_i in decks_new:
        status_i = get_status(deck_i)

    if get_deck_hash(deck) == '3B1A6B2A8B':
        pass

    if decks_new:
        for deck_i in decks_new:
            deck_i_new = leftShift(deck_i[:])
            deck_i_new_hash = get_deck_hash(deck_i_new)
            status = get_status(deck_i)
            if deck_i_new_hash not in global_decks_list and deck_i_new_hash != get_deck_hash(deck_start):
                global_decks_list[deck_i_new_hash] = get_deck_hash(deck)
                if status.get("hero") != 0 and status.get("monster") != 0:
                    # no win or defeat, and deck changed, or it is the last action row iteration anyway
                    try:
                        play_card(deck_i_new[:])
                    except RecursionError as re:
                        print(deck_i_new_hash, ":", status, "recursion overflow")
                elif status.get("hero") == 0 or status.get("monster") == 0:
                    game_deck_i_new = recreate_game(deck_i_new_hash)
                    print(len(global_decks_list), ":",
                          deck_i_new_hash, ":",
                          status,
                          'start deck:', game_deck_i_new[-1],
                          'length of game:', len(game_deck_i_new) - 1)
                    if status.get("monster") == 0:
                        pass
    else:
        pass


# deck_hash = '1A6A2A7A3A8A4A9A5A'
deck_start_hash = '1A6A2A8A3A'
deck_start = create_deck(deck_start_hash)

global_decks_list = dict()

play_card(deck_start)
