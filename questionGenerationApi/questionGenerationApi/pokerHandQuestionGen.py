from .models import Question
import random
from .utils import saveNewQuestion, remove_items
import collections

# These are the hard-coded probabilities for each poker hand type.
ROYAL_FLUSH = 1.5390771693292702e-06
STRAIGHT_FLUSH = 1.3851694523963431e-05
FOUR_KIND = 0.00024009603841536616
FULL_HOUSE = 0.0014405762304921968
FLUSH = 0.001965401545233478
STRAIGHT = 0.003924646781789639
THREE_KIND = 0.0035214085634253703
TWO_PAIR = 0.0475390156062425
ONE_PAIR = 1.625915857154571e-07
HIGH_CARD = 0.5011773940345369

# Helper to check if a hand exists to avoid duplicates.
def handExists(src, target):
    for elem in src:
        if collections.Counter(elem) == collections.Counter(target) :
            return True

# HIGH CARD START
def highCard(deck, nQuestions=1):
    counter = nQuestions
    if(counter > 1302540):
        counter = 1302540
        
    usedDeck = deck.copy()
    SpadesIndices = []
    randomVals = []
    hands = []

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))
    
    while(counter > 0):
        # Get a random values from the spades cards using index.
        randomVals = random.sample(SpadesIndices, 5)

        draw1 = usedDeck[random.choice(range(randomVals[0], randomVals[0]+4))],
        draw2 = usedDeck[random.choice(range(randomVals[1], randomVals[1]+4))],
        draw3 = usedDeck[random.choice(range(randomVals[2], randomVals[2]+4))],
        draw4 = usedDeck[random.choice(range(randomVals[3], randomVals[3]+4))],
        draw5 = usedDeck[random.choice(range(randomVals[4], randomVals[4]+4))],
 
        hand = [draw1, draw2, draw3, draw4, draw5]
        
        if(not handExists(hands, hand)):
            hands.append(hand)
            counter = counter -1
            
    for hand in hands:
        draw1 = hand[0]
        draw2 = hand[1]
        draw3 = hand[2]
        draw4 = hand[3]
        draw5 = hand[4]
    
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
        q.answer = HIGH_CARD
        q.difficulty = 5
        q.numInputs = 0
        saveNewQuestion(q)
# HIGH CARD END

#ONE PAIR START
def onePair(deck, nQuestions=1):
    counter = nQuestions
    if(counter > 1098240):
        counter = 1098240
        
    usedDeck = deck.copy()
    SpadesIndices = []
    hands = []

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))
    
    while(counter > 0):
        # Get a random value from the spades cards using index.
        pairValueIndex = random.choice(SpadesIndices)

        # Get Pair Cards
        pairIndices = random.sample(range(pairValueIndex, pairValueIndex + 3), 2)
        draw1 = usedDeck[pairIndices[0]]
        draw2 = usedDeck[pairIndices[1]]

        # Remove the value that has the pair from deck (4 cards)
        usedDeck = remove_items(usedDeck, draw1[0], 'numberOnly')

        # Get three random cards from usedDeck
        remainingIndices = random.sample(range(0, len(usedDeck)), 3)
        draw3 = usedDeck[remainingIndices[0]]
        draw4 = usedDeck[remainingIndices[1]]
        draw5 = usedDeck[remainingIndices[2]]
        
        hand = [draw1, draw2, draw3, draw4, draw5]
        
        if(not handExists(hands, hand)):
            hands.append(hand)
            counter = counter - 1
        
        usedDeck = deck.copy()
    
    for hand in hands:
        draw1 = hand[0]
        draw2 = hand[1]
        draw3 = hand[2]
        draw4 = hand[3]
        draw5 = hand[4]
        
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
        q.answer = ONE_PAIR
        q.difficulty = 4
        q.numInputs = 0
        saveNewQuestion(q)
# ONE PAIR END

# TWO PAIR START
def twoPair(deck, nQuestions=1):
    counter = nQuestions
    if(counter > 123552):
        counter = 123552
        
    usedDeck = deck.copy()
    SpadesIndices = []
    hands = []

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))
    
    while(counter > 0):
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
        
        hand = [draw1, draw2, draw3, draw4, draw5]
        
        if(not handExists(hands, hand)):
            hands.append(hand)
            counter = counter - 1
        
        usedDeck = deck.copy()
    
    for hand in hands:
        draw1 = hand[0]
        draw2 = hand[1]
        draw3 = hand[2]
        draw4 = hand[3]
        draw5 = hand[4]
    
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
        q.answer = TWO_PAIR
        q.difficulty = 5
        q.numInputs = 0
        saveNewQuestion(q)
# TWO PAIR END

# THREE OF A KIND START 
def threeOfAKind(deck, nQuestions=1):
    counter = nQuestions
    if(counter > 54912):
        counter = 54912
        
    usedDeck = deck.copy()
    SpadesIndices = []
    hands = []

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))
    
    while(counter > 0): 
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
        
        hand = [draw1, draw2, draw3, draw4, draw5]
        
        if(not handExists(hands, hand)):
            hands.append(hand)
            counter = counter - 1
        
        usedDeck = deck.copy()
        
    for hand in hands:
        draw1 = hand[0]
        draw2 = hand[1]
        draw3 = hand[2]
        draw4 = hand[3]
        draw5 = hand[4]
        
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
        q.answer = THREE_KIND
        q.difficulty = 5
        q.numInputs = 0
        saveNewQuestion(q)
# THREE OF A KIND END

def fourOfAKind(deck, nQuestions=1):
    counter = nQuestions
    if(counter > 624):
        counter = 624
        
    usedDeck = deck.copy()
    SpadesIndices = []
    hands = []

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))
    
    while(counter > 0):  
        # Get a random value from the spades cards using index.
        tripleVal = random.choice(SpadesIndices)

        # Get offset values for suit.
        suitOffset = random.sample(range(0, 4), 4)
            
        draw1 = usedDeck[tripleVal + suitOffset[0]]
        draw2 = usedDeck[tripleVal + suitOffset[1]]
        draw3 = usedDeck[tripleVal + suitOffset[2]]
        draw4 = usedDeck[tripleVal + suitOffset[3]]

        # Remove the value that has the pair from deck (4 cards)
        usedDeck = remove_items(usedDeck, draw1[0], 'numberOnly')

        draw5 = random.choice(usedDeck)
        
        hand = [draw1, draw2, draw3, draw4, draw5]
        
        if(not handExists(hands, hand)):
            hands.append(hand)
            counter = counter - 1
        
        usedDeck = deck.copy()
    
    for hand in hands:
        draw1 = hand[0]
        draw2 = hand[1]
        draw3 = hand[2]
        draw4 = hand[3]
        draw5 = hand[4]
    
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
        q.answer = FOUR_KIND
        q.difficulty = 5
        q.numInputs = 0
        saveNewQuestion(q)
# FOUR OF A KIND END

# STRAIGHT START
def straight(deck, nQuestions=1):
    counter = nQuestions
    if(counter > 10200):
        counter = 10200
        
    usedDeck = deck.copy()
    SpadesIndices = []
    hands = []

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))
    
    while(counter > 0):  
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
        
        hand = [draw1, draw2, draw3, draw4, draw5]
        
        if(not handExists(hands, hand)):
            hands.append(hand)
            counter = counter - 1
        
    for hand in hands:
        draw1 = hand[0]
        draw2 = hand[1]
        draw3 = hand[2]
        draw4 = hand[3]
        draw5 = hand[4]
    
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
        q.answer = STRAIGHT
        q.difficulty = 5
        q.numInputs = 0
        saveNewQuestion(q)
# STRAIGHT END

# STRAIGHT FLUSH START   
def straightFlush(deck, nQuestions=1):
    counter = nQuestions
    if(counter > 36):
        counter = 36
        
    usedDeck = deck.copy()
    SpadesIndices = []
    hands = []

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))
    
    while(counter > 0):  
        # Get a random value from the spades cards using index.
        midValueIndex = SpadesIndices.index(random.choice(SpadesIndices[2:11]))
        
        # Get offset value for suit.
        suitOffset = random.choice(range(0, 4))
            
        draw1 = usedDeck[SpadesIndices[midValueIndex-2] + suitOffset]
        draw2 = usedDeck[SpadesIndices[midValueIndex-1] + suitOffset]
        draw3 = usedDeck[SpadesIndices[midValueIndex] + suitOffset]
        draw4 = usedDeck[SpadesIndices[midValueIndex+1] + suitOffset]
        draw5 = usedDeck[SpadesIndices[midValueIndex+2] + suitOffset]
        
        hand = [draw1, draw2, draw3, draw4, draw5]

        if(not handExists(hands, hand)):
            hands.append(hand)
            counter = counter - 1
        
    for hand in hands:
        draw1 = hand[0]
        draw2 = hand[1]
        draw3 = hand[2]
        draw4 = hand[3]
        draw5 = hand[4]
    
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
        q.answer = STRAIGHT_FLUSH
        q.difficulty = 5
        q.numInputs = 0
        saveNewQuestion(q)
# STRAIGHT FLUSH END

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

# FLUSH START
def flush(deck, nQuestions=1):
    counter = nQuestions
    if(counter > 5108):
        counter = 5108
        
    usedDeck = deck.copy()
    SpadesIndices = []
    SpadeValueIndices = []
    hands = []
    
    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))

    while(counter > 0):     
        isFlush = True
        
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
        
        hand = [draw1, draw2, draw3, draw4, draw5]

        if(not handExists(hands, hand)):
            hands.append(hand)
            counter = counter - 1
        
    for hand in hands:
        draw1 = hand[0]
        draw2 = hand[1]
        draw3 = hand[2]
        draw4 = hand[3]
        draw5 = hand[4]
    
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
        q.answer = FLUSH
        q.difficulty = 5
        q.numInputs = 0
        saveNewQuestion(q)
# FLUSH END   

# ROYAL FLUSH START
def royalFlush(deck, nQuestions=1):
    counter = nQuestions
    if(counter > 4):
        counter = 4
        
    usedDeck = deck.copy()
    SpadesIndices = []
    hands = []

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))
        
    while(counter > 0):     
        # Get offset value for suit.
        suitOffset = random.choice(range(0, 4))
            
        draw1 = usedDeck[SpadesIndices[0] + suitOffset]
        draw2 = usedDeck[SpadesIndices[12] + suitOffset]
        draw3 = usedDeck[SpadesIndices[11] + suitOffset]
        draw4 = usedDeck[SpadesIndices[10] + suitOffset]
        draw5 = usedDeck[SpadesIndices[9] + suitOffset]
        
        hand = [draw1, draw2, draw3, draw4, draw5]

        if(not handExists(hands, hand)):
            hands.append(hand)
            counter = counter - 1
        
    for hand in hands:
        draw1 = hand[0]
        draw2 = hand[1]
        draw3 = hand[2]
        draw4 = hand[3]
        draw5 = hand[4]
    
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
        q.answer = ROYAL_FLUSH
        q.difficulty = 5
        q.numInputs = 0
        saveNewQuestion(q)
    
def fullHouse(deck, nQuestions=1):
    counter = nQuestions
    if(counter > 3744):
        counter = 3744
    
    usedDeck = deck.copy()
    SpadesIndices = []
    hands = []

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))
   
    while(counter > 0):          
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
        
        hand = [draw1, draw2, draw3, draw4, draw5]

        if(not handExists(hands, hand)):
            hands.append(hand)
            counter = counter - 1
        
    for hand in hands:
        draw1 = hand[0]
        draw2 = hand[1]
        draw3 = hand[2]
        draw4 = hand[3]
        draw5 = hand[4]
    
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
        q.answer = FULL_HOUSE
        q.difficulty = 5
        q.numInputs = 0
        saveNewQuestion(q)
# ROYAL FLUSH END