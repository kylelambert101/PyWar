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
        if self.isEmpty():
            raise RuntimeError('No more cards')
        return self.cards.pop()
    def popAll(self):
        tmp = Deck()
        for i in range(len(self.cards)):
            tmp.push(self.pop())
        return tmp.cards
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
