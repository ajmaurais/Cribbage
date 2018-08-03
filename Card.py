#+JMJ+
#Paul A Maurais
#2018

class Card:
    """A single card. Attributes: name (Ace, One, ... King), suit, value (1-10), and dataTuple (tuple of the other three attributes)"""
    def __init__(self,name='',suit='N',value=0):
        """name (Ace, One, ... King), suit, value (1-10). Assigns all three to the instance and an instance tuple"""
        self.name=name
        self.suit=suit
        self.value = value
        self.dataTuple=(name,suit,value)

    def __getitem__(self, key):
        """Indexing Scheme: 0-> name, 1-> value, 2->value """
        return self.dataTupple[key]

    def __str__(self):
        return str(self.dataTuple)

#+JMJ+