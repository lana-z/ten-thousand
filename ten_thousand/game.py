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

        while not user_quit:
            print(f"Starting round {round_number}")
            dice_remaining = 6   
            #reset round score to 0 at the start of each round    
            unbanked_score = 0 
            
            while dice_remaining > 0:
                print(f"Rolling {dice_remaining} dice...")
                dice_roll = roller(dice_remaining)
                print("*** " + ''.join(str(die) + ' ' for die in dice_roll).strip() + " ***")
            
                roll_score = GameLogic.calculate_score(dice_roll)
                if roll_score == 0:  # Check for Farkle
                    print("""
                    ****************************************
                    **        Zilch!!! Round over         **
                    ****************************************
                    """)
                    break

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

                        next_move = input(f"You have {unbanked_score} unbanked points and {dice_remaining} dice remaining\n(r)oll again, (b)ank your points or (q)uit:\n> ")
                    
                    if next_move.lower() == 'b':
                        score += unbanked_score
                        print(f"You banked {unbanked_score} points in round {round_number}")
                        print(f"Total score is {score} points")
                        round_number += 1
                        break

                    elif next_move.lower() == 'r':
                        print(f"Rolling {dice_remaining} dice...")
                        dice_roll = roller(dice_remaining)
                        print("*** " + ''.join(str(die) + ' ' for die in dice_roll).strip() + " ***")
                        dice_remaining -= len(keep_dice)
                        
                        roll_score = GameLogic.calculate_score(dice_roll)

                    elif next_move.lower() == 'q':
                        user_quit = True
                        print(f"Thanks for playing. You earned {score} points")                        
                        break

                    else:
                        print("Invalid input. Please enter 'r', 'b', or 'q'.")
            
            if user_quit:
                break

        print(f"Thanks for playing. You earned {score} points")


    elif play_game.lower() == 'n':
        print("OK. Maybe another time")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    play()
