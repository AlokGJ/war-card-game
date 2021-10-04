from helpers import values

class Card():
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " + self.suit