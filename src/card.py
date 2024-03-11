class Card:
    pass


class MonsterCard(Card):
    def __init__(self, name, attack, defense, effects=None):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.effects = effects
        self.position = None
