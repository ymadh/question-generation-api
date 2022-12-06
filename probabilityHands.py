import itertools
import math
from math import comb, pow
import random
from collections import Counter

# https://en.wikipedia.org/wiki/Poker_probability#5-card_poker_hands

# todo: figure out these calculations for storing the answers :/

# NOTE: These are frequencies/counts, not probability

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
##################### END Poker Hands ########################

# make a deck of cards
deck = list(itertools.product(range(1, 14), [
    'Spade', 'Heart', 'Diamond', 'Club']))
# shuffle the cards
random.shuffle(deck)
tmpVal = [0, 0, 0, 0, 0]
# draw five cards
print("You got:")
for i in range(5):
    print(deck[i][0], deck[i][1])
    # store just the number (for the 2 of a kind,3,4,fullhouse)
    tmpVal[i] = deck[i][0]


# calculate the probability of 2 of a kind, 3, etc
c = Counter(tmpVal)
maxNums = c.most_common(1)
nextHighest = c.most_common(2)

# store the count only (not the card)
maxNumCount = maxNums[0][1]
nextHighestCount = nextHighest[0][1]

# default value
probability = 0.0000
# look for full house
if (maxNumCount == 3 and nextHighestCount == 2):
    print("Full House")
    probability = calc_full_house()/calc_all_possible
elif (maxNumCount == 4):
    print("Full House")
    probability = calc_four_of_a_kind()/calc_all_possible
elif (maxNumCount == 3):
    print("Full House")
    probability = 1/calc_three_of_a_kind()/calc_all_possible
elif (maxNumCount == 2):
    print("Full House")
    probability = 1/calc_two_of_a_kind()/calc_all_possible
else:
    print('High card?')

print(probability)
