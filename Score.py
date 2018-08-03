#+JMJ+
#Paul A Maurais
#2018

import Hand
import Card
import itertools

def score(hand):
    total=0

    if len(hand) != 5:
        print("Incorrect Hand Length")
        return

    subsets=genSubsets(hand) #subsets of the hand are used in all possible scoreings

    total+=(fiftines(subsets)*2) #15s
    total+=(pairs([set for set in subsets if len(set)==2])*2) #pairs (compute only on subsets that have a len of 2)
    total+=(runs([set for set in subsets if len(set>=3)])) #runs (only compute on subsets with len >=3)

    return total

def genSubsets(set):
    """Generates all possible subsets of the hand"""
    if set == []:
        return [[]]

    x = genSubsets(set[1:])
    return x + [[set[0]] + y for y in x]

def fiftines(subsets):
    """Calculates the number of subsets in the hand that sum to 15"""
    count=0
    for set in subsets:
        setSum=0
        for card in set:
            setSum+=card.value
        if setSum==15:
            count+=1

    return count

def pairs(subsets):
    """Calculates the number of subsets that have pairs.  Subsets must have len 2"""
    count=0
    for set in subsets:
        if len(set) != 2:
            print("Incorrect Set Length, must be 2")
            return

        if set[0].name==set[1].name:
            count+=1

    return count

def runs(subsets):
    value=0
    subsets=order(subsets)

def order(subsets):
    pass



#+JMJ+