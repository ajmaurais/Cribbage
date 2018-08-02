#+JMJ+
#Paul A Maurais
#2018

from Card import Card
import random

class Deck:
    """A Full Deck of 52 cards"""

    def __init__(self):
        self.Cards = []
        self.Deck = []
        self.genCards()


    def genCards(self):
        """Generates a deck of 52 cards in order"""
        for suit in ['H','D','S','C']:
            self.Cards.append(Card(name='Ace',suit=suit,value=1))
            self.Cards.append(Card(name='Two', suit=suit, value=2))
            self.Cards.append(Card(name='Three', suit=suit, value=3))
            self.Cards.append(Card(name='Four', suit=suit, value=4))
            self.Cards.append(Card(name='Five', suit=suit, value=5))
            self.Cards.append(Card(name='Six', suit=suit, value=6))
            self.Cards.append(Card(name='Seven', suit=suit, value=7))
            self.Cards.append(Card(name='Eight', suit=suit, value=8))
            self.Cards.append(Card(name='Nine', suit=suit, value=9))
            self.Cards.append(Card(name='Ten', suit=suit, value=10))
            self.Cards.append(Card(name='Jack', suit=suit, value=10))
            self.Cards.append(Card(name='Queen', suit=suit, value=10))
            self.Cards.append(Card(name='King', suit=suit, value=10))

    def shuffle(self):
        """Generates a new, randomly shuffled deck"""
        self.Deck=[]
        for i in (random.sample(range(0,51),51)):
            self.Deck.append(self.Cards[i])

    def cut(self):
        """Shows card that resulted form cut, does not remove from deck"""
        cutIndex=random.randint(1,len(self.Deck))
        return self.Deck[cutIndex]

    def dealCard(self):
        """Deals a single card by popping the top card off the Deck"""
        return self.Deck.pop(0)



#+JMJ+