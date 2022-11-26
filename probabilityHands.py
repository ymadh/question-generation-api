import itertools
import math
import random
from collections import Counter

# https://en.wikipedia.org/wiki/Poker_probability#5-card_poker_hands

# todo: figure out these calculations for storing the answers :/


def calc_two_of_a_kind():
    return ((13/1)*(4/2)*(12/3)*(4/1)*(4/1)*(4/1))


def calc_three_of_a_kind():
    return 0


def calc_four_of_a_kind():
    return 0


def calc_full_house():
    return 0


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
    probability = calc_full_house()
elif (maxNumCount == 4):
    print("Full House")
    probability = calc_four_of_a_kind()
elif (maxNumCount == 3):
    print("Full House")
    probability = calc_three_of_a_kind()
elif (maxNumCount == 2):
    print("Full House")
    probability = calc_two_of_a_kind()
else:
    print('High card?')

print(probability)
