from Deck import Deck
from DeckFunctions import DeckFunctions


class Game:
    def __init__(self,numPlayers=2):
        self.deck = DeckFunctions.getFullDeck()
        self.players = [Deck() for _ in range(numPlayers)]
        self.pool = Deck()
        self.stage = Deck()
        self.deal()
        self.gameOver = False

    def deal(self):
        self.deck.shuffle()
        currentPlayerIndex = 0
        while not self.deck.isEmpty():
            self.players[currentPlayerIndex].push(self.deck.pop())
            currentPlayerIndex = (currentPlayerIndex+1)%len(self.players)

    def runTurn(self):
        summary = ""
        try:
            self.pool.pushAll([p.pop() for p in self.players])
            self.stage.pushAll(self.pool.cards)
            summary+=f'Stage: {self.stage}\n'

            winningCard = max(self.stage.cards)
            summary+=f'Winning card: {winningCard}\n'
        
            while(len([c for c in self.stage.cards if c == winningCard])>1):
                summary+=f'Tie\n'
                self.stage = Deck()
                #TODO Restrict to only players with winning cards
                for p in self.players:
                    draws = [p.pop(),p.pop(),p.pop()]
                    self.pool.pushAll(draws)
                    self.stage.push(draws[-1])
                    summary+=f'Player {self.players.index(p)} draws {draws}\n'
                # HACK Cards end up in reverse-player order, so reverse the stage to match up indexes
                self.stage.cards.reverse()
                summary+=f'New Pool: {self.pool}\n'
                summary+=f'New Stage: {self.stage}\n'

                winningCard = max(self.stage.cards)
                summary+=f'Winning card: {winningCard}\n'
            
            winningPlayerIndex = self.stage.cards.index(winningCard)
            self.players[winningPlayerIndex].pushAll(self.pool.popAll())
            self.stage = Deck()

            summary+=f'Player {winningPlayerIndex} wins the round\n'
        except:
            self.gameOver = True
        finally:
            return summary
    
    def play(self):
        summary=''
        roundNumber=1
        while not self.gameOver:
            summary+=f'{{Round {roundNumber}}}\n'
            for p in self.players:
                summary+=f'Player {self.players.index(p)}: {p}\n\n'
            summary+=self.runTurn()
            summary+='\n'
            roundNumber+=1          
        winner = next(p for p in self.players if len(p.cards) > 0)
        summary+=f'Player {self.players.index(winner)} wins!'
        return summary
