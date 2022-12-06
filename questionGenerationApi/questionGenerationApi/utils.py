from .models import Question
from fractions import Fraction
import itertools
import random
from .pokerHandFrequencies import *

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

'''POKER HANDS'''
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

# Generates only one question
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
    remainingIndices = random.sample(range(0, 48), 3)
    draw3 = usedDeck[remainingIndices[0]]
    draw4 = usedDeck[remainingIndices[1]]
    draw5 = usedDeck[remainingIndices[2]]
    
    q = Question()
    q.name = "One Pair"
    q.questionText = f'What are the chances of drawing {draw1} {draw2} {draw3} {draw4} {draw5}?'
    q.answer = calcOnePair()/calcAllPossible()
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
    pairIndices1 = random.sample(range(pairValueIndices[0], pairValueIndices[0] + 3), 2)
    draw1 = usedDeck[pairIndices1[0]]
    draw2 = usedDeck[pairIndices1[1]]

    # Get Pair Cards 2
    pairIndices2 = random.sample(range(pairValueIndices[1], pairValueIndices[1] + 3), 2)
    draw3 = usedDeck[pairIndices2[0]]
    draw4 = usedDeck[pairIndices2[1]]

    # Remove the value that has the pair from deck (8 cards)
    usedDeck = remove_items(usedDeck, draw1[0], 'numberOnly')
    usedDeck = remove_items(usedDeck, draw3[0], 'numberOnly')
    
    # Get three random cards from usedDeck
    remainingIndices = random.sample(range(0, 44), 1)
    draw5 = usedDeck[remainingIndices[0]]
    
    q = Question()
    q.name = "Two Pair"
    q.questionText = f'What are the chances of drawing {draw1} {draw2} {draw3} {draw4} {draw5}?'
    q.answer = calcTwoPair()/calcAllPossible()
    q.difficulty = 5
    q.numInputs = 0
    saveNewQuestion(q)

# Generates many questions
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