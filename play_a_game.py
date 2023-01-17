import cards
import handybrawl as hb
from colorama import Fore, Style  # , Back


def recreate_game(d_hash):
    global game_bits
    game = []
    d_i_hash = d_hash[:]
    key_found = True
    game.append(d_i_hash)
    while key_found:
        d_prev_hash = game_bits.get(d_i_hash)
        if d_prev_hash:
            game.append(d_prev_hash)
            d_i_hash = d_prev_hash[:-2] + d_prev_hash[-2:]
        else:
            key_found = False
    return game


def colour_card(c):
    s_out = Style.BRIGHT \
            + card_colours[c[0].get("name")] \
            + "{:2d}".format(c[0].get("number")) \
            + c[1][0].get("face") \
            + card_status[c[1][0].get("life")] \
            + Style.RESET_ALL \
            + ' '
    return s_out


# deck_start_hash = '1A6A2A7A3A8A4A9A5A'
# deck_start_hash = '6A7A8A9A1A2A3A4A5A'
# deck_start_hash = '1A2A3A4A5A6A7A8A9A'
# deck_start_hash = '1A2A3A5A4A6A9A7A8A'
deck_start_hash = '1A2A3A4A6A9A8A5A7A'
# deck_start_hash = '1A2B3C4D6A9A8B5C7D'
# deck_start_hash = '1A2A10A15A6A17A8A20A24A'
# deck_start_hash = '1C6C2D7A8A3C5D4D9C'
# deck_start_hash = '1A6A2A8A3A'
# deck_start_hash = '9b2b6d5c'

deck_start = hb.create_deck(deck_start_hash, cards.cards)

card_colours = dict(warrior=Fore.RED, ogre=Fore.GREEN, ranger=Fore.LIGHTGREEN_EX, vampire=Fore.MAGENTA, pyromancer=Fore.LIGHTYELLOW_EX, venomous=Fore.LIGHTMAGENTA_EX)
card_status = dict(healthy="◼", wounded="⬓", exhausted="◻")

game_bits = dict()

deck = deck_start[:]
decks_new = [deck]
#decks_new = hb.play_card(deck)
print("Welcome to the new game with the following deck:")

while True:
    # sort results by their decreasing her status, and increasing monster status
    decks_new.sort(key=lambda dx: (hb.get_status(dx).get("hero"), -hb.get_status(dx).get("monster")), reverse=True)

    # global card_colours, card_status
    for k, d in enumerate(decks_new):
        s = ''
        for c in d:
            s += colour_card(c)
        print("{:3d}".format(k+1), ":", s)
    if len(decks_new) != 1:
        option_number = input('Choose card variant to play: ')
    else:
        option_number = 1
        print("No option to choose. Proceeding automatically to a new deck...")
    deck_i = decks_new[int(option_number)-1]

    # print('Your choice:',  option_number)
    print('The new deck to play is:')

    # global game_bits
    deck_i_new = hb.back_shift(deck_i[:])
    s = ''
    for c in deck_i_new:
        s += colour_card(c)
    print('      ' + s)

    if hb.get_deck_hash(deck_i_new) == '6A3A9A8A5A7A1A2A4A':
        pass

    deck_i_new_hash = hb.get_deck_hash(deck_i_new)
    status = hb.get_status(deck_i)
    print(status)
    if deck_i_new_hash not in game_bits and deck_i_new_hash != hb.get_deck_hash(deck_start):
        game_bits[deck_i_new_hash] = hb.get_deck_hash(deck)
        game_deck_i_new = recreate_game(deck_i_new_hash)
        if status.get("hero") == 0 or status.get("monster") == 0:
            if status.get("monster") == 0:
                print("game end", ":", len(game_bits), ":",
                      deck_i_new_hash, ":",
                      status,
                      'start deck:', game_deck_i_new[-1],
                      'length of game:', len(game_deck_i_new) - 1)
        elif status.get("hero") != 0 \
                and status.get("monster") != 0:
            # no win or defeat, and deck changed
            try:
                decks_new = hb.play_card(deck_i_new[:])
                deck = deck_i
            except RecursionError:
                print(deck_i_new_hash, ":", status, "recursion overflow")
