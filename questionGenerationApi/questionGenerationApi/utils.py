from .models import Question
from fractions import Fraction
import random


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
    # chances of getting a single value
    usedDeck = deck.copy()
    for i in range(13):
        draw = random.choice(usedDeck)
        q = Question()
        q.name = "Single Card Number Only"
        q.questionText = f'What are the chances of drawing a {draw[0]} from a single deck of cards'
        q.answer = round(4/52, 2)
        q.difficulty = 1
        q.numInputs = 0
        saveNewQuestion(q)
        usedDeck = remove_items(usedDeck, draw[0], 'numberOnly')

    return


def singleCard(deck):
    usedDeck = deck.copy()
    for i in range(52):
        draw = random.choice(deck)
        q = Question()
        q.name = "Single Card"
        q.questionText = f'What are the chances of drawing a {draw[0]} of {draw[1]} from a single deck of cards'
        q.answer = round(1/52, 2)
        q.difficulty = 1
        q.numInputs = 0
        saveNewQuestion(q)
        # add to a used list so we dont repeat
        usedDeck = remove_items(usedDeck, draw, 'numberAndSuite')


def multipleCards(deck):
    usedDeck = deck.copy()
    for numCards in range(2, 4):
        for i in range(52):
            draw = random.choice(deck)
            q = Question()
            q.name = "Multiple Card"
            q.questionText = f'What are the chances of drawing {numCards} {draw[0]}\'s from a 5 card draw'
            if (numCards == 2):
                q.answer = 42.25
            elif (numCards == 3):
                q.answer = 2.11
            elif (numCards == 4):
                q.answer = 0.024
            q.difficulty = numCards  # two of a kind is easier than 4 of a kind
            q.numInputs = 0
            saveNewQuestion(q)
            # add to a used list so we dont repeat
            usedDeck = remove_items(usedDeck, draw, 'numberAndSuite')
