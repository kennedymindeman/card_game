from src.deck import Deck


class Hand:
    def __init__(self):
        self.cards = []

    def draw(self, deck: Deck, num_cards: int = 1):
        self.cards.extend(deck.draw(num_cards))
