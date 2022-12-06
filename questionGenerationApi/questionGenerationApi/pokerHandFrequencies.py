from math import comb, pow

##################### START Poker Hand Frequencies ########################
def calc_all_possible():
    return comb(52, 5)

# Two of a Kind = One Pair
'''START N KIND'''
def calc_two_of_a_kind():
    return (
        comb(13, 1)* comb(4, 2)* comb(12, 3)* pow(comb(4, 1), 3)
    )


def calc_three_of_a_kind():
    return (
        comb(13, 1) * comb(4, 3) * comb(11, 1) * pow(comb(4, 1), 2)
    )


def calc_four_of_a_kind():
    return (
        comb(13, 1) * comb(4, 4) * comb(12, 1) * comb(4, 1)
    )
'''END N KIND'''
###
'''START FLUSH'''   
def calc_royal_flush():
    return (
        comb(4, 1)
    )
def calc_straight_flush():
    return (
        (comb(10, 1) * comb(4, 1)) - comb(4, 1)
    )
    
def calc_flush():
    return (
        (comb(13, 5) * comb(4, 1)) - (comb(10, 1) * comb(4, 1))
    )
'''END FLUSH'''
###
'''START PAIR'''
def calc_one_pair():
    return (
        calc_two_of_a_kind()
    )
def calc_two_pair():
    return (
        comb(13, 2) * pow(comb(4, 2), 2) * comb(11, 1) * comb(4, 1)
    )
# No Pair = High Card
def calc_no_pair():
    return (
        (comb(13, 5) - comb(10, 1)) * (pow(comb(4, 1), 5) - comb(4, 1))
    )
'''END PAIR'''
###
'''START OTHER'''
def calc_full_house():
    return (
        comb(13, 1) * comb(4, 3) * comb(12, 1) * comb(4, 2)
    )
def calc_straight():
    return (
        (comb(10, 1) * pow(comb(4, 1), 5)) -  (comb(10, 1) * comb(4, 1))
    )
'''END OTHER'''
##################### END Poker Hand Frequencies ########################