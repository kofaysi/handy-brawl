"""
"""
# import handybrawl as hb
#import copy
# import re


def hash2deck(d_hash):
    """
    Separates numbers and letter in the hash and creates

    :param d_hash: the hash of a deck
    :return: two lists, a list of numbers and a list of faces
    """
    faces = {'A', 'B', 'C', 'D'}
    hash_new = ''
    for i, s in enumerate(d_hash):
        if i > 0 and (d_hash[i - 1] in faces) ^ (s in faces):
            hash_new += ' '
        hash_new += s
    # hash_new = [w for i, s in enumerate(d_hash) if (i > 0 and (d_hash[i - 1] in faces) ^ (s in faces)) else w += s]

    # split the string by the separator ' '
    hash_list = hash_new.split(' ')
    return [[int(hash_list[i]), hash_list[i+1]] for i in range(0, len(hash_list) - 1, 2)]


class Deck:

    def __init__(self, parameter=None):
        if isinstance(parameter, str):
            self.cards = hash2deck(parameter)
        if isinstance(parameter, list):
            self.cards = parameter
        # self.origin = Deck()  # The origin can be assigned without initialisation.
        self.actions = []
        self.prev = None

    def __eq__(self, other):
    # use 'is' to compare for identity of two deck objects
       if not isinstance(other, Deck):
           # don't attempt to compare against unrelated types
           return NotImplemented

       return self.cards == other.cards

    def __hash__(self):
        # necessary for instances to behave sanely in dicts and sets.
        return hash(self.hash_str)

    def __len__(self):
        return len(self.cards)

    @property
    def top_number(self):
        self.cards[0][0]

    @property
    def top_face(self):
        self.cards[0][1]

    @property
    def hash_str(self):
        """
        The method is a property. Use assignment
            new = Deck(other.hash_str)
        to get the hash_str for a new deck
            new.hash_str

        :return: int hash
        """
        return ''.join([str(value) for card in self.cards for value in card])

    def add_action(self, action):
        self.actions += [element for element in action]

    def game(self):
        if self.prev:
            return [self.prev] + self.prev.game()
        else:
            return []


start = Deck('5A9A4A8A3A7A2A6A1A')
new = copy.deepcopy(start)
pass
