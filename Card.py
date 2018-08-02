#+JMJ+
#Paul A Maurais
#2018

class Card:
    def __init__(self,name='',suit='N',value=0):
        self.name=name
        self.suit=suit
        self.value = value
        self.dataTupple=(name,suit,value)

    def __getitem__(self, key):
        return self.dataTupple[key]

#+JMJ+