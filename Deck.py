import random

class Deck:
    def __init__(self,cards=[]):
        self.cards = cards
    def __str__(self):
        return str(self.cards)
    def __repr__(self):
        return str(self)
    def pop(self):
        return self.cards.pop()
    def push(self,card):
        self.cards.append(card)
    def pushAll(self, cards):
        for card in cards:
            self.cards.append(card)
    def isEmpty(self):
        return len(self.cards) == 0
    def shuffle(self):
        random.shuffle(self.cards)
