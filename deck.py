"""
"""
# import handybrawl as hb
import copy
import re


def unzip(d_hash):
    """
    Separates numbers and letter in the hash and creates

    :param d_hash: the hash of a deck
    :return: two lists, a list of numbers and a list of faces
    """
    matches = re.findall(r'\d+|\D+', d_hash)
    return [[int(matches[i]), matches[i + 1]] for i in range(0, len(matches) - 1, 2)]


class Deck:

    def __init__(self, parameter=None):
        if isinstance(parameter, str):
            self.deck = unzip(parameter) if parameter else None
        if isinstance(parameter, list):
            self.deck = parameter
        # self.origin = Deck()  # The origin can be assigned without initialisation.
        self.actions = []

    def __eq__(self, other):
        if not isinstance(other, Deck):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.deck == other.deck

    def __hash__(self):
        # necessary for instances to behave sanely in dicts and sets.
        return hash(self.zip_str)

    @property
    def zip_str(self):
        """
        The method is a property. Use assignment
            new = Deck(other.zip_str)
        to get the zip_str for a new deck
            new.zip_str

        :return: int zip
        """
        return ''.join([str(value) for card in self.deck for value in card])

    def next_action(self, action):
        self.actions.append(action)


start = Deck('5A9A4A8A3A7A2A6A1A')
new = copy.deepcopy(start)
pass
