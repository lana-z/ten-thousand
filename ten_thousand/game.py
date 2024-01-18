

def play():
    print("Welcome to Ten Thousand")
    choice = input("(y)es to play or (n)o to decline\n> ")

    if choice.lower() == 'y':
        # Add logic here to start the game
        print("Starting the game...🎲")
    elif choice.lower() == 'n':
        print("OK. Maybe another time")
    else:
        print("Invalid input. Please enter 'y' or 'n'.")

play()
