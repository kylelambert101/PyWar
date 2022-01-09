import random

class Deck:
    def __init__(self,cards=None):
        self.cards = cards
        if self.cards == None:
            self.cards = []
    def __str__(self):
        return str(self.cards)
    def __repr__(self):
        return str(self)
    def pop(self):
        return self.cards.pop()
    def popAll(self):
        tmp = [c for c in self.cards]
        self.cards = []
        return tmp
    def push(self,card):
        self.cards.insert(0, card)
    def pushAll(self, cards):
        for card in cards:
            self.push(card)
    def isEmpty(self):
        return len(self.cards) == 0
    def shuffle(self):
        random.shuffle(self.cards)
    def hasDuplicates(self):
        return len(self.cards) > len(set(self.cards))
