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

    def get_score_card_for_category(self, category_name):
        '''Get the scorecard for a given category'''
        return next((cat for cat in self.score_card if cat['name'] == category_name), None)

    def choose_category_to_score(self, best_match=None):
        '''Record the score for the current roll'''
        # 
        self.display_scorecard()
        if best_match is not None:
            best_match = self.get_score_card_for_category(best_match)
            print(f"Your best match is {best_match['name']} with a score of {best_match['score']}")
            use_best_input = False
            while use_best_input is False:
                use_best = input(f"Do you want to use {best_match['name']}?")
                if use_best.lower() == 'y':
                    return best_match
                if use_best.lower() == 'n':
                    self.display_scorecard()
                    category_number = int(input("Enter the number of the category you want to score: "))
                    return self.get_score_card_for_category(category_number)
                else:
                    print("Invalid input. Please enter 'y' or 'n'")
        else:
            category_number = int(input("Enter the number of the category you want to score: "))
            return self.get_score_card_for_category(category_number)
        
    def record_score(self, category):
        # Figure out how to record the score after the turn
        self.score_card[category['number']-1]['score'] = category['score']
        return
        
    def detect_dice_roll(self):
        roll = self.dice
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

    def calculate_best_category_to_play(self, matches):
        '''Take in category matches and look at the currently scored categories and determine the best match based on the best strategy for yahtzee'''
        available_categories = []
        for match in matches:
            for category in self.score_card:
                if category['score'] is None and category['name'] == match:
                    available_categories.append(match)
        
        categories_in_order = ["yahtzee", "large Straight", "full House", "small Straight", "four-of-a-kind", "three-of-a-kind", "sixes", "fives", "fours", "threes", "twos", "ones", "chance"]
        for category in categories_in_order:
            if category in available_categories:
                # If the category is Yahtzee
                if category == "Yahtzee":
                    return category
                # If the category is a kind or a straight
                elif "Four-of-a-kind" in category:
                    return category
                # If the category is a Large straight
                elif "Large Straight" in category:
                    return category
                # If the category is a full house
                elif category == "Full House":
                    return category
                # If the category is a small straight
                elif category.endswith('s'):
                    return category
                elif category == "Chance":
                    return category

    def get_score_of_roll(self, category):
        # Find the scores of the matches and return scores
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
        input_text_length = len(input)                                    
        input_int = [int(i) for i in input]
        if len(input_text_length) != len(input_int):
            print("Invalid input!")
            return False
        for i in input_int:
            if i not in range(1, 6):
                print("Invalid input!")
                return False
        return True

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
            for i in range(3):
                print(f"Roll {i + 1}...")
                while i < 2:  # if it's not the last roll
                    print(f"Your roll: {self.dice}")
                    # Print out the best match and score
                    categories = self.detect_dice_roll()
                    best_match = self.calculate_best_category_to_play(categories)
                    score = self.get_score_of_roll(best_match)
                    print(f"Best match: {best_match} with a score of {score}")

                    # Ask the user if they want to keep the roll
                    keep_roll_input = False
                    while keep_roll_input == False:
                        keep_roll = input("Do you want to keep this roll? (y/n): ")
                        if self.validate_text_input(keep_roll) == False:
                            break
                        if keep_roll.lower() == 'n':
                            reroll_input = False
                            while reroll_input == False:
                                reroll = input("Enter the numbers of the dice you want to reroll, separated by spaces: ")
                                if self.validate_int_input(reroll) == False:
                                    break
                                else:
                                    reroll = reroll.split()
                                    self.reroll_dice(reroll)
                                    reroll_input = True
                                    break
                                # the problem here is that they need to break out to the outer loop
                            break
                        if keep_roll.lower() == 'y':
                            keep_roll_input = True
                            break
            self.calculate_score()
            self.turn += 1
        print("Game over!")
    
if __name__ == '__main__':
    yahtzee = Yahtzee()
    yahtzee.play_game() 