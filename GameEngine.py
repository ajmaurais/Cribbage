# +JMJ+
# Paul A Maurais
# 2018

# 121 points
# two player game only
from Player import Player
from Deck import Deck


def main():
    players = [Player(), Player()]
    deck = Deck()
    dealerIndex = selectDealer(players, deck)
    deck.shuffle()

    while (True):
        # every turn progresses: deal, play, peg
        deal(players, deck, dealerIndex)
        return


def selectDealer(players, deck):
    # lowest cut card deals.  If their rank matches, the first card drawn is the lowest
    i = 0;
    playerIndex = 0
    low = 14
    for player in players:
        temp = deck.cut()['rank']
        if temp < low:
            low = temp
            playerIndex = i
        print("player " + str(i + 1) + " drew a " + str(temp))
        i = i + 1
    players[playerIndex].dealer = True
    print("player " + str(playerIndex + 1) + " drew a the lowest card and is dealer")

    return playerIndex


def deal(players, deck, dealerIndex):
    for i in range(0, 12):
        players[(dealerIndex + 1 + i) % len(players)].hand.addCard(deck.dealCard())


if __name__ == '__main__':
    main()

# +JMJ+
