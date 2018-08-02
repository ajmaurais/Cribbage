#+JMJ+
#Paul A Maurais
#2018


class Hand:
    def __init__(self):
        self.hand=[]

    def addCard(self,card):
        self.hand.append(card)

    def remCard(self,card):
        self.hand.remove(card)

    def scoreHand(self):
        #TODO generate methood to auto score and devise user scoring methood
        pass

#+JMJ+