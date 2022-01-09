class DeckFunctions:
    def getFullDeck():
        deck = Deck()
        print(deck)
        for symbol in Card.Symbols:
            for i in range(4):
                deck.push(Card(symbol))
        return deck