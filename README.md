# Handy Brawl in terminal

The  application (play_a_game.py) is simulating the Handy Brawl game (2022) made by Igor Zuber.
Download the cards and the rules from the files section at https://boardgamegeek.com/boardgame/362692/handy-brawl.

This application is a hobby project by Milan Žroutík <zroutik@e.email>.

The game is represented as a flow of turns.
If one possible turn is evaluated, that turn is made automatically and requires no user interaction.
Otherwise, possible outcome variants are offered to the user to choose from by entering a number.

At the current version, only cards for the warrior and the ogre character (in the range from 1 to 9) are properly implemented.

The deck is visualised by a list of number+character+life triplets.
Cards from top to bottom are displayed from right to left.
The cards design and available actions on sections are not displayed within the application.
Therefore, a card overview is required to play the game properly.
Actions leading to the resulting outcome variant are listed.  

Example of the displayed outcome variant:
- 1 :  3D⬓  7B◼  2C◻  6C◻  1A◼  5A◼  9D⬓  8D⬓  4A◼  (damage, 2)

Oth the other hand, the hash for a deck is a string consisting of alternating integers and characters [A, B, C, D].
and represents the list of cards from top to bottom.
Card numbers are represented by integers and the sections of the cards by letters.
Lower case letters and spaces are accepted.
Omitted letters represent the section 'A' of the card. (Spaces between numbers are mandatory in such a case.)

Valid hash examples:

- 5A9A4A8A3A7A2A6A1A
- 5A 9A 4A 8A 3A 7A 2A 6A 1A
- 5 9 4 8 3 7 2 6 1

The user shall enter the starting deck as a hash, top card first. 
