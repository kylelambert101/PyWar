from Game import Game

g = Game()

for i in range(5):
    for p in g.players:
        print(f'Player {g.players.index(p)}: {p}\n')
    print(g.runTurn())
    print()

