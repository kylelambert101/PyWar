from Card import Card
from Deck import Deck


class DeckFunctions:
    def getFullDeck():
        deck = Deck()
        for symbol in Card.Symbols:
            for i in range(4):
                deck.push(Card(symbol))
        return deck