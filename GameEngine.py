# +JMJ+
# Paul A Maurais
# 2018

# 121 points
# two player game only
from Player import Player
from Deck import Deck
from Hand import Hand


def main():
    players = [Player(), Player()]
    deck = Deck()
    dealerIndex = selectDealer(players, deck)
    deck.shuffle()

    while (True):
        # every turn progresses: deal, play, peg
        deal(players, deck, dealerIndex)
        crib=discard(players)
        print(crib)


def selectDealer(players, deck):
    '''lowest cut card deals.  If their rank matches, the first card drawn is the lowest'''
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
    '''Deal cards to the players in player list'''
    for i in range(0, 12):
        players[(dealerIndex + 1 + i) % len(players)].hand.addCard(deck.dealCard())

def discard(players):
    '''Promp players to discard cards and use discarded cards to build the crib. returns crib (Hand)'''
    crib=Hand()
    playerNum=1
    for player in players:
        for i in range(0,2):
            if i==0:
                string='first'
            else:
                string= 'second'
            print(player.hand)
            discardIndex=getInput(playerNum,string)
            crib.addCard(player.hand.remCard(int(discardIndex)-1))
        playerNum+=1

    return crib

def getInput(playerNum,string):
    '''broken into its own function for testing'''
    return input("Player " + str(playerNum) + ' Select index of ' + string + " card to discard: \n")


if __name__ == '__main__':
    main()

# +JMJ+
