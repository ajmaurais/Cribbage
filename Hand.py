# +JMJ+
# Paul A Maurais
# 2018
from Card import Card

class Hand:
    def __init__(self):
        self.cards = []

    def addCard(self, card):
        self.cards.append(card)

    def remCard(self, card):
        if isinstance(card,Card):
            self.cards.remove(card)
            return card
        elif isinstance(card, int):
            return self.cards.pop(card)

    def __getitem__(self, key):
        return self.cards[key]

    def __len__(self):
        return len(self.cards)

    def __iter__(self):
        return iter(self.cards)

    def __str__(self):
        return str([str(card) for card in self.cards])

# +JMJ+
