from src.field import Field
from src.hand import Hand


class Player:
    def __init__(self, name, deck):
        self.name = name
        self.deck = deck
        self.hand = Hand()
        self.field = Field()
        self.graveyard = []
