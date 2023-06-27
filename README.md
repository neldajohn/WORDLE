# WORDLE
This is a simplified version of the New York Times Wordle game that I created for fun. I wanted to replicate the basic idea of the game without using graphics. 

## Usage
This game allows players to choose to either play with the computer (single-player) or with a friend (duo player). 
* Single Player: The game scrapes 5, 6, and 7-letter words from the internet and chooses one for the player
* Duo Player: Each player takes turns setting a secret word for the other

## Scoring
- After users select the length of the words they want to guess (word_length), they will have (word_length + 1) guesses available before the game ends.
- With each guess, their guess will be displayed in a matrix table, where if the letters appear:
      - Green: correct letter, correct position
      - Yellow: correct letter, wrong position
      - Red: wrong letter, wrong position
- The score will decrease by 2 until it reaches 0 and the next player plays or the game ends.
