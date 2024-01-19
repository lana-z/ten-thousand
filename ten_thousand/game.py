from ten_thousand.game_logic import GameLogic 

def play(roller=None):
    if roller is None:
            roller = GameLogic.roll_dice

    print("Welcome to Ten Thousand")
    #print or input prints
    play_game = input("(y)es to play or (n)o to decline\n> ")
    score = 0

    if play_game.lower() == 'y':
        round_number = 1
        
        # Flag to indicate the end of the game
        user_quit = False

        #while True: the user keeps playing is true, infinite loop
        #while not user_quit
        #while user_quit == False  do same thing but the second two include a Flag for end of game and prevent infinite loop
        #all three of the above are the same the second two include a Flag, a way to let the user quit and stop the loop
        while not user_quit:
            print(f"Starting round {round_number}")
        
            print("Rolling 6 dice...")
            dice_roll = roller(6)
            print("*** " + ''.join(str(die) + ' ' for die in dice_roll).strip() + " ***")
        
            while True:
                keep_dice = input("Enter dice to keep, or (q)uit:\n> ")

                if keep_dice.lower() == 'q':
                    user_quit = True
                    break
                
                else:
                    #convert each character in keep_dice to an integer
                    keep_dice = tuple(map(int, keep_dice))
                    unbanked_score = GameLogic.calculate_score(keep_dice)
                    dice_remaining = 6 - len(keep_dice)

                    next_roll = input(f"You have {unbanked_score} unbanked points and {dice_remaining} dice remaining\n(r)oll again, (b)ank your points or (q)uit:\n> ")
                    
                    if next_roll.lower() == 'b':
                        score += unbanked_score
                        print(f"You banked {unbanked_score} points in round {round_number}")
                        print(f"Total score is {score} points")
                        break

                    elif next_roll.lower() == 'r':
                        break

                    elif next_roll.lower() == 'q':
                        user_quit = True
                        print(f"Thanks for playing. You earned {score} points")                        
                        break

                    else:
                        print("Invalid input. Please enter 'r', 'b', or 'q'.")
            
            if user_quit:
                break

            round_number += 1

        print(f"Thanks for playing. You earned {score} points")


    elif play_game.lower() == 'n':
        print("OK. Maybe another time")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    play()
