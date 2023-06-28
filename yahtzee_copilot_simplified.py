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
            {'name': 'three of a kind', 'score': None, 'number': 7, 'section': 2},
            {'name': 'four of a kind', 'score': None, 'number': 8, 'section': 2},
            {'name': 'full house', 'score': None, 'number': 9, 'section': 2},
            {'name': 'small straight', 'score': None, 'number': 10, 'section': 2},
            {'name': 'large straight', 'score': None, 'number': 11, 'section': 2},
            {'name': 'yahtzee', 'score': None, 'number': 12, 'section': 2},
            {'name': 'chance', 'score': None, 'number': 13, 'section': 3},
        ]
        self.turn = 0
        # self.current_matches = []
        # self.current_matches_scores = []
        #self.current_roll_best_match = {'category': None, 'score': None, 'number': None}

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

    def record_score(self, category):
        '''Record the score for the current turn'''
        score = self.get_score_of_roll(category)
        for cat in self.score_card:
            if cat['name'] == category:
                cat['score'] = score
                break
        self.display_scorecard()
        return
    
    def choose_category_to_score(self):
        '''Record the score for the current roll'''
        matches = self.detect_dice_roll()
        # remove any matches that have already been scored
        matches = [match for match in matches if match not in [cat['name'] for cat in self.score_card if cat['score'] is not None]]

        print("\nChoose a category to score:")
        for i, match in enumerate(matches):
            print(f"{i+1}. {match.title()}")  # assuming match is a string

        while True:
            choice = input("Enter the number of your choice: ")
            if choice.isdigit() and 0 < int(choice) <= len(matches):
                choice = int(choice) - 1
                self.record_score(matches[choice])
                return
            else:
                print("Invalid input. Please enter a number corresponding to your choice.")
        
    def detect_dice_roll(self):
        roll = sorted(self.dice)
        counts = Counter(roll)
        categories = []

        # Ones through Sixes
        for i in range(1, 7):
            if i in counts:
                if i == 1:
                    categories.append("ones")
                elif i == 2:
                    categories.append("twos")
                elif i == 3:
                    categories.append("threes")
                elif i == 4:
                    categories.append("fours")
                elif i == 5:
                    categories.append("fives")
                elif i == 6:
                    categories.append("sixes")

        # Three-of-a-kind, Four-of-a-kind, and Yahtzee
        for num, count in counts.items():
            if count == 3:
                categories.append("three-of-a-kind")
            if count == 4:
                categories.append("four-of-a-kind")
            if count == 5:
                categories.append("yahtzee")
        
        # Full House
        if set(counts.values()) == {2, 3}:
            categories.append("full house")
        
        # Small and Large Straight
        if any(set(roll[i:i+4]) in [{1, 2, 3, 4}, {2, 3, 4, 5}, {3, 4, 5, 6}] for i in range(len(roll)-3)):
            categories.append("small straight")
        if set(roll) == {1, 2, 3, 4, 5} or set(roll) == {2, 3, 4, 5, 6}:
            categories.append("large straight")
        
        # Chance
        categories.append("chance")
        return categories

    def get_score_of_roll(self, category):
        # Find the scores of the matches and return scores
        # This function assumes a single category is passed in from the detect_dice_roll function and choose_category_to_score function
        score_map = {
            'ones': self.dice.count(1),
            'twos': self.dice.count(2) * 2,
            'threes': self.dice.count(3) * 3,
            'fours': self.dice.count(4) * 4,
            'fives': self.dice.count(5) * 5,
            'sixes': self.dice.count(6) * 6,
            'three-of-a-kind': sum(self.dice),
            'four-of-a-kind': sum(self.dice),
            'full house': 25,
            'small straight': 30,
            'large straight': 40,
            'yahtzee': 50,
            'chance': sum(self.dice)
        }
        return score_map[category]

    def validate_num_input(self, input):
        # Remove spaces from the input
        input = input.replace(" ", "")
        counts = Counter(input)
        if all(count == 1 for count in counts.values()) is False:
            print("Invalid input! Contains duplicate numbers.")
            return False
        if len(input) > 5:
            print("Invalid input! Too many numbers.")
            return False
        input_int = []
        for i in input:
            if not i.isdigit():
                print("Invalid input! Contains non-digit characters.")
                return False
            input_int.append(int(i))
        for i in input_int:
            if i not in range(1, 6):
                print("Invalid input! Number not in range 1-5.")
                return False
        return input_int


    def validate_text_input(self, input):
        if input.lower() not in ['y', 'n']:
            print("Invalid input!")
            return False
        return True

    def play_game(self):
        '''Play the game'''
        while self.turn < 13:
            print(f"\nTurn {self.turn + 1} of 13:")
            print(f"First rolling of the dice...")
            self.roll_all_dice()
            skip_reroll = False
            for i in range(3):
                if skip_reroll == True:
                    break
                print(f"Roll {i + 1}...")
                while i < 3:  # if it's not the last roll
                    print(f"Your roll: {self.dice}")
                    # Print out the best match and score
                    categories = self.detect_dice_roll()
                    print(f"Possible categories: {categories}")

                    # Ask the user if they want to keep the roll
                    keep_roll_input = False
                    if i == 2:
                        break
                    while keep_roll_input == False:
                        keep_roll = input("Do you want to keep this roll? (y/n): ")
                        if self.validate_text_input(keep_roll) == False:
                            continue
                        if keep_roll.lower() == 'n':
                            reroll_input = False
                            while reroll_input == False:
                                reroll = input("Enter the numbers of the dice you want to reroll, separated by spaces: ")
                                reroll = self.validate_num_input(reroll)
                                if reroll == False:
                                    continue
                                else:
                                    for die_index in reroll:
                                        self.roll_die(int(die_index)-1)
                                    reroll_input = True
                                    i += 1
                                    break
                            break
                        if keep_roll.lower() == 'y':
                            keep_roll_input = True
                            skip_reroll = True
                            break
                        
                    break
                
            self.choose_category_to_score()
            self.turn += 1
        print("Game over!")
    
if __name__ == '__main__':
    yahtzee = Yahtzee()
    yahtzee.play_game() 