# +JMJ+
# Paul A Maurais
# 2018

# 121 points
from Player import Player
from Deck import Deck


def main():
    players = [Player(), Player()]
    deck = Deck()
    selectDealer(players, deck)


def selectDealer(players, deck):
    # lowest cut card deals
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


if __name__ == '__main__':
    main()

# +JMJ+
