from math import comb, pow

##################### START Poker Hand Probabilities ########################
def calcAllPossible():
    return comb(52, 5)

# Two of a Kind = One Pair
'''START N KIND'''
def calcTwoOfAKind():
    return (
        (comb(13, 1)* comb(4, 2)* comb(12, 3)* pow(comb(4, 1), 3))/calcAllPossible()
    )


def calcThreeOfAKind():
    return (
        (comb(13, 1) * comb(4, 3) * comb(11, 1) * pow(comb(4, 1), 2))/calcAllPossible()
    )


def calcFourOfAKind():
    return (
        (comb(13, 1) * comb(4, 4) * comb(12, 1) * comb(4, 1))/calcAllPossible()
    )
'''END N KIND'''
###
'''START FLUSH'''   
def calcRoyalFlush():
    return (
        (comb(4, 1))/calcAllPossible()
    )
def calcStraightFlush():
    return (
        ((comb(10, 1) * comb(4, 1)) - comb(4, 1))/calcAllPossible()
    )
    
def calcFlush():
    return (
        ((comb(13, 5) * comb(4, 1)) - (comb(10, 1) * comb(4, 1)))/calcAllPossible()
    )
'''END FLUSH'''
###
'''START PAIR'''
def calcOnePair():
    return (
        (calcTwoOfAKind())/calcAllPossible()
    )
def calcTwoPair():
    return (
        (comb(13, 2) * pow(comb(4, 2), 2) * comb(11, 1) * comb(4, 1))/calcAllPossible()
    )
    
# No Pair = High Card
def calcNoPair():
    return (
        ((comb(13, 5) - comb(10, 1)) * (pow(comb(4, 1), 5) - comb(4, 1)))/calcAllPossible()
    )
'''END PAIR'''
###
'''START OTHER'''
def calcFullHouse():
    return (
        (comb(13, 1) * comb(4, 3) * comb(12, 1) * comb(4, 2))/calcAllPossible()
    )
def calcStraight():
    return (
        ((comb(10, 1) * pow(comb(4, 1), 5)) -  (comb(10, 1) * comb(4, 1)))/calcAllPossible()
    )
'''END OTHER'''
##################### END Poker Hand Probabilities ########################