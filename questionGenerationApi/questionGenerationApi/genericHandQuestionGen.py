from .models import Question
import random
from .utils import saveNewQuestion, remove_items
from math import comb, pow
        
'''
What is the probability that a five-card poker hand does not contain the {Value} of {Suit}?
'''
def notContainsCardInHand(deck, nQuestions=1):
    counter = nQuestions
    usedDeck = deck.copy()
    repertoire = set()
    
    while counter > 0:
        n = random.randrange(1, 5)
        cardsSet = frozenset(random.sample(usedDeck, n))
        cards = list(cardsSet)
        question = ''
        
        if(not cardsSet in repertoire):
            repertoire.add(cardsSet)
            question = f'What is the probability that a five-card poker hand does not contain the {cards[0][0]} of {cards[0][1]}'
            
            if(n == 2):
                question += f' and {cards[1][0]} of {cards[1][1]}?'
            elif(n > 3):
                for i in range(2, n):
                    if(i == n-1):
                        question += f', and {cards[i][0]} of {cards[i][1]}?'
                    else:
                        question += f', {cards[i][0]} of {cards[i][1]}'
            else:
                question += '?'
                
            counter -= 1
            
            q = Question()
            q.name = "Not Contain Cards in Poker Hand"
            q.questionText = question
            q.answer = 1 - comb(52-(5-n), 5-(5-n))/comb(52,5)
            q.difficulty = 5
            q.numInputs = 0
            saveNewQuestion(q)

'''
Contains Value of Suit ([randrange(1,5)] * (&& Value of Suit)) (Multiple)
'''
# I do not know the max number for this one, but I know it's way too many...
def containCardsInHand(deck, nQuestions=1):
    counter = nQuestions
    usedDeck = deck.copy()
    repertoire = set()
    
    while counter > 0:
        n = random.randrange(1, 5)
        cardsSet = frozenset(random.sample(usedDeck, n))
        cards = list(cardsSet)
        question = ''
        
        if(not cardsSet in repertoire):
            repertoire.add(cardsSet)
            answer = 0
            question = f'What is the probability that a five-card poker hand contains the {cards[0][0]} of {cards[0][1]}'
            
            if(n == 2):
                question += f' and {cards[1][0]} of {cards[1][1]}?'
            elif(n > 3):
                for i in range(2, n):
                    if(i == n-1):
                        question += f', and {cards[i][0]} of {cards[i][1]}?'
                    else:
                        question += f', {cards[i][0]} of {cards[i][1]}'
            else:
                question += '?'
                
            counter -= 1
            
            q = Question()
            q.name = "Contains Cards in Poker Hand"
            q.questionText = question
            q.answer = comb(52-n, 5-n)/comb(52,5)
            q.difficulty = 5
            q.numInputs = 0
            saveNewQuestion(q)
            
'''
What is the probability that a five-card poker hand contains exactly one {Value}?
'''
def exactlyOneValueInHand(deck, nQuestions=1):
    counter = nQuestions
    if(counter > 13):
        counter = 13
        
    usedDeck = deck.copy()
    valueIndex = []
    
    for card in deck[::4]:
        valueIndex.append(usedDeck.index(card))

    for i in range(counter):
        index = random.choice(valueIndex)
        valueIndex.remove(index)
        card = usedDeck[index]
        
        q = Question()
        q.name = 'Exactly One Value in Poker Hand'
        q.questionText = (    
            f'What is the probability that a five-card poker hand contains exactly one {card[0]} card?'
        )
        q.answer = 3243/10829
        q.difficulty = 5
        q.numInputs = 0
        saveNewQuestion(q)  


'''
What is the probability that a five-card poker hand contains at least one {Value}?
'''
def atLeastOneValueInHand(deck, nQuestions=1):
    counter = nQuestions
    if(counter > 13):
        counter = 13
        
    usedDeck = deck.copy()
    valueIndex = []
    
    for card in deck[::4]:
        valueIndex.append(usedDeck.index(card))

    for i in range(counter):
        index = random.choice(valueIndex)
        valueIndex.remove(index)
        card = usedDeck[index]
        
        q = Question()
        q.name = 'Exactly One Value in Poker Hand'
        q.questionText = (    
            f'What is the probability that a five-card poker hand contains at least one {card[0]} card?'
        )
        q.answer = 18472/54145
        q.answer = 1/13
        q.difficulty = 5
        q.numInputs = 0
        saveNewQuestion(q)  
