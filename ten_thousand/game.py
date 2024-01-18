from ten_thousand.game_logic import GameLogic 

def play():
    print("Welcome to Ten Thousand")
    play_game = input("(y)es to play or (n)o to decline\n> ")

    if play_game.lower() == 'y':
        # Add logic here to start the game
        print("Starting round 1 🏁")
        
        print("Rolling 6 dice...🎲")
        dice_roll = GameLogic.roll_dice(6)
        print("***", " ".join(map(str, dice_roll)), "***")
        
        keep_dice = input("Enter dice to keep, or (q)uit:\n> ")
        if keep_dice.lower() == 'q':
            print("Thanks for playing. You earned 0 points")


    elif play_game.lower() == 'n':
        print("OK. Maybe another time")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

if __name__ == "__main__":
    play()
