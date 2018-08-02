#+JMJ+
#Paul A Maurais
#2018


class Hand:
    def __init__(self):
        self.cards=[]

    def addCard(self,card):
        self.cards.append(card)

    def remCard(self,card):
        self.cards.remove(card)

    def __getitem__(self, key):
        return self.cards[key]

#+JMJ+