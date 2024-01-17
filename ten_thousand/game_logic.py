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