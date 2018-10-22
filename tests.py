# +JMJ+
# Paul A Maurais
# 2018

import unittest
from Card import *
from Hand import *
from Deck import *
from Player import *
from Score import *


class scoreTest(unittest.TestCase):
    x = Card('Eight', 'H', 8)
    y = Card('Eight', 'S', 8)
    z = Card('Seven', 'S', 7)
    a = Card('Nine', 'C', 9)
    b = Card('Ten', 'H', 10)

    hand = Hand()
    hand.addCard(x)
    hand.addCard(y)
    hand.addCard(z)
    hand.addCard(a)
    hand.addCard(b)
    subsets = genSubsets(hand)

    def testGenSubsets(self):
        subsets = genSubsets(scoreTest.hand)
        self.assertEqual(len(subsets), 32)

    def testFifteens(self):
        self.assertEqual(fifteens(scoreTest.subsets), 4)

    def testPair(self):
        couples = [set for set in scoreTest.subsets if len(set) == 2]
        self.assertEqual(pairs(couples), 2)

    def testRun(self):
        runSets = [set for set in scoreTest.subsets if len(set) >= 3]
        self.assertEqual(runs(runSets), 8)

    def testScore(self):
        self.assertEqual(score(scoreTest.hand), 14)


if __name__ == '__main__':
    unittest.main()

# +JMJ+
