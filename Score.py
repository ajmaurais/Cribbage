#+JMJ+
#Paul A Maurais
#2018

def score(hand):
    total=0

    if len(hand) != 5:
        print("Incorrect Hand Length")
        return

    subsets=genSubsets(hand) #subsets of the hand are used in all possible scoreings

    total+=fifteens(subsets) #15s
    total+=pairs([set for set in subsets if len(set)==2]) #pairs (compute only on subsets that have a len of 2)
    total+=runs([set for set in subsets if len(set)>=3]) #runs (only compute on subsets with len >=3)

    return total

def genSubsets(set):
    """Generates all possible subsets of the hand"""
    if set == []:
        return [[]]

    x = genSubsets(set[1:])
    return x + [[set[0]] + y for y in x]

def fifteens(subsets):
    """Calculates the number of subsets in the hand that sum to 15. returns count*2 for score"""
    count=0
    for set in subsets:
        setSum=0
        for card in set:
            setSum+=card.value
        if setSum==15:
            count+=1

    return count*2

def pairs(subsets):
    """Calculates the number of subsets that have pairs.  Subsets must have len 2. returns count*2 for score"""
    count=0
    for set in subsets:
        if len(set) != 2:
            print("Incorrect Set Length, must be 2")
            return

        if set[0].name==set[1].name:
            count+=1

    return count*2

def runs(subsets):
    """Calculates the value of the runs in a hand"""
    #an important note on runs: if there is a run of len 3 and a run of len 3+n where n is an element of the set [1,2]
    #(four cards in hand plus starter makes five) the run of len 3 must be a subset of the run of len 3+n.  In other
    #words, There can not be BOTH a run of len 3 and a run of len 3+n, there is only the run of higher len value.  The
    #same principal holds true for runs of len 4 and len 5.  The run of len 4 must be a subset of the run of len 5.

    value=0
    maxRunLen=0
    #order each set and count only those where every element in the set is in sequential order
    for set in subsets:
        set=order(set) #order the set to make determining a run easier

        runLen = 1  # keep track of run len.  Only runs of the max len will be counted
        curr = set[0].sequenceNumber
        for card in set[1:]:
            if card.sequenceNumber==curr+1:
                runLen+=1
                curr+=1
            else:
                runLen=1
                break #only count runs that span the whole set (every subset of the hand is coverd)

        #only count the max run and any runs of equivilent len
        if runLen>maxRunLen:
            value=runLen
            maxRunLen=runLen
        elif runLen==maxRunLen:
            value+=runLen

    return value

def order(subsets):
    """Orders a subset based off of enumeration value"""
    return sorted(subsets, key= lambda card:card.sequenceNumber)




#+JMJ+