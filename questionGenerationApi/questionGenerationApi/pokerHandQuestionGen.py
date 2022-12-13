from .models import Question
import random
from .utils import saveNewQuestion

# These are the hard-coded probabilities for each poker hand type that are in decimal form, not percentages.
# calcAllPossible(): comb(52, 5) or 2,598,960 

# (comb(4, 1))/calcAllPossible()
ROYAL_FLUSH = 1.5390771693292702e-06

#((comb(10, 1) * comb(4, 1)) - comb(4, 1))/calcAllPossible()
STRAIGHT_FLUSH = 1.3851694523963431e-05

# (comb(13, 1) * comb(4, 4) * comb(12, 1) * comb(4, 1))/calcAllPossible()
FOUR_KIND = 0.00024009603841536616

# (comb(13, 1) * comb(4, 3) * comb(12, 1) * comb(4, 2))/calcAllPossible()
FULL_HOUSE = 0.0014405762304921968

# ((comb(13, 5) * comb(4, 1)) - (comb(10, 1) * comb(4, 1)))/calcAllPossible()
FLUSH = 0.001965401545233478

# ((comb(10, 1) * pow(comb(4, 1), 5)) -  (comb(10, 1) * comb(4, 1)))/calcAllPossible()
STRAIGHT = 0.003924646781789639

# (comb(13, 1) * comb(4, 3) * comb(11, 1) * pow(comb(4, 1), 2))/calcAllPossible()
THREE_KIND = 0.0035214085634253703

# (comb(13, 2) * pow(comb(4, 2), 2) * comb(11, 1) * comb(4, 1))/calcAllPossible()
TWO_PAIR = 0.0475390156062425

# (calcTwoOfAKind())/calcAllPossible()
ONE_PAIR = 1.625915857154571e-07

# ((comb(13, 5) - comb(10, 1)) * (pow(comb(4, 1), 5) - comb(4, 1)))/calcAllPossible()
HIGH_CARD = 0.5011773940345369

# HIGH CARD START
def highCard(deck, nQuestions=1):
    counter = nQuestions
    if(counter > 1302540):
        counter = 1302540

    usedDeck = deck.copy()
    SpadesIndices = []
    randomVals = []
    hands = set()

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))

    while(counter > 0):
        # Get a random values from the spades cards using index.
        randomVals = random.sample(SpadesIndices, 5)
        hand = frozenset([
            usedDeck[random.randrange(randomVals[0], randomVals[0]+4)],
            usedDeck[random.randrange(randomVals[1], randomVals[1]+4)],
            usedDeck[random.randrange(randomVals[2], randomVals[2]+4)],
            usedDeck[random.randrange(randomVals[3], randomVals[3]+4)],
            usedDeck[random.randrange(randomVals[4], randomVals[4]+4)],
        ])

        if(not hand in hands):
            hands.add(hand)
            counter = counter - 1

    for hand in hands:
        vals = list(hand)
        draw1 = vals[0]
        draw2 = vals[1]
        draw3 = vals[2]
        draw4 = vals[3]
        draw5 = vals[4]

        q = Question()
        q.name = "Poker Questions Set: High Card"
        q.questionText = (
            f'What are the chances of drawing a five-card poker hand that is a high card (no pair)? For example: ' +
            f'the {draw1[0]} of {draw1[1]}, ' +
            f'the {draw2[0]} of {draw2[1]}, ' +
            f'the {draw3[0]} of {draw3[1]}, ' +
            f'the {draw4[0]} of {draw4[1]}, and ' +
            f'the {draw5[0]} of {draw5[1]}.'
        )
        q.answer = HIGH_CARD
        q.difficulty = 1
        q.numInputs = 0
        saveNewQuestion(q)
# HIGH CARD END

# ONE PAIR START
def onePair(deck, nQuestions=1):
    counter = nQuestions
    if(counter > 1098240):
        counter = 1098240

    usedDeck = deck.copy()
    SpadesIndices = []
    hands = set()

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))

    while(counter > 0):
        # Get four random values from the spades cards using index
        valueIndices = random.sample((SpadesIndices), 4)

        # Get Pair Cards 1 Index
        pairIndices1 = random.sample(
            range(valueIndices[0], valueIndices[0] + 4), 2)

        # Get Random Remaining Cards Indices
        randomCard1 = random.randrange(valueIndices[1], valueIndices[1] + 4)
        randomCard2 = random.randrange(valueIndices[2], valueIndices[2] + 4)
        randomCard3 = random.randrange(valueIndices[3], valueIndices[3] + 4)

        hand = frozenset([
            usedDeck[pairIndices1[0]],
            usedDeck[pairIndices1[1]],
            usedDeck[randomCard1],
            usedDeck[randomCard2],
            usedDeck[randomCard3]
        ])

        if(not hand in hands):
            hands.add(hand)
            counter = counter - 1

    for hand in hands:
        vals = list(hand)
        draw1 = vals[0]
        draw2 = vals[1]
        draw3 = vals[2]
        draw4 = vals[3]
        draw5 = vals[4]

        q = Question()
        q.name = "Poker Questions Set: One Pair"
        q.questionText = (
            f'What are the chances of drawing a five-card poker hand that is a one pair? For example: ' +
            f'the {draw1[0]} of {draw1[1]}, ' +
            f'the {draw2[0]} of {draw2[1]}, ' +
            f'the {draw3[0]} of {draw3[1]}, ' +
            f'the {draw4[0]} of {draw4[1]}, and ' +
            f'the {draw5[0]} of {draw5[1]}.'
        )
        q.answer = ONE_PAIR
        q.difficulty = 2
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
    hands = set()

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))

    while(counter > 0):
        # Get three random values from the spades cards using index
        valueIndices = random.sample((SpadesIndices), 3)

        # Get Pair Cards 1 Indices
        pairIndices1 = random.sample(
            range(valueIndices[0], valueIndices[0] + 4), 2)

        # Get Pair Cards 2 Indices
        pairIndices2 = random.sample(
            range(valueIndices[1], valueIndices[1] + 4), 2)

        # Get Random Card Index
        randomCard1 = random.randrange(valueIndices[2], valueIndices[2] + 4)

        hand = frozenset([
            usedDeck[pairIndices1[0]],
            usedDeck[pairIndices1[1]],
            usedDeck[pairIndices2[0]],
            usedDeck[pairIndices2[1]],
            usedDeck[randomCard1]
        ])

        if(not hand in hands):
            hands.add(hand)
            counter = counter - 1

    for hand in hands:
        vals = list(hand)
        draw1 = vals[0]
        draw2 = vals[1]
        draw3 = vals[2]
        draw4 = vals[3]
        draw5 = vals[4]

        q = Question()
        q.name = "Poker Questions Set: Two Pair"
        q.questionText = (
            f'What are the chances of drawing a five-card poker hand that is a two pair? For example: ' +
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
    hands = set()

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))

    while(counter > 0):
        # Get three random values from the spades cards using index
        valueIndices = random.sample((SpadesIndices), 3)

        # Get triple Cards Indices
        tripleIndices = random.sample(
            range(valueIndices[0], valueIndices[0] + 4), 3)

        # Get Random Remaining Cards Indices
        randomCard1 = random.randrange(valueIndices[1], valueIndices[1] + 4)
        draw4 = usedDeck[randomCard1]

        randomCard2 = random.randrange(valueIndices[2], valueIndices[2] + 4)

        hand = frozenset([
            usedDeck[tripleIndices[0]],
            usedDeck[tripleIndices[1]],
            usedDeck[tripleIndices[2]],
            usedDeck[randomCard1],
            usedDeck[randomCard2]
        ])

        if(not hand in hands):
            hands.add(hand)
            counter = counter - 1

    for hand in hands:
        vals = list(hand)
        draw1 = vals[0]
        draw2 = vals[1]
        draw3 = vals[2]
        draw4 = vals[3]
        draw5 = vals[4]

        q = Question()
        q.name = "Poker Questions Set: Three of a Kind"
        q.questionText = (
            f'What are the chances of drawing a five-card poker hand that is a three of a kind? For example: ' +
            f'the {draw1[0]} of {draw1[1]}, ' +
            f'the {draw2[0]} of {draw2[1]}, ' +
            f'the {draw3[0]} of {draw3[1]}, ' +
            f'the {draw4[0]} of {draw4[1]}, and ' +
            f'the {draw5[0]} of {draw5[1]}?'
        )
        q.answer = THREE_KIND
        q.difficulty = 3
        q.numInputs = 0
        saveNewQuestion(q)
# THREE OF A KIND END

# FOUR OF A KIND START
def fourOfAKind(deck, nQuestions=1):
    counter = nQuestions
    if(counter > 624):
        counter = 624

    usedDeck = deck.copy()
    SpadesIndices = []
    hands = set()

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))

    while(counter > 0):
        # Get three random values from the spades cards using index
        valueIndices = random.sample((SpadesIndices), 2)

        # Get Quadruple Cards Indices
        quadIndices = random.sample(
            range(valueIndices[0], valueIndices[0] + 4), 4)

        # Get Random Remaining Card Index
        randomCard1 = random.randrange(valueIndices[1], valueIndices[1] + 4)

        hand = frozenset([
            usedDeck[quadIndices[0]],
            usedDeck[quadIndices[1]],
            usedDeck[quadIndices[2]],
            usedDeck[quadIndices[3]],
        ])

        if(not hand in hands):
            hands.add(hand)
            counter = counter - 1

    for hand in hands:
        vals = list(hand)
        draw1 = vals[0]
        draw2 = vals[1]
        draw3 = vals[2]
        draw4 = vals[3]

        q = Question()
        q.name = "Poker Questions Set: Four of a Kind"
        q.questionText = (
            f'What are the chances of drawing a five-card poker hand that is a four of a kind? For example: ' +
            f'the {draw1[0]} of {draw1[1]}, ' +
            f'the {draw2[0]} of {draw2[1]}, ' +
            f'the {draw3[0]} of {draw3[1]}, and ' +
            f'the {draw4[0]} of {draw4[1]}?'
            # i just removed this one, and changed answer to reflect specific 4 of a kind
        )
        q.answer = FOUR_KIND
        q.difficulty = 4
        q.numInputs = 0
        saveNewQuestion(q)
# FOUR OF A KIND END

# STRAIGHT START
def straight(deck, nQuestions=1):
    counter = nQuestions
    if(counter > 10200):
        counter = 10200

    usedDeck = deck.copy()
    # Handle cases for Ace as highest card
    usedDeck.append(usedDeck[0])
    usedDeck.append(usedDeck[1])
    usedDeck.append(usedDeck[2])
    usedDeck.append(usedDeck[3])
    SpadesIndices = []
    hands = set()

    # Get all the indices of all spades cards.
    for card in usedDeck[::4]:
        SpadesIndices.append(usedDeck.index(card))

    while(counter > 0):
        # Get a random value from the spades cards using index.
        midValueIndex = SpadesIndices.index(random.choice(SpadesIndices[2:12]))

        # Get offset values for suit.
        suitOffset = [0, 0, 0, 0, 0]
        while suitOffset[0] == suitOffset[1] == suitOffset[2] == suitOffset[3] == suitOffset[4]:
            for i in range(5):
                suitOffset[i] = random.randrange(0, 4)

        hand = frozenset([
            usedDeck[SpadesIndices[midValueIndex-2] + suitOffset[0]],
            usedDeck[SpadesIndices[midValueIndex-1] + suitOffset[1]],
            usedDeck[SpadesIndices[midValueIndex] + suitOffset[2]],
            usedDeck[SpadesIndices[midValueIndex+1] + suitOffset[3]],
            usedDeck[SpadesIndices[midValueIndex+2] + suitOffset[4]],
        ])

        if(not hand in hands):
            hands.add(hand)
            counter = counter - 1

    for hand in hands:
        vals = list(hand)
        draw1 = vals[0]
        draw2 = vals[1]
        draw3 = vals[2]
        draw4 = vals[3]
        draw5 = vals[4]

        q = Question()
        q.name = "Poker Questions Set: Straight"
        q.questionText = (
            f'What are the chances of drawing a five-card poker hand that is a straight?  For example: ' +
            f'the {draw1[0]} of {draw1[1]}, ' +
            f'the {draw2[0]} of {draw2[1]}, ' +
            f'the {draw3[0]} of {draw3[1]}, ' +
            f'the {draw4[0]} of {draw4[1]}, and ' +
            f'the {draw5[0]} of {draw5[1]}.'
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
    hands = set()

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))

    while(counter > 0):
        # Get a random value from the spades cards using index.
        midValueIndex = SpadesIndices.index(random.choice(SpadesIndices[2:11]))

        # Get offset value for suit.
        suitOffset = random.randrange(0, 4)

        hand = frozenset([
            usedDeck[SpadesIndices[midValueIndex-2] + suitOffset],
            usedDeck[SpadesIndices[midValueIndex-1] + suitOffset],
            usedDeck[SpadesIndices[midValueIndex] + suitOffset],
            usedDeck[SpadesIndices[midValueIndex+1] + suitOffset],
            usedDeck[SpadesIndices[midValueIndex+2] + suitOffset],
        ])

        if(not hand in hands):
            hands.add(hand)
            counter = counter - 1

    for hand in hands:
        vals = list(hand)
        draw1 = vals[0]
        draw2 = vals[1]
        draw3 = vals[2]
        draw4 = vals[3]
        draw5 = vals[4]

        q = Question()
        q.name = "Poker Questions Set: Straight Flush"
        q.questionText = (
            f'What are the chances of drawing a five-card poker hand that is a straight flush? For example: ' +
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
# There's a defect where 0 is not accounted for, so there's a fix for that

def isConsecutive(input):
    nums = []
    for number in input:
        nums.append(number + 1)

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
    hands = set()

    # Get all the indices of all spades cards.
    for card in usedDeck[::4]:
        SpadesIndices.append(usedDeck.index(card))

    while(counter > 0):
        isOtherFlush = True

        # To check if it is a straight flush or royal flush
        # It's very efficient because there's only 9 possibilities that the hand is a straight
        # flush if accounting just the values.
        while isOtherFlush:
            # 1287 Possibilities
            SpadeValueIndices = random.sample(range(0, len(SpadesIndices)), 5)
            SpadeValueIndicesSet = set(SpadeValueIndices)

            # Check if royal flush (1 possibility) -> 1286
            if(SpadeValueIndicesSet == set([0, 9, 10, 11, 12])):
                continue
            # Check if straight flush (9 possibilities) -> 1277
            elif(isConsecutive(SpadeValueIndices)):
                continue
            else:
                isOtherFlush = False

        # Get offset value for suit.
        suitOffset = random.randrange(0, 4)

        hand = frozenset([
            usedDeck[SpadesIndices[SpadeValueIndices[0]] + suitOffset],
            usedDeck[SpadesIndices[SpadeValueIndices[1]] + suitOffset],
            usedDeck[SpadesIndices[SpadeValueIndices[2]] + suitOffset],
            usedDeck[SpadesIndices[SpadeValueIndices[3]] + suitOffset],
            usedDeck[SpadesIndices[SpadeValueIndices[4]] + suitOffset],
        ])

        if(not hand in hands):
            hands.add(hand)
            counter = counter - 1

    for hand in hands:
        vals = list(hand)
        draw1 = vals[0]
        draw2 = vals[1]
        draw3 = vals[2]
        draw4 = vals[3]
        draw5 = vals[4]

        q = Question()
        q.name = "Poker Questions Set: Flush"
        q.questionText = (
            f'What are the chances of drawing five-card poker hand that is a flush? For example: ' +
            f'the {draw1[0]} of {draw1[1]}, ' +
            f'the {draw2[0]} of {draw2[1]}, ' +
            f'the {draw3[0]} of {draw3[1]}, ' +
            f'the {draw4[0]} of {draw4[1]}, and ' +
            f'the {draw5[0]} of {draw5[1]}'
        )
        q.answer = FLUSH
        q.difficulty = 6
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
    hands = set()

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))

    while(counter > 0):
        # Get offset value for suit.
        suitOffset = random.randrange(0, 4)

        hand = frozenset([
            usedDeck[SpadesIndices[0] + suitOffset],
            usedDeck[SpadesIndices[12] + suitOffset],
            usedDeck[SpadesIndices[11] + suitOffset],
            usedDeck[SpadesIndices[10] + suitOffset],
            usedDeck[SpadesIndices[9] + suitOffset],
        ])

        if(not hand in hands):
            hands.add(hand)
            counter = counter - 1

    for hand in hands:
        vals = list(hand)
        draw1 = vals[0]
        draw2 = vals[1]
        draw3 = vals[2]
        draw4 = vals[3]
        draw5 = vals[4]

        q = Question()
        q.name = "Poker Questions Set: Royal Flush"
        q.questionText = (
            f'What are the chances of drawing a five-card poker hand with a royal flush? For example: ' +
            f'the {draw1[0]} of {draw1[1]}, ' +
            f'the {draw2[0]} of {draw2[1]}, ' +
            f'the {draw3[0]} of {draw3[1]}, ' +
            f'the {draw4[0]} of {draw4[1]}, and ' +
            f'the {draw5[0]} of {draw5[1]}?'
        )
        q.answer = ROYAL_FLUSH
        q.difficulty = 6
        q.numInputs = 0
        saveNewQuestion(q)


def fullHouse(deck, nQuestions=1):
    counter = nQuestions
    if(counter > 3744):
        counter = 3744

    usedDeck = deck.copy()
    SpadesIndices = []
    hands = set()

    # Get all the indices of all spades cards.
    for card in deck[::4]:
        SpadesIndices.append(usedDeck.index(card))

    while(counter > 0):
        # Get two random values indices from the spades cards using index
        pairValueIndices = random.sample((SpadesIndices), 2)

        # Get Triple Cards Indices
        tripleIndices = random.sample(
            range(pairValueIndices[0], pairValueIndices[0] + 4), 3)

        # Get Pair Cards Indices
        pairIndices = random.sample(
            range(pairValueIndices[1], pairValueIndices[1] + 4), 2)

        hand = frozenset([
            usedDeck[tripleIndices[0]],
            usedDeck[tripleIndices[1]],
            usedDeck[tripleIndices[2]],
            usedDeck[pairIndices[0]],
            usedDeck[pairIndices[1]],
        ])

        if(not hand in hands):
            hands.add(hand)
            counter = counter - 1

    for hand in hands:
        vals = list(hand)
        draw1 = vals[0]
        draw2 = vals[1]
        draw3 = vals[2]
        draw4 = vals[3]
        draw5 = vals[4]

        q = Question()
        q.name = "Poker Questions Set: Full House"
        q.questionText = (
            f'What are the chances of drawing a five-card poker hand that is a full house? For example: ' +
            f'the {draw1[0]} of {draw1[1]}, ' +
            f'the {draw2[0]} of {draw2[1]}, ' +
            f'the {draw3[0]} of {draw3[1]}, ' +
            f'the {draw4[0]} of {draw4[1]}, and ' +
            f'the {draw5[0]} of {draw5[1]}.'
        )
        q.answer = FULL_HOUSE
        q.difficulty = 5
        q.numInputs = 0
        saveNewQuestion(q)
# ROYAL FLUSH END
