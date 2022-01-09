class Card:
    
    Symbols = ['2','3','4','5','6','7','8','9','10','J','Q','K','A']

    def __init__(self,symbol):
        if symbol not in Card.Symbols:
            raise ValueError(f'{symbol} is not a valid Card symbol')
        self.symbol = symbol
        self.value = Card.Symbols.index(symbol)
        
    def __str__(self):
        return f'[{self.symbol} ({self.value})]'
    def __repr__(self):
        return str(self)
        
    # Comparators
    def __lt__(self, other):
        return self.value < other.value
    def __le__(self, other):
        return self.value <= other.value
    def __eq__(self, other):
        return self.value == other.value
    def __ne__(self, other):
        return self.value != other.value
    def __gt__(self, other):
        return self.value > other.value
    def __ge__(self, other):
        return self.value >= other.value
    def __hash__(self):
        return hash(repr(self))