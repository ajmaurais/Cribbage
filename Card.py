# +JMJ+
# Paul A Maurais
# 2018

class Card:
    """A single card. Attributes: name (Ace, One, ... King), suit, value (1-10), rank (1-13), and dataDict (tuple of the other four attributes)"""

    def __init__(self, name='', suit='N', value=0):
        """name (Ace, One, ... King), suit, value (1-10), rank (1-13). Assigns all four to the instance and an instance tuple"""
        self.name = name
        self.suit = suit
        self.value = value
        self.rank = self.assignRank()
        self.dataDict = {"name": name, "suit": suit, "value": value, "rank": self.rank}

    def assignRank(self):
        """returns a rank value.  The rank differs from the value ie value of king is 10 and rank is 13. used to score runs"""
        if self.value < 10:
            return self.value
        elif self.name == 'Ten':
            return 10
        elif self.name == 'Jack':
            return 11
        elif self.name == 'Queen':
            return 12
        else:
            return 13

    def __getitem__(self, key):
        """Indexing Scheme: 0-> name, 1-> suit, 2->value, 3->Rank """
        return self.dataDict[key]

    def __str__(self):
        return str(self.dataDict['name']+' of '+self.dataDict['suit'])

# +JMJ+
