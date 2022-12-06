from math import comb, pow

##################### START Poker Hand Frequencies ########################
def calcAllPossible():
    return comb(52, 5)

# Two of a Kind = One Pair
'''START N KIND'''
def calcTwoOfAKind():
    return (
        comb(13, 1)* comb(4, 2)* comb(12, 3)* pow(comb(4, 1), 3)
    )


def calcThreeOfAKind():
    return (
        comb(13, 1) * comb(4, 3) * comb(11, 1) * pow(comb(4, 1), 2)
    )


def calcFourOfAKind():
    return (
        comb(13, 1) * comb(4, 4) * comb(12, 1) * comb(4, 1)
    )
'''END N KIND'''
###
'''START FLUSH'''   
def calcRoyalFlush():
    return (
        comb(4, 1)
    )
def calcStraightFlush():
    return (
        (comb(10, 1) * comb(4, 1)) - comb(4, 1)
    )
    
def calcFlush():
    return (
        (comb(13, 5) * comb(4, 1)) - (comb(10, 1) * comb(4, 1))
    )
'''END FLUSH'''
###
'''START PAIR'''
def calcOnePair():
    return (
        calcTwoOfAKind()
    )
def calcTwoPair():
    return (
        comb(13, 2) * pow(comb(4, 2), 2) * comb(11, 1) * comb(4, 1)
    )
# No Pair = High Card
def calcNoPair():
    return (
        (comb(13, 5) - comb(10, 1)) * (pow(comb(4, 1), 5) - comb(4, 1))
    )
'''END PAIR'''
###
'''START OTHER'''
def calcFullHouse():
    return (
        comb(13, 1) * comb(4, 3) * comb(12, 1) * comb(4, 2)
    )
def calcStraight():
    return (
        (comb(10, 1) * pow(comb(4, 1), 5)) -  (comb(10, 1) * comb(4, 1))
    )
'''END OTHER'''
##################### END Poker Hand Frequencies ########################