import pydealer as pd
from pydealer.const import POKER_RANKS
#Class to represent all possible question types
class Generator:
    #individual class for a question type
    class cardProbability:

        def one_pair():
            deck = pd.Deck(ranks=POKER_RANKS)
            card1 = deck.deal()
            print(card1)


