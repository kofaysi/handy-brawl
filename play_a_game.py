"""
An application running a Handy Brawl game in terminal according to the Handy Brawl game rules.
There are no means to manipulate the virtual deck of cards such as in the PCIO representation of the game.

The deck is visualised as a list of strings (cards) from right (top card) to left (bottom card).

The application may be a subject to rapid changes in the following weeks.
todo:
    - add missing characters
    - add missing actions and conditions
"""
import copy

# from cards import cards
import handybrawl as hb
import re
import deck


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
            number = int(input('Choose deck variant to play: '))
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


def request_deck():
    game_description = "This application is simulating the Handy Brawl game designed by Igor Zuber.\n" \
                       "A card overview is required to play the game properly.\n" \
                       "The cards design and available actions on faces are not displayed.\n" \
                       "Download the cards and the rules from the files section at " \
                       "https://boardgamegeek.com/boardgame/362692/handy-brawl." \

    app_description = "This application is a hobby type of project by Milan Žroutík <zroutik@e.email>."

    instructions = "The hash for a deck is a string consisting of alternating integers and characters [A, B, C, D].\n" \
                   "The physical cards in the physical deck are played from top to bottom. " \
                   "The virtual deck with cards (and their faces) are displayed from right to left.\n" \
                   "Card numbers are represented by integers and the faces of the cards by letters.\n" \
                   "Lower case letters are allowed. Spaces are allowed.\n" \
                   "Missing letters represent the face 'A' of the card.\n" \
                   "    (Spaces between numbers are required in such case.)\n" \
                   "Use card numbers for the warrior and the ogre characters, in the range from 1 to 9.\n" \
                   "The visualisation od the deck (5A◼  9A◼  4A◼  8A◼  3A◼  7A◼  2A◼  6A◼  1A◼)\n " \
                   "and the hash to the deck (1A6A2A7A3A8A4A9A5A) have reversed order of the cards.\n " \
                   "Some examples of a valid hash (top card of the deck first, bottom card of the deck last):\n" \
                   "    - 1A6A2A7A3A8A4A9A5A\n" \
                   "    - 1A 6A 2A 7A 3A 8A 4A 9A 5A\n" \
                   "    - 1 6 2 7 3 8 4 9 5"

    def corrections(s_hash: str) -> str:
        # make the hash uppercase
        s_hash = s_hash.strip().upper()
        # remove other then [A, B, C, D] chars
        s_hash = re.sub(r'[E-Z]', '', s_hash)
        # replace spaces between numbers and following chars
        s_hash = re.sub(r'(\d)\s+(?=[ABCD])', r'\1', s_hash)
        # replace spaces between numbers without chars by char 'A'
        s_hash = re.sub(r'(\d)\s+(?=\d)', r'\1A', s_hash)
        # add face A to the number without chars by char 'A' and at the end of the string
        s_hash = re.sub(r'(\d)$', r'\1A', s_hash)
        # remove spaces
        s_hash = re.sub(r'([ABCD])\s*(?=\d)', r'\1', s_hash)
        return s_hash

    print(app_description)
    print()
    print(game_description)
    print()
    print(instructions)
    print()

    while True:
        try:
            input_hash = str(input('Enter a hash for the deck to play '
                                   '(start entering the top card first, proceed the list from left to right): '))
        except ValueError:
            print("The input has been captured.")
            # better try again... Return to the start of the loop
            continue

        input_hash_cor = corrections(input_hash)

        try:
            start = deck.Deck(input_hash_cor)
            # hb.get_deck_hash(hb.create_deck(input_hash_cor, cards))
            #
            print("The accepted hash: ", input_hash_cor)
            numbers = [card[0] for card in start.cards]
            if not all([1 <= i <= 9 for i in numbers]):
                print("Use card numbers for the warrior and the ogre characters, in the range from 1 to 9. "
                      "Other characters are coming soon.")
                continue
            print("If the hash has been parsed incorrectly, start the application over.")
            break
        except ValueError:
            print("The supplied input is not following the the suggested structure.")
            print("The hash cannot be converted to its deck representation.")
            print(instructions)
            continue
        except IndexError:
            print("No corresponding card numbers could be found.")
            continue

    return start


if 'deck_start_hash' not in locals():
    deck_start_hash = ''

answer = input("Do you wish to start a game with your own deck? ([Y]es/No) "
               "(In case of 'no', you will be served by the deck saved within the script): ")

# or not deck_start_hash
if answer.lower() in {'yes', 'y', 'yeah', 'ano', 'igen'}:
    start = request_deck()

decks_new = None


def build_graphical_representation_to_deck(deck):
    rep = ''
    for card in reversed(deck.cards):
        rep += hb.colour_card_hash(card)
    return rep


while True:
    # sort results by their decreasing her status, and increasing monster status

    if not decks_new:
        # initialise at start
        prev = copy.deepcopy(start)
        decks_new = [prev]
        deck_new = decks_new[0]
        print("Welcome to the new game with the following deck:")
        symbol_description = "Each colour represents one character.\n" \
                             "The life status is represented by square symbols:"
        print(symbol_description)
        print(hb.card_status_symbols)
    else:
        decks_new.sort(key=lambda dx: (hb.get_status(dx).get("hero"), -hb.get_status(dx).get("monster")), reverse=True)

        # global card_colours, card_status .
        for k, d in enumerate(decks_new):
            s = build_graphical_representation_to_deck(d)
            print("{:3d}".format(k + 1), ":", s)

        if len(decks_new) != 1:
            option_number = request_number(maximum=len(decks_new))
        else:
            option_number = 1
            print("A single outcome evaluated. Proceeding automatically to a new deck...")
            # input("Please confirm by enter...")

        deck_new = decks_new[option_number - 1]
        deck_new.cards = hb.back_shift(deck_new.cards)

        print('The new deck to play is:')

    s = build_graphical_representation_to_deck(deck_new)
    print(' '*6 + s)

    if hb.get_deck_hash(deck_new) == '6A3A9A8A5A7A1A2A4A':
        pass

    deck_new_hash = hb.get_deck_hash(deck_new)
    deck_prev_hash = hb.get_deck_hash(prev)
    status = hb.get_status(deck_new)
    print(status)
    if deck_new_hash not in hb.game_turns:
        if deck_new_hash != deck_prev_hash:
            hb.game_turns[deck_new_hash] = deck_prev_hash
        if status.get("hero") == 0 or status.get("monster") == 0:
            game_deck_new = hb.recreate_game(deck_new_hash)
            hb.report_game_status(game_deck_new)
            break
        elif status.get("hero") != 0 \
                and status.get("monster") != 0:
            # no win or defeat, and deck changed
            decks_new = hb.play_card(deck_new)
            prev = deck_new
