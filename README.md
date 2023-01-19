# handy-brawl

This application is a simulating the Handy Brawl game by Igor Zuber.
Download the cards and the rules from the files section at https://boardgamegeek.com/boardgame/362692/handy-brawl.

This application is a hobby type of project by Milan Žroutík <zroutik@e.email>.

The game is represented as a flow of turns.
Due to the structure of the deck and the action selection at the face of the top card, some turns require no user inetraction.
For others, variants of outcome are offered to the user to choose from.

The hash for a deck is a string consisting of alternating integers and characters [A, B, C, D].
Card numbers are represented by integers and the faces of the cards by letters.
Lower case letters are accepted. Spaces are accepted.
Missing letters represent the face 'A' of the card.
    (Spaces between numbers are required in such case.)

Use card numbers for the warrior and the ogre characters, in the range from 1 to 9.
Valid hash examples:

- 1A6A2A7A3A8A4A9A5A
- 1A 6A 2A 7A 3A 8A 4A 9A 5A
- 1 6 2 7 3 8 4 9 5

The decks are represented similarly by a list of number+character+life items.
Therefore, a card overview is required to play the game properly.
The cards design and available actions on faces are not displayed within the application.
