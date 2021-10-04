import random
from helpers import suits, cards
from Card import Card

class Deck:
    def __init__(self):
        self.all_cards = [Card(card, suit) for card in cards for suit in suits]
    
    def shuffle(self):
        random.shuffle(self.all_cards)
    
    def deal_one(self):
        return self.all_cards.pop()