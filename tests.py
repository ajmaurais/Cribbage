import unittest
from Card import *
from Hand import *
from Deck import *
from Player import *
from Score import *


class scoreTest(unittest.TestCase):
    x = Card.Card('Eight', 'H', 8)
    y = Card.Card('Eight', 'S', 8)
    z = Card.Card('Seven', 'S', 7)
    a = Card.Card('Nine', 'C', 9)
    b = Card.Card('Ten', 'H', 10)

    hand=Hand.Hand()
    hand.addCard(x)
    hand.addCard(y)
    hand.addCard(z)
    hand.addCard(a)
    hand.addCard(b)
    subsets = genSubsets(hand)

    def testGenSubsets(self):
        subsets=genSubsets(scoreTest.hand)
        self.assertEqual(len(subsets), 32)

    def testFifteens(self):
        self.assertEqual(fiftines(scoreTest.subsets),2)

    def testPair(self):
        couples=[set for set in scoreTest.subsets if len(set)==2]
        self.assertEqual(pairs(couples),1)


if __name__ == '__main__':
    unittest.main()