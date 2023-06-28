# Yahtzee CLI Game

## Overview
Yahtzee CLI Game is a command-line implementation of the popular dice game Yahtzee. It allows users to play Yahtzee directly from their terminal. Roll the dice, score your combinations, and compete for the highest score!

## Features
- Roll the dice: The game automatically rolls the dice for you.
- Score combinations: Choose from various scoring categories to score your dice rolls.
- Scorecard display: See your current scores and track your progress on the scorecard.
- Automatic turn progression: The game progresses through 13 turns automatically.
- Interactive gameplay: The game prompts the user for inputs and displays information during gameplay.
- Randomized dice rolls: The dice are rolled randomly for each turn.

## Installation
1. Clone the repository: `git clone https://github.com/your-username/yahtzee-cli-game.git`
2. Navigate to the project directory: `cd yahtzee-cli-game`
3. Install the required dependencies: NO DEPENDENCIES

## Usage
1. Run the game: `python yahtzee.py`
2. Follow the prompts in the terminal to play the game.
3. Make choices by entering the corresponding numbers or letters.
4. Enjoy playing Yahtzee!

## Rules
The rules of Yahtzee can be found [here](https://www.hasbro.com/common/instruct/Yahtzee.pdf).

## Example
```
$ python yahtzee.py

Welcome to Yahtzee!

Turn 1 of 13:
First rolling of the dice...
Roll 1...
Your roll: [2, 4, 1, 6, 3]
Possible categories: ['ones', 'twos', 'threes', 'fours', 'fives', 'sixes', 'three-of-a-kind', 'four-of-a-kind', 'full house', 'small straight', 'large straight', 'yahtzee', 'chance']

Choose a category to score:
1. Ones
2. Twos
3. Threes
4. Fours
5. Fives
6. Sixes
7. Three-of-a-kind
8. Four-of-a-kind
9. Full house
10. Small straight
11. Large straight
12. Yahtzee
13. Chance

Enter the number of your choice: 4

Scorecard:
1. Ones: Not scored yet
2. Twos: Not scored yet
3. Threes: Not scored yet
4. Fours: 12
5. Fives: Not scored yet
6. Sixes: Not scored yet
7. Three-of-a-kind: Not scored yet
8. Four-of-a-kind: Not scored yet
9. Full house: Not scored yet
10. Small straight: Not scored yet
11. Large straight: Not scored yet
12. Yahtzee: Not scored yet
13. Chance: Not scored yet

Turn 2 of 13:
First rolling of the dice...
Roll 1...
Your roll: [1, 2, 4, 4, 5]
Possible categories: ['ones', 'twos', 'threes', 'fives', 'sixes', 'three-of-a-kind', 'four-of-a-kind', 'full house', 'small straight', 'large straight', 'yahtzee', 'chance']

Choose a category to score:
1. Ones
2. Twos
3. Threes
4. Fours
5. Fives
6. Sixes
7. Three-of-a-kind
8. Four-of-a-kind
