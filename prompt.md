# Documentation of AI Use for Lab 06 per Lab Instructions

## Prompts 
ME:
Title this chat Farkle

CHATGPT:
The title of this chat is now "Farkle." How can I assist you today?

ME:

Title this chat Farkle


CHATGPT:

The title of this chat is now "Farkle." How can I assist you today?

ME:

Act as though you are a software developer experienced in python. 

Build a program for two players to play the dice game Ten Thousand, sometimes known as Farkle. 

First, read through the instructions below and let me know if you have any questions about the instructions. Secondly, write the program. 

"""
Define a GameLogic class in ten_thousand/game_logic.py file.
Handle calculating score for dice roll.
Add calculate_score static method to GameLogic class.
The input to calculate_score is a tuple of integers that represent a dice roll.
The output from calculate_score is an integer representing the roll’s score according to the rules of game.
Handle rolling dice. 
Add roll_dice static method to GameLogic class.
The input to roll_dice is an integer between 1 and 6.
The output of roll_dice is a tuple with random values between 1 and 6.
The length of tuple must match the argument given to roll_dice method.
"""

CHATGPT:

Sure, I can help with that. Before we proceed with writing the program, let's ensure that I understand the rules of the game "Ten Thousand" (Farkle) and the specific requirements you've outlined.

1. **Calculate Score**: The `calculate_score` method will take a tuple of integers representing dice rolls (1 to 6) as input. Based on the game's scoring rules, this method will return the score for that roll. We'll need to know the specific scoring rules for the game.

2. **Roll Dice**: The `roll_dice` method will simulate rolling dice. It takes an integer as an input, representing the number of dice to roll. It returns a tuple with random values between 1 and 6, with the length of the tuple equal to the number of dice rolled.

Before proceeding, could you please provide the scoring rules for the game? These rules are essential to implement the `calculate_score` method correctly.

ME:
Yes, good question. These are the base methods of scoring, provided by Wikipedia
"""
Single fives are worth 50 points
Single ones are worth 100 points
Three of a kind are worth 100 points times the number rolled, except for three ones which are worth 1000 points
If four, five, or six of a kind are rolled, each additional dice doubles the amount of dice previously rolled. For example, 4 dice showing the number 3 would be 600 points and 5 dice showing the number 3 would be 1200 points
This makes the highest possible score in a single roll 8000 for six ones (1000 for three ones, after that player multiplies the roll by two for each additional one in that series of rolling.)
A straight from 1 to 6 is worth 1500 points. If a player fails to roll a straight, they may make one attempt to complete the straight. If the desired number(s) does not turn up on the next roll, that round is a "crap out" even if there are scoring dice on the table i.e. 1's or 5's.
Three pairs are worth 1000 points, for instance 2+2, 4+4, 5+5. This rule does not count if you roll a quadruple and a pair e.g. 2+2, 2+2, 6+6 unless stated otherwise (some places have their own house rules).
Full house (3 of a kind plus 2 of a kind) are worth 1,500
Typically each roll scores separately, with dice scored at the time they are rolled, so that three or more of a kind must be rolled simultaneously, and dice from later rolls do not "stack" for the higher score. In so-called progressive scoring, dice can form combinations with dice previously scored and set aside. Also to add you can not take a full house with 4 of a kind and a 2 of a kind without rolling 1 of the 4 dice to make the full house a 3 of a kind and a 2 of a kind for a full house

Example: Player 1 rolls all six dice, and chooses to score three fours for 400 points. She rolls the remaining three dice for a 2, 4, 5; the additional 4 does not multiply the previous three of a kind unless playing progressive, and she can only score 50 points for the lone 5. If she rolls two more 5's with the remaining dice, if not playing progressive they will only score 50 points each, and do not form a three of a kind with the other 5.

"""

Here is some starter code for the program
"""
from random import randint, sample
class GameLogic:

    @staticmethod
    def roll_dice(num_dice):
        return tuple(randint(1,6) for _ in range(0,num_dice))
        # or
        # return tuple(sample(range(1, 6 + 1), num_dice))
"""

Let me know if you have any other questions. 


CHATGPT:

Thank you for providing the detailed scoring rules and the starter code for the `GameLogic` class. Based on your description, I'll implement the `calculate_score` static method within the `GameLogic` class. This method will analyze the dice roll (represented as a tuple of integers) and calculate the score according to the rules you've provided.

The scoring rules are quite comprehensive, covering various scenarios such as single ones and fives, three of a kind, straights, three pairs, full house, and progressive scoring for four, five, or six of a kind. 

I'll start by implementing the `calculate_score` method. This method will handle different scoring scenarios by analyzing the counts of each dice face value in the roll. 

Let's proceed with the implementation.

The `GameLogic` class has been implemented with both the `roll_dice` and `calculate_score` methods. In the example usage, a dice roll of (1, 2, 3, 4, 5, 6) was tested, which correctly scored 1500 points, as it represents a straight from 1 to 6.

You can now use this `GameLogic` class to integrate into your Ten Thousand (Farkle) game application, handling both the rolling of dice and the calculation of scores according to the provided rules. If you have any further modifications, questions, or another part of the game you'd like to implement, feel free to ask!

```python
from random import randint
from collections import Counter

class GameLogic:
    @staticmethod
    def roll_dice(num_dice):
        return tuple(randint(1,6) for _ in range(num_dice))

    @staticmethod
    def calculate_score(dice_roll):
        # Count the frequency of each number in the dice roll
        counts = Counter(dice_roll)
        score = 0

        # Scoring for single ones (100 points each) and single fives (50 points each)
        score += counts[1] * 100
        score += counts[5] * 50

        # Handling three of a kind or more
        for num in counts:
            if counts[num] >= 3:
                if num == 1:
                    score += 1000  # Three ones are 1000 points
                else:
                    score += num * 100  # Other three of a kinds

                # Additional scoring for four, five, or six of a kind
                if counts[num] > 3:
                    score *= 2 ** (counts[num] - 3)  # Doubling for each dice beyond three

        # Scoring for a straight from 1 to 6
        if set(dice_roll) == {1, 2, 3, 4, 5, 6}:
            score = 1500

        # Scoring for three pairs
        if len(counts) == 3 and all(count == 2 for count in counts.values()):
            score = 1000

        # Scoring for a full house (3 of a kind plus 2 of a kind)
        if len(counts) == 2 and (3 in counts.values() and 2 in counts.values()):
            score = 1500

        return score

# Example usage score 1500
dice_roll = (1, 2, 3, 4, 5, 6)
score = GameLogic.calculate_score(dice_roll)
score
```

## Replaced test files with lab's updated test files test_calculate_score.py and test_roll_dice.py

