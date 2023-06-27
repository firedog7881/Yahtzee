'''Create a CLI version of Yahtzee'''
import random
from collections import Counter
from time import sleep
import re

class Yahtzee:
    def __init__(self):
        self.dice = [0, 0, 0, 0, 0]
        self.roll_all_dice()
        self.score_card = [
            {'name': 'ones', 'score': None, 'number': 1, 'section': 1},
            {'name': 'twos', 'score': None, 'number': 2, 'section': 1},
            {'name': 'threes', 'score': None, 'number': 3, 'section': 1},
            {'name': 'fours', 'score': None, 'number': 4, 'section': 1},
            {'name': 'fives', 'score': None, 'number': 5, 'section': 1},
            {'name': 'sixes', 'score': None, 'number': 6, 'section': 1},
            {'name': 'three_of_a_kind', 'score': None, 'number': 7, 'section': 2},
            {'name': 'four_of_a_kind', 'score': None, 'number': 8, 'section': 2},
            {'name': 'full_house', 'score': None, 'number': 9, 'section': 2},
            {'name': 'small_straight', 'score': None, 'number': 10, 'section': 2},
            {'name': 'large_straight', 'score': None, 'number': 11, 'section': 2},
            {'name': 'yahtzee', 'score': None, 'number': 12, 'section': 2},
            {'name': 'chance', 'score': None, 'number': 13, 'section': 3},
        ]
        self.turn = 0

    def display_scorecard(self):
        '''Display the scorecard to the user'''
        print("\nScorecard:")
        for category in self.score_card:
            score = category['score']
            if score is None:
                score = 'Not scored yet'
            print(f"{category['number']}. {category['name'].title()}: {score}")

    def roll_die(self, die_index):
        '''Roll a single die'''
        self.dice[die_index] = random.randint(1, 6)

    def roll_all_dice(self):
        '''Roll all dice'''
        for i in range(5):
            self.roll_die(i)

    def record_score(self, best_match=None):
        '''Record the score for the current roll'''
        self.display_scorecard()
        if best_match is not None:
            print(f"Your best match is {best_match['name']}")
            use_best = input(f"Do you want to score {best_match['name']}?")
            if use_best.lower() == 'y':
                category_number = best_match['number']
        else:
            category_number = int(input("Enter the number of the category you want to score: "))

        category = next((cat for cat in self.score_card if cat['number'] == category_number), None)
        if category is None or category['score'] is not None:
            print("Invalid category number or category has already been scored!")
            return
    
    
    def detect_dice_roll(self, pop_chance=False):
        '''Using the input of self.dice detect what categories the dice roll matches using regex and then figure out the score for each category and return the category and score of the best score'''
        # Create a list of the dice roll
        dice_roll = self.dice
        # Convert the list to a string
        dice_roll = ''.join(str(i) for i in dice_roll)
        # Detect the dice roll

        
        # Create a list to hold the matches
        matches = []

        return matches

    def calculate_best_category_to_play(self, matches):
        '''Take in category matches and look at the currently scored categories and determine the best match based on the best strategy for yahtzee'''




    def some_other_function(self):
        # # Map the score of the category to tell which category is the best match
        # score_map = {
        #     'ones': self.dice.count(1),
        #     'twos': self.dice.count(2) * 2,
        #     'threes': self.dice.count(3) * 3,
        #     'fours': self.dice.count(4) * 4,
        #     'fives': self.dice.count(5) * 5,
        #     'sixes': self.dice.count(6) * 6,
        #     'three_of_a_kind': (Counter(self.dice).values() >= 3) * 3,
        #     'four_of_a_kind': (Counter(self.dice).values() >= 3) * 4,
        #     'full_house': 25,
        #     'small_straight': 30,
        #     'large_straight': 40,
        #     'yahtzee': 50,
        #     'chance': sum(self.dice)
        # }
        
        # # Find the scores of the matches and return the best match and score
        # scores = [score_map[match] for match in matches]
        # best_match = matches[scores.index(max(scores))]
        # score = max(scores)
        # return best_match, score

    def play_game(self):
        '''Play the game'''
        while self.turn < 13:
            print(f"\nTurn {self.turn + 1} of 13:")
            print(f"First rolling of the dice...")
            self.roll_all_dice()
            for i in range(3):
                print(f"Roll {i + 1}...")
                while i < 1:  # if it's not the last roll
                    print(f"Your roll: {self.dice}")
                    # Print out the best match and score
                    best_match, score = self.detect_dice_roll(True)
                    print(f"Best match: {best_match} with a score of {score}")
                    # Ask the user if they want to keep the roll
                    keep_roll_input = False
                    while keep_roll_input == False:
                        keep_roll = input("Do you want to keep this roll? (y/n): ")
                        if keep_roll.lower() == 'y':
                            keep_roll_input = True
                            break
                        if keep_roll.lower() == 'n':
                            reroll_input = False
                            while reroll_input == False:
                                reroll = input("Enter the numbers of the dice you want to reroll, separated by spaces (or press n to not reroll any): ")
                                if reroll.lower() == 'n':
                                    reroll_input = True
                                    break
                                else:
                                    #validate that reroll is a list of numbers between 1 and 5
                                    while reroll_input == False:
                                        isvalid = True
                                        for num in reroll.split():
                                            if not num.isdigit():
                                                print("Invalid input!")
                                                reroll = input("Enter the numbers of the dice you want to reroll: ")
                                                break
                                            # if number is not between 1 and 5, ask for input again
                                            if int(num) not in range(1, 6):
                                                print("Invalid input!")
                                                reroll = input("Enter the numbers of the dice you want to reroll: ")
                                                break
                                        if isvalid:
                                            reroll = [int(num) for num in reroll.split() if num.isdigit() and 1 <= int(num) <= 5]     
                                            for num in reroll:
                                                self.roll_die(num-1)
                                                reroll_input = True

                        else:
                            print("Invalid input!")
            self.calculate_score()
            self.turn += 1
        print("Game over!")
    
if __name__ == '__main__':
    yahtzee = Yahtzee()
    yahtzee.play_game()
                         

git config --global user.email "bmeyer24@gmail.com"
git config --global user.name "Brandon"