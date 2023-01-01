import cards


class HandyBrawlDeck:
    """class for the deck management game Handy Brawl https://boardgamegeek.com/boardgame/362692/handy-brawl"""

    def flip(self, c):
        return [c[0], c[3], c[4], c[1], c[2]]

    def rotate(self, c):
        return [c[0], c[2], c[1], c[4], c[3]]

    def rotate_card_to_face(self, c, f):
        c_new = c
        face_current = c_new[1][0].get("face")
        if face_current != f:
            c_new = self.rotate(c[:])
            face_current = c_new[1][0].get("face")
            if face_current != f:
                c_new = self.flip(c[:])
                face_current = c_new[1][0].get("face")
                if face_current != f:
                    c_new = self.flip(self.rotate(c[:]))
        return c_new

    def create_deck(self, d_hash):
        self.deck = []
        d_items = [d_hash[i:i + 2] for i in range(0, len(d_hash), 2)]
        for number_face in d_items:
            for card in cards.cards:
                number = int(number_face[:-1])
                face = number_face[-1]
                if card[0].get("number") == number:
                    c_new = self.rotate_card_to_face(self, card[:], face)
                    self.deck.append(c_new)
        return self.deck

    def __init__(self, hash):
        self.hash = hash
        self.deck = self.create_deck(hash)
