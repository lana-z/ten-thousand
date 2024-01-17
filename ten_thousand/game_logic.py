from random import randint
from collections import Counter

class GameLogic:
    @staticmethod
    def roll_dice(num_dice):
        return tuple(randint(1,6) for _ in range(num_dice))

    @staticmethod
    def calculate_score(dice_roll):
        counts = Counter(dice_roll)
        score = 0

        # Check for straight, three pairs, and full house first since they are exclusive
        if set(dice_roll) == {1, 2, 3, 4, 5, 6}:
            return 1500
        if len(counts) == 3 and all(count == 2 for count in counts.values()):
            return 1000
        if len(counts) == 2 and (3 in counts.values() and 2 in counts.values()):
            return 1500

        # Scoring for three or more of a kind (excluding ones initially)
        for num in counts:
            if counts[num] >= 3:
                if num == 1:
                    score += 1000
                    additional_dice = counts[num] - 3
                    score += additional_dice * 1000
                else:
                    score += num * 100
                    additional_dice = counts[num] - 3
                    score += additional_dice * num * 100

        # Scoring for single ones and fives (not part of three or more of a kind)
        # Check if ones or fives are part of a multiple, and subtract them from the total count
        if counts[1] < 3:
            score += counts[1] * 100
        if counts[5] < 3:
            score += counts[5] * 50

        return score
