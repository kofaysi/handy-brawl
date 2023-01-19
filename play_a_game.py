import cards
import handybrawl as hb


# deck_start_hash = '1A6A2A7A3A8A4A9A5A'
# deck_start_hash = '6A7A8A9A1A2A3A4A5A'
# deck_start_hash = '1A2A3A4A5A6A7A8A9A'
# deck_start_hash = '1A2A3A5A4A6A9A7A8A'
# deck_start_hash = '1A2A3A4A6A9A8A5A7A'
deck_start_hash = '1A6A2A7A3A8A4A9A5A'
# deck_start_hash = '1A2B3C4D6A9A8B5C7D'
# deck_start_hash = '1A2A10A15A6A17A8A20A24A'
# deck_start_hash = '1C6C2D7A8A3C5D4D9C'
# deck_start_hash = '1A6A2A8A3A'
# deck_start_hash = '9b2b6d5c'

deck_start = hb.create_deck(deck_start_hash, cards.cards)

deck = deck_start[:]
decks_new = [deck]
print("Welcome to the new game with the following deck:")


def request_number(minimum=1, maximum=1):
    """
    A routine to obtain a choice among the served options/deck variants.

    :param minimum: the minimum for the input (int)
    :param maximum: the maximum for the input (int)
    :return: int
    """
    number = None
    while True:
        try:
            number = int(input('Choose card variant to play: '))
        except ValueError:
            print("An integer number has been expected, please.")
            # better try again... Return to the start of the loop
            continue

        if minimum <= number <= maximum:
            # options was successfully selected!
            # we're ready to exit the loop.
            break
        else:
            print("The supplied number is not in the range of the suggested options.")
            continue
    return number


while True:
    # sort results by their decreasing her status, and increasing monster status
    decks_new.sort(key=lambda dx: (hb.get_status(dx).get("hero"), -hb.get_status(dx).get("monster")), reverse=True)

    # global card_colours, card_status
    for k, d in enumerate(decks_new):
        s = ''
        for c in d:
            s += hb.colour_card_hash(c)
        print("{:3d}".format(k+1), ":", s)

    if len(decks_new) != 1:
        option_number = request_number(maximum=len(decks_new))
    else:
        option_number = 1
        print("A single outcome evaluated. Proceeding automatically to a new deck...")
    deck_i = decks_new[option_number-1]

    # print('Your choice:',  option_number)
    print('The new deck to play is:')

    deck_i_new = hb.back_shift(deck_i[:])
    s = ''
    for c in deck_i_new:
        s += hb.colour_card_hash(c)
    print(' '*6 + s)

    if hb.get_deck_hash(deck_i_new) == '6A3A9A8A5A7A1A2A4A':
        pass

    deck_i_new_hash = hb.get_deck_hash(deck_i_new)
    status = hb.get_status(deck_i)
    print(status)
    if deck_i_new_hash not in hb.game_bits and deck_i_new_hash != hb.get_deck_hash(deck_start):
        hb.game_bits[deck_i_new_hash] = hb.get_deck_hash(deck)
        if status.get("hero") == 0 or status.get("monster") == 0:
            game_deck_i_new = hb.recreate_game(deck_i_new_hash)
            print("game end", ":", len(hb.game_bits), ":",
                  deck_i_new_hash, ":",
                  status,
                  'start deck:', game_deck_i_new[-1],
                  'length of game:', len(game_deck_i_new) - 1, "turns")
            break
        elif status.get("hero") != 0 \
                and status.get("monster") != 0:
            # no win or defeat, and deck changed
            try:
                decks_new = hb.play_card(deck_i_new[:])
                deck = deck_i_new[:]
            except RecursionError:
                print(deck_i_new_hash, ":", status, "recursion overflow")
