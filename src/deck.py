class Deck:
    def __init__(self):
        self.cards = []

    def draw(self, num_cards=1):
        drawn_cards, self.cards = self.cards[:num_cards], self.cards[num_cards:]
        return drawn_cards
