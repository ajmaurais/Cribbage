# +JMJ+
# Paul A Maurais
# 2018

from unittest.mock import patch
import unittest
from Card import *
from Hand import *
from Deck import *
from Player import *
from Score import *
import GameEngine
import copy


class gameTest(unittest.TestCase):
    deck = Deck()
    x = Card('Eight', 'H', 8)
    y = Card('Eight', 'S', 8)
    z = Card('Seven', 'S', 7)
    a = Card('Nine', 'C', 9)
    b = Card('Ten', 'H', 10)
    c = Card('Ten', 'H', 10)
    x1 = Card('Eight', 'H', 8)
    y1 = Card('Eight', 'S', 8)
    z1 = Card('Seven', 'S', 7)
    a1 = Card('Nine', 'C', 9)
    b1 = Card('Ten', 'H', 10)
    c1 = Card('Ten', 'H', 10)

    deck.Deck = [x, y, z, a, b, c, x1, y1, z1, a1, b1, c1]

    def testDealerP1(self):
        deck = copy.deepcopy(self.deck)
        players = [Player(), Player()]
        GameEngine.deal(players,deck,0)

        actualCards = []
        for card in players[0].hand:
            actualCards.append((card['suit'], card['rank']))
        self.assertEqual([('S', 8), ('C', 9), ('H', 10), ('S', 8), ('C', 9), ('H', 10)], actualCards)

        actualCards = []
        for card in players[1].hand:
            actualCards.append((card['suit'], card['rank']))
        self.assertEqual([('H', 8), ('S', 7), ('H', 10), ('H', 8), ('S', 7), ('H', 10)], actualCards)

    def testDealerP2(self):
        deck = copy.deepcopy(self.deck)
        players=[Player(),Player()]
        GameEngine.deal(players,deck,1)

        actualCards=[]
        for card in players[1].hand:
            actualCards.append((card['suit'],card['rank']))
        self.assertEqual([('S', 8),('C', 9),('H', 10),('S', 8),('C', 9),('H', 10)],actualCards)

        actualCards = []
        for card in players[0].hand:
            actualCards.append((card['suit'], card['rank']))
        self.assertEqual([('H', 8), ('S', 7), ('H', 10), ('H', 8), ('S', 7), ('H', 10)],actualCards)

    @patch('GameEngine.getInput', return_value='1')
    def testDiscard(self,input):
        deck = copy.deepcopy(self.deck)
        players = [Player(), Player()]
        GameEngine.deal(players, deck, 0)
        crib=(GameEngine.discard(players))

        actualCards = []
        for card in players[0].hand:
            actualCards.append((card['suit'], card['rank']))
        self.assertEqual([('H', 10), ('S', 8), ('C', 9), ('H', 10)], actualCards)

        actualCards = []
        for card in players[1].hand:
            actualCards.append((card['suit'], card['rank']))
        self.assertEqual([('H', 10), ('H', 8), ('S', 7), ('H', 10)], actualCards)

        actualCards=[]
        for card in crib:
            actualCards.append((card['suit'], card['rank']))
        self.assertEqual([('S', 8), ('C', 9), ('H', 8), ('S', 7)], actualCards)



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
