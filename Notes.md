This is just a staging area for ideas. It can be deleted once I have some code down.

Wouldn't it be cool to simulate the card game war in Python and run some repeat simulations of games to see if anything interesting pops up?

Rules of the game:

- 2 or more players
- Each player gets an even fraction of the deck (1/#players)
- Each player puts down a card in a round
  - Higher card value wins
  - Winnning player collects all cards and adds to their deck
  - Matching cards causes both players to add two nonplayed cards to the pool and then a third, with that card being the new battling card.

Entities that could be useful classes:

- Card
  - Symbol
  - Numeric Value
  - **eq** comparison method
- Deck
  - Collection of cards
  - Pop and push capabilities
  - Check for emptiness
- Player
  - Has a deck
  - Has a status (active/inactive)
- Pool
  - Is a deck
- Game
  - Has list of player decks
  - Has a single pool deck
  - Responsible for transferring cards between decks
  - Responsible for performing actions based on game rules
  - Turn Steps:
    - Draw for all players
    - Compare cards
    - Winner -> transfer cards between players and pool
    - Stalemate -> Draw more cards and re-draw, start over
    - Check count of players' cards to determine if player stays active.
  - Game continues until only one player is active
