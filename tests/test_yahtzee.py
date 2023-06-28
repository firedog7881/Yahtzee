import pytest
from yahtzee import Yahtzee

@pytest.fixture
def yahtzee():
    return Yahtzee()

def test_roll_die(yahtzee):
    yahtzee.roll_all_dice()
    saved_values = yahtzee.dice.copy()
    
    yahtzee.roll_die(12)
    changed = False
    if saved_values[0] != yahtzee.dice[0] or saved_values[1] != yahtzee.dice[1]:
        changed = True
    
    if not changed:
        yahtzee.roll_die(12)
        if saved_values[0] != yahtzee.dice[0] or saved_values[1] != yahtzee.dice[1]:
            changed = True
    
    if not changed:
        yahtzee.roll_die(12)
        if saved_values[0] != yahtzee.dice[0] or saved_values[1] != yahtzee.dice[1]:
            changed = True
    
    assert changed, "The values of the first two dice did not change after rolling three times."

def test_roll_all_dice(yahtzee):
    yahtzee.roll_all_dice()
    assert len(yahtzee.dice) == 5
    assert all(1 <= die <= 6 for die in yahtzee.dice)

def test_get_score_of_roll(yahtzee):
    yahtzee.dice = [1, 2, 3, 4, 5]
    assert yahtzee.get_score_of_roll('ones') == 1
    assert yahtzee.get_score_of_roll('twos') == 2
    assert yahtzee.get_score_of_roll('threes') == 3
    assert yahtzee.get_score_of_roll('fours') == 4
    assert yahtzee.get_score_of_roll('fives') == 5
    assert yahtzee.get_score_of_roll('sixes') == 0
    assert yahtzee.get_score_of_roll('three-of-a-kind') == 15
    assert yahtzee.get_score_of_roll('four-of-a-kind') == 15
    assert yahtzee.get_score_of_roll('full house') == 25
    assert yahtzee.get_score_of_roll('small straight') == 30
    assert yahtzee.get_score_of_roll('large straight') == 40
    assert yahtzee.get_score_of_roll('yahtzee') == 0
    assert yahtzee.get_score_of_roll('chance') == 15

def test_validate_num_input(yahtzee):
    # Valid inputs
    assert yahtzee.validate_num_input("12345") == [1, 2, 3, 4, 5]
    assert yahtzee.validate_num_input("5 4 3 2 1") == [5, 4, 3, 2, 1]
    assert yahtzee.validate_num_input("345") == [3, 4, 5]
    assert yahtzee.validate_num_input("145") == [1, 4, 5]
    assert yahtzee.validate_num_input("12") == [1, 2]
    
    # Invalid inputs
    assert yahtzee.validate_num_input("112") == False  # Contains duplicate numbers
    assert yahtzee.validate_num_input("123456") == False  # Too many numbers
    assert yahtzee.validate_num_input("1a3b5") == False  # Contains non-digit characters
    assert yahtzee.validate_num_input("67890") == False  # Number not in range 1-5


def test_validate_text_input(yahtzee):
    assert yahtzee.validate_text_input('y') == True
    assert yahtzee.validate_text_input('Y') == True
    assert yahtzee.validate_text_input('n') == True
    assert yahtzee.validate_text_input('N') == True
    # Invalid inputs
    assert yahtzee.validate_text_input("yes") == False  # Non-letter
    assert yahtzee.validate_text_input("no") == False  # Non-letter
    assert yahtzee.validate_text_input("1") == False  # Non-letter character
    assert yahtzee.validate_text_input("@") == False  # Non-letter character

def test_detect_dice_roll(yahtzee):
    # Sample dice rolls for each category
    dice_ones = [1, 2, 3, 4, 5]
    dice_twos = [2, 2, 3, 4, 5]
    dice_threes = [1, 2, 3, 3, 5]
    dice_fours = [1, 2, 4, 4, 4]
    dice_fives = [1, 2, 3, 4, 5]
    dice_sixes = [6, 6, 6, 6, 6]
    dice_three_of_a_kind = [1, 1, 1, 2, 3]
    dice_four_of_a_kind = [4, 4, 4, 4, 2]
    dice_full_house = [3, 3, 3, 2, 2]
    dice_small_straight = [1, 2, 3, 4, 6]
    dice_large_straight = [2, 3, 4, 5, 6]
    dice_yahtzee = [4, 4, 4, 4, 4]
    dice_chance = [2, 3, 4, 5, 6]

    # Assert each category is detected in the corresponding dice roll
    assert 'ones' in yahtzee.detect_dice_roll(dice_ones)
    assert 'twos' in yahtzee.detect_dice_roll(dice_twos)
    assert 'threes' in yahtzee.detect_dice_roll(dice_threes)
    assert 'fours' in yahtzee.detect_dice_roll(dice_fours)
    assert 'fives' in yahtzee.detect_dice_roll(dice_fives)
    assert 'sixes' in yahtzee.detect_dice_roll(dice_sixes)
    assert 'three-of-a-kind' in yahtzee.detect_dice_roll(dice_three_of_a_kind)
    assert 'four-of-a-kind' in yahtzee.detect_dice_roll(dice_four_of_a_kind)
    assert 'full house' in yahtzee.detect_dice_roll(dice_full_house)
    assert 'small straight' in yahtzee.detect_dice_roll(dice_small_straight)
    assert 'large straight' in yahtzee.detect_dice_roll(dice_large_straight)
    assert 'yahtzee' in yahtzee.detect_dice_roll(dice_yahtzee)
    assert 'chance' in yahtzee.detect_dice_roll(dice_chance)


def test_record_score(yahtzee):
    yahtzee.dice = [1, 2, 3, 4, 5]
    yahtzee.record_score('ones')
    assert yahtzee.score_card[0]['score'] == 1

def test_choose_category_to_score(yahtzee):
    yahtzee.dice = [1, 2, 3, 4, 5]
    yahtzee.choose_category_to_score()
    assert yahtzee.score_card[0]['score'] == 1
