class Game:
    def __init__(self):
        self.deck = DeckFunctions.getFullDeck()
        print("Original")
        print(self.deck)
        self.deck.shuffle()
        print('Shuffled')
        print(self.deck)