from .models import Question
from fractions import Fraction
import itertools
import random
from .pokerHandProbability import *
from enum import Enum

def saveNewQuestion(question):
    q = Question(
        name=question.name,
        questionText=question.questionText,
        answer=question.answer,
        difficulty=question.difficulty,
        numInputs=question.numInputs,
    )
    q.save()


# removes an item from the deck of cards so it doesn't get used again
# only works with single decks
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

''' OLD - Generates Many
def singleCardNumberOnly(deck):
    # chances of getting a single value from a deck off cards
    usedDeck = deck.copy()
    for i in range(13):
        draw = random.choice(usedDeck)
        q = Question()
        q.name = "Single Card Number Only"
        q.questionText = f'What are the chances of drawing a {draw[0]} from a single deck of cards?'
        q.answer = round(4/52, 2)
        q.difficulty = 1
        q.numInputs = 0
        saveNewQuestion(q)
        usedDeck = remove_items(usedDeck, draw[0], 'numberOnly')
'''

''' OLD - Generates Many
def singleCard(deck):
    # chances of card value and suit from a deck of cards
    usedDeck = deck.copy()
    for i in range(52):
        draw = random.choice(deck)
        q = Question()
        q.name = "Single Card"
        q.questionText = f'What are the chances of drawing a {draw[0]} of {draw[1]} from a single deck of cards?'
        q.answer = round(1/52, 2)
        q.difficulty = 1
        q.numInputs = 0
        saveNewQuestion(q)
        # add to a used list so we dont repeat
        usedDeck = remove_items(usedDeck, draw, 'numberAndSuite')
'''

''' OLD - Generates Many
def colorOrNumber(numbers, color):
    for i in range(len(numbers)):
        for j in range(len(color)):
            q = Question()
            q.name = "Simple OR"
            q.questionText = f'What are the chances of drawing either {color[j]} or {numbers[i]}?'
            # 26 + 4 - 2 = 28
            q.answer = 0.54
            q.difficulty = 5
            q.numInputs = 0
            saveNewQuestion(q)
'''



# chances of getting a single VALUE from a deck off cards
def singleCardNumberOnly(deck):
    usedDeck = deck.copy()
    draw = random.choice(usedDeck)
    q = Question()
    q.name = "Single Card Number Only"
    q.questionText = f'What are the chances of drawing a {draw[0]} from a single deck of cards?'
    q.answer = round(4/52, 2)
    q.difficulty = 1
    q.numInputs = 0
    saveNewQuestion(q)
    usedDeck = remove_items(usedDeck, draw[0], 'numberOnly')

# chances of card VALUE and SUIT from a deck of cards
def singleCard(deck):

    usedDeck = deck.copy()
    draw = random.choice(deck)
    q = Question()
    q.name = "Single Card"
    q.questionText = f'What are the chances of drawing a {draw[0]} of {draw[1]} from a single deck of cards?'
    q.answer = round(1/52, 2)
    q.difficulty = 1
    q.numInputs = 0
    saveNewQuestion(q)

def colorOrNumber(numbers, color):
    i = random.choice(range(len(numbers)))
    j = random.choice(range(len(color)))
    q = Question()
    q.name = "Simple OR"
    q.questionText = f'What are the chances of drawing either {color[j]} or {numbers[i]}?'
    # 26 + 4 - 2 = 28
    q.answer = 0.54
    q.difficulty = 5
    q.numInputs = 0
    saveNewQuestion(q)

###################################################################################################################
'''POKER HANDS'''

''' OLD Generates Many
# n of a kind... type questions
def multipleCards(deck):
    usedDeck = deck.copy()
    for numCards in range(2, 4):
        for i in range(52):
            draw = random.choice(deck)
            q = Question()
            q.name = "Multiple Card"
            q.questionText = f'What are the chances of drawing {numCards} {draw[0]}\'s from a 5 card draw?'
            if (numCards == 2):
                q.answer = calcTwoOfAKind()/calcAllPossible()
            elif (numCards == 3):
                q.answer = calcThreeOfAKind()/calcAllPossible()
            elif (numCards == 4):
                q.answer = calcFourOfAKind()/calcAllPossible()
            q.difficulty = numCards  # two of a kind is easier than 4 of a kind
            q.numInputs = 0
            saveNewQuestion(q)
            # add to a used list so we dont repeat
            usedDeck = remove_items(usedDeck, draw, 'numberAndSuite')
'''

''' OLD Generates Many
# todo: randomize the draw 1,2,3 and 4,5 for types of suites drawn
# this will add a lot
def fullhouse(deck):
    # chances of getting a certain card and suite (should be 1/52)
    # start again
    usedDeck = deck.copy()
    for i in range(10):
        # could add more variability here
        draw1 = usedDeck[i]
        draw2 = usedDeck[i+1]
        draw3 = usedDeck[i+2]
        usedDeck = remove_items(usedDeck, draw1[0], 'numberOnly')
        for j in range(i+1, 11):
            # could add more variability here
            draw4 = usedDeck[j]
            draw5 = usedDeck[j+1]
            q = Question()
            q.name = "Full House"
            q.questionText = f'What are the chances of drawing {draw1} {draw2} {draw3} {draw4} {draw5}?'
            q.answer = calcFullHouse()/calcAllPossible()
            q.difficulty = 6
            q.numInputs = 0
            saveNewQuestion(q)
'''

''' OLD - Generates MANY questions
def twoPairs(deck):
    usedDeck = deck.copy()

    hands = list(itertools.combinations(usedDeck, 5))
    twoPairs = []

    for hand in hands:
        values = [hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]]
        unique = list(set(values))
        
        if(len(unique) == 3):
            c1 = values.count(unique[0])
            c2 = values.count(unique[1])
            c3 = values.count(unique[2])
            if( 
            (c1 == c2 and c3 == 1) or 
            (c2 == c3 and c1 == 1) or
            (c3 == c1 and c2 == 1) 
            ):
                twoPairs.append(hand)

    for hand in twoPairs:        
        q = Question()
        q.name = "Two Pair"
        q.questionText = f'What are the chances of drawing {hand[0]} {hand[1]} {hand[2]} {hand[3]} {hand[4]}?'
        q.answer = calcTwoPair()/calcAllPossible()
        q.difficulty = 5
        q.numInputs = 0
        saveNewQuestion(q)
'''

# Just so we only have to calc these only once to save computational power.
class PokerHandProb(float, Enum):
    ROYAL_FLUSH = (calcRoyalFlush(),)
    STRAIGHT_FLUSH = (calcStraightFlush(),)
    FOUR_KIND = (calcFourOfAKind(),)
    FULL_HOUSE = (calcFullHouse(),)
    FLUSH = (calcFlush(),)
    STRAIGHT = (calcStraight(),)
    THREE_KIND = (calcThreeOfAKind(),)
    TWO_PAIR = (calcTwoPair(),)
    ONE_PAIR = (calcOnePair(),)
    HIGH_CARD = (calcNoPair(),)
    
    def __call__(self, *args, **kwargs):
        self.value[0](*args, **kwargs)
    
# All of these generate only one question instead of hundred of thousands or over a million LOL 

def highCard(deck):
    usedDeck = deck.copy()
    SpadesIndices = []
    randomVals = []

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))
        
    # Get a random values from the spades cards using index.
    randomVals = random.sample(SpadesIndices, 5)
        
    draw1 = usedDeck[random.choice(range(randomVals[0], randomVals[0]+4))]
    draw2 = usedDeck[random.choice(range(randomVals[1], randomVals[1]+4))]
    draw3 = usedDeck[random.choice(range(randomVals[2], randomVals[2]+4))]
    draw4 = usedDeck[random.choice(range(randomVals[3], randomVals[3]+4))]
    draw5 = usedDeck[random.choice(range(randomVals[4], randomVals[4]+4))]
    
    q = Question()
    q.name = "High Card"
    q.questionText = (    
        f'What are the chances of drawing a 5-hand Poker hand with ' + 
        f'the {draw1[0]} of {draw1[1]}, ' + 
        f'the {draw2[0]} of {draw2[1]}, ' +
        f'the {draw3[0]} of {draw3[1]}, ' +
        f'the {draw4[0]} of {draw4[1]}, and ' +
        f'the {draw5[0]} of {draw5[1]}?'
    )
    q.answer = PokerHandProb.HIGH_CARD.value
    q.difficulty = 5
    q.numInputs = 0
    saveNewQuestion(q)

def onePair(deck):
    usedDeck = deck.copy()
    SpadesIndices = []

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))
        
    # Get a random value from the spades cards using index.
    pairValueIndex = random.choice(SpadesIndices)

    # Get Pair Cards
    pairIndices = random.sample(range(pairValueIndex, pairValueIndex + 3), 2)
    draw1 = usedDeck[pairIndices[0]]
    draw2 = usedDeck[pairIndices[1]]

    # Remove the value that has the pair from deck (4 cards)
    usedDeck = remove_items(usedDeck, draw1[0], 'numberOnly')

    # Get three random cards from usedDeck
    remainingIndices = random.sample(range(0, 49), 3)
    draw3 = usedDeck[remainingIndices[0]]
    draw4 = usedDeck[remainingIndices[1]]
    draw5 = usedDeck[remainingIndices[2]]
    
    q = Question()
    q.name = "One Pair"
    q.questionText = (    
        f'What are the chances of drawing a 5-hand Poker hand with ' + 
        f'the {draw1[0]} of {draw1[1]}, ' + 
        f'the {draw2[0]} of {draw2[1]}, ' +
        f'the {draw3[0]} of {draw3[1]}, ' +
        f'the {draw4[0]} of {draw4[1]}, and ' +
        f'the {draw5[0]} of {draw5[1]}?'
    )
    q.answer = PokerHandProb.ONE_PAIR.value
    q.difficulty = 4
    q.numInputs = 0
    saveNewQuestion(q)

# Generates only one question  
def twoPair(deck):
    usedDeck = deck.copy()
    SpadesIndices = []

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))
        
    # Get two random values from the spades cards using index
    pairValueIndices = random.sample((SpadesIndices), 2)

    # Get Pair Cards 1
    pairIndices1 = random.sample(range(pairValueIndices[0], pairValueIndices[0] + 4), 2)
    draw1 = usedDeck[pairIndices1[0]]
    draw2 = usedDeck[pairIndices1[1]]

    # Get Pair Cards 2
    pairIndices2 = random.sample(range(pairValueIndices[1], pairValueIndices[1] + 4), 2)
    draw3 = usedDeck[pairIndices2[0]]
    draw4 = usedDeck[pairIndices2[1]]

    # Remove the value that has the pair from deck (8 cards)
    usedDeck = remove_items(usedDeck, draw1[0], 'numberOnly')
    usedDeck = remove_items(usedDeck, draw3[0], 'numberOnly')
    
    # Get one random cards from usedDeck
    remainingIndices = random.sample(range(0, 45), 1)
    draw5 = usedDeck[remainingIndices[0]]
    
    q = Question()
    q.name = "Two Pair"
    q.questionText = (    
        f'What are the chances of drawing a 5-hand Poker hand with ' + 
        f'the {draw1[0]} of {draw1[1]}, ' + 
        f'the {draw2[0]} of {draw2[1]}, ' +
        f'the {draw3[0]} of {draw3[1]}, ' +
        f'the {draw4[0]} of {draw4[1]}, and ' +
        f'the {draw5[0]} of {draw5[1]}?'
    )
    q.answer = PokerHandProb.TWO_PAIR.value
    q.difficulty = 5
    q.numInputs = 0
    saveNewQuestion(q)
    
def threeOfAKind(deck):
    usedDeck = deck.copy()
    SpadesIndices = []

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))
        
    # Get a random value from the spades cards using index.
    tripleVal = random.choice(SpadesIndices)

    # Get offset values for suit.
    suitOffset = random.sample(range(0, 4), 3)
        
    draw1 = usedDeck[tripleVal + suitOffset[0]]
    draw2 = usedDeck[tripleVal + suitOffset[1]]
    draw3 = usedDeck[tripleVal + suitOffset[2]]

    # Remove the value that has the pair from deck (4 cards)
    usedDeck = remove_items(usedDeck, draw1[0], 'numberOnly')

    draw4 = random.choice(usedDeck)

    # Remove the value that has the pair from deck (4 cards)
    usedDeck = remove_items(usedDeck, draw4[0], 'numberOnly')

    draw5 = random.choice(usedDeck)
    
    q = Question()
    q.name = "Three of a Kind"
    q.questionText = (    
        f'What are the chances of drawing a 5-hand Poker hand with ' + 
        f'the {draw1[0]} of {draw1[1]}, ' + 
        f'the {draw2[0]} of {draw2[1]}, ' +
        f'the {draw3[0]} of {draw3[1]}, ' +
        f'the {draw4[0]} of {draw4[1]}, and ' +
        f'the {draw5[0]} of {draw5[1]}?'
    )
    q.answer = PokerHandProb.THREE_KIND.value
    q.difficulty = 5
    q.numInputs = 0
    saveNewQuestion(q)
    
def fourOfAKind(deck):
    usedDeck = deck.copy()
    SpadesIndices = []

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))
        
    # Get a random value from the spades cards using index.
    tripleVal = random.choice(SpadesIndices)

    # Get offset values for suit.
    suitOffset = random.sample(range(0, 4), 3)
        
    draw1 = usedDeck[tripleVal + suitOffset[0]]
    draw2 = usedDeck[tripleVal + suitOffset[1]]
    draw3 = usedDeck[tripleVal + suitOffset[2]]

    # Remove the value that has the pair from deck (4 cards)
    usedDeck = remove_items(usedDeck, draw1[0], 'numberOnly')

    draw4 = random.choice(usedDeck)

    # Remove the value that has the pair from deck (4 cards)
    usedDeck = remove_items(usedDeck, draw4[0], 'numberOnly')

    draw5 = random.choice(usedDeck)
    
    q = Question()
    q.name = "Four of a Kind"
    q.questionText = (    
        f'What are the chances of drawing a 5-hand Poker hand with ' + 
        f'the {draw1[0]} of {draw1[1]}, ' + 
        f'the {draw2[0]} of {draw2[1]}, ' +
        f'the {draw3[0]} of {draw3[1]}, ' +
        f'the {draw4[0]} of {draw4[1]}, and ' +
        f'the {draw5[0]} of {draw5[1]}?'
    )
    q.answer = PokerHandProb.FOUR_KIND.value
    q.difficulty = 5
    q.numInputs = 0
    saveNewQuestion(q)

def straight(deck):
    usedDeck = deck.copy()
    SpadesIndices = []

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))
        
    # Get a random value from the spades cards using index.
    midValueIndex = SpadesIndices.index(random.choice(SpadesIndices[2:11]))


    # Get offset values for suit.
    suitOffset = []
    for i in range(5):
        suitOffset.append(random.choice(range(0, 4)))
        
    draw1 = usedDeck[SpadesIndices[midValueIndex-2] + suitOffset[0]]
    draw2 = usedDeck[SpadesIndices[midValueIndex-1] + suitOffset[1]]
    draw3 = usedDeck[SpadesIndices[midValueIndex] + suitOffset[2]]
    draw4 = usedDeck[SpadesIndices[midValueIndex+1] + suitOffset[3]]
    draw5 = usedDeck[SpadesIndices[midValueIndex+2] + suitOffset[4]]
    
    q = Question()
    q.name = "Straight"
    q.questionText = (    
        f'What are the chances of drawing a 5-hand Poker hand with ' + 
        f'the {draw1[0]} of {draw1[1]}, ' + 
        f'the {draw2[0]} of {draw2[1]}, ' +
        f'the {draw3[0]} of {draw3[1]}, ' +
        f'the {draw4[0]} of {draw4[1]}, and ' +
        f'the {draw5[0]} of {draw5[1]}?'
    )
    q.answer = PokerHandProb.STRAIGHT.value
    q.difficulty = 5
    q.numInputs = 0
    saveNewQuestion(q)
    
def straightFlush(deck):
    usedDeck = deck.copy()
    SpadesIndices = []

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))
        
    # Get a random value from the spades cards using index.
    midValueIndex = SpadesIndices.index(random.choice(SpadesIndices[2:11]))


    # Get offset value for suit.
    suitOffset = random.choice(range(0, 4))
        
    draw1 = usedDeck[SpadesIndices[midValueIndex-2] + suitOffset]
    draw2 = usedDeck[SpadesIndices[midValueIndex-1] + suitOffset]
    draw3 = usedDeck[SpadesIndices[midValueIndex] + suitOffset]
    draw4 = usedDeck[SpadesIndices[midValueIndex+1] + suitOffset]
    draw5 = usedDeck[SpadesIndices[midValueIndex+2] + suitOffset]
    
    q = Question()
    q.name = "Straight Flush"
    q.questionText = (    
        f'What are the chances of drawing a 5-hand Poker hand with ' + 
        f'the {draw1[0]} of {draw1[1]}, ' + 
        f'the {draw2[0]} of {draw2[1]}, ' +
        f'the {draw3[0]} of {draw3[1]}, ' +
        f'the {draw4[0]} of {draw4[1]}, and ' +
        f'the {draw5[0]} of {draw5[1]}?'
    )
    q.answer = PokerHandProb.STRAIGHT_FLUSH.value
    q.difficulty = 5
    q.numInputs = 0
    saveNewQuestion(q)

''' HELPER START '''
# To help detect straight in flush function. This will be used using the indices in SpadesIndices
def isConsecutive(nums):
    if len(nums) < 1: 
        return False 
    min_val = min(nums) 
    max_val = max(nums) 
    if max_val - min_val + 1 == len(nums): 
        for i in range(len(nums)): 
            if nums[i] < 0: 
                j = -nums[i] - min_val 
            else: 
                j = nums[i] - min_val 
            if nums[j] > 0: 
                nums[j] = -nums[j] 
            else: 
                return False 
        return True 
    return False
''' HELPER END '''
 
def flush(deck):
    usedDeck = deck.copy()
    SpadesIndices = []
    SpadeValueIndices = []
    isFlush = True

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))

    # To check if it is a straight flush
    # It's very efficient because there's only 9 possibilities that the hand is a straight
    while isFlush:
        SpadeValueIndices = random.sample(range(0, len(SpadesIndices)), 5)
        isFlush = isConsecutive(SpadeValueIndices)


    # Get offset value for suit.
    suitOffset = random.choice(range(0, 4))
        
    draw1 = usedDeck[SpadesIndices[SpadeValueIndices[0]] + suitOffset]
    draw2 = usedDeck[SpadesIndices[SpadeValueIndices[1]] + suitOffset]
    draw3 = usedDeck[SpadesIndices[SpadeValueIndices[2]] + suitOffset]
    draw4 = usedDeck[SpadesIndices[SpadeValueIndices[3]] + suitOffset]
    draw5 = usedDeck[SpadesIndices[SpadeValueIndices[4]] + suitOffset]
    
    q = Question()
    q.name = "Flush"
    q.questionText = (    
        f'What are the chances of drawing a 5-hand Poker hand with ' + 
        f'the {draw1[0]} of {draw1[1]}, ' + 
        f'the {draw2[0]} of {draw2[1]}, ' +
        f'the {draw3[0]} of {draw3[1]}, ' +
        f'the {draw4[0]} of {draw4[1]}, and ' +
        f'the {draw5[0]} of {draw5[1]}?'
    )
    q.answer = PokerHandProb.FLUSH.value
    q.difficulty = 5
    q.numInputs = 0
    saveNewQuestion(q)
    
def royalFlush(deck):
    usedDeck = deck.copy()
    SpadesIndices = []

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))
        
    # Get offset value for suit.
    suitOffset = random.choice(range(0, 4))
        
    draw1 = usedDeck[SpadesIndices[0] + suitOffset]
    draw2 = usedDeck[SpadesIndices[12] + suitOffset]
    draw3 = usedDeck[SpadesIndices[11] + suitOffset]
    draw4 = usedDeck[SpadesIndices[10] + suitOffset]
    draw5 = usedDeck[SpadesIndices[9] + suitOffset]
    
    q = Question()
    q.name = "Royal Flush"
    q.questionText = (    
        f'What are the chances of drawing a 5-hand Poker hand with ' + 
        f'the {draw1[0]} of {draw1[1]}, ' + 
        f'the {draw2[0]} of {draw2[1]}, ' +
        f'the {draw3[0]} of {draw3[1]}, ' +
        f'the {draw4[0]} of {draw4[1]}, and ' +
        f'the {draw5[0]} of {draw5[1]}?'
    )
    q.answer = PokerHandProb.ROYAL_FLUSH.value
    q.difficulty = 5
    q.numInputs = 0
    saveNewQuestion(q)
    
def fullHouse(deck):
    usedDeck = deck.copy()
    SpadesIndices = []

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))
        
    # Get two random values from the spades cards using index
    pairValueIndices = random.sample((SpadesIndices), 2)

    # Get Pair Cards 1
    pairIndices1 = random.sample(range(pairValueIndices[0], pairValueIndices[0] + 4), 3)
    draw1 = usedDeck[pairIndices1[0]]
    draw2 = usedDeck[pairIndices1[1]]
    draw3 = usedDeck[pairIndices1[2]]

    # Get Pair Cards 2
    pairIndices2 = random.sample(range(pairValueIndices[1], pairValueIndices[1] + 4), 2)
    draw4 = usedDeck[pairIndices2[1]]
    draw5 = usedDeck[pairIndices2[0]]
    
    q = Question()
    q.name = "Full House"
    q.questionText = (    
        f'What are the chances of drawing a 5-hand Poker hand with ' + 
        f'the {draw1[0]} of {draw1[1]}, ' + 
        f'the {draw2[0]} of {draw2[1]}, ' +
        f'the {draw3[0]} of {draw3[1]}, ' +
        f'the {draw4[0]} of {draw4[1]}, and ' +
        f'the {draw5[0]} of {draw5[1]}?'
    )
    q.answer = PokerHandProb.FULL_HOUSE.value
    q.difficulty = 5
    q.numInputs = 0
    saveNewQuestion(q)
