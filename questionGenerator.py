from fractions import Fraction
import itertools
from os import remove
import random

# make a deck of cards
deck = list(itertools.product(['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K'],
                              ['Spade', 'Heart', 'Diamond', 'Club']))

numCards = len(deck)


# removes an item from the deck of cards so it doesn't get used again
# only works with single digits
def remove_items(test_list, item, typeOfMatch):

    if (typeOfMatch == 'colorAndSuite'):
        res = list(filter(
            lambda tup: (tup != item),
            test_list
        ))
        return res
    elif (typeOfMatch == 'numberOnly'):
        res = list(filter(
            lambda tup: (tup[0] != item),
            test_list
        ))
        return res


# chances of getting a single value
usedDeck = deck.copy()
# 13 values
for i in range(13):
    draw = random.choice(usedDeck)
    print("What are the chances of drawing a ", draw[0])
    # find the number of items in a deck
    # ie how many 4's are there
    foundValues = list(filter(
        lambda tup: (tup[0] == draw[0]),
        deck
    ))
    numValuesFound = len(foundValues)
    print(Fraction(numValuesFound, numCards))
    # add to a used list so we dont repeat
    usedDeck = remove_items(usedDeck, draw[0], 'numberOnly')

print("checking multiple number and suite")
# chances of getting a certain card and suite (should be 1/52)
# start again
usedDeck = deck.copy()
for i in range(52):
    draw = random.choice(deck)
    print("What are the chances of drawing a ", draw)
    # calculate the odds
    foundValues = list(filter(
        lambda tup: (tup == draw),
        deck
    ))
    numValuesFound = len(foundValues)
    print(Fraction(numValuesFound, numCards))
    # add to a used list so we dont repeat
    usedDeck = remove_items(usedDeck, draw, 'numberAndSuite')
