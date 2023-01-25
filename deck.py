"""
"""
# import handybrawl as hb
import copy


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
    deck = []
    for i, n in enumerate(numbers):
        deck.append([n, faces[i]])
    return deck


class Deck:

    def __init__(self, parameter=None):
        if isinstance(parameter, str):
            self.deck = unzip_hash(parameter) if parameter else None
        if isinstance(parameter, list):
            self.deck = parameter
        self.origin = self.deck
        self.actions = []

    def __eq__(self, other):
        if not isinstance(other, Deck):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.deck == other.deck

    def __hash__(self):
        # necessary for instances to behave sanely in dicts and sets.
        return hash(self.hash_str)

    @property
    def hash_str(self):
        """
        The method is a property. Use assignment
            new = Deck(other.hash_str)
        to get the hash_str for a new deck
            new.hash_str

        :return: int hash
        """
        return ''.join([str(value) for card in self.deck for value in card])

    def next_action(self, action):
        self.actions.append(action)


start = Deck('5A9A4A8A3A7A2A6A1A')
new = copy.deepcopy(start)
pass
