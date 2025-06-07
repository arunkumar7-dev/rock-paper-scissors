# Rock, Paper, Scissor Game with exception handling

import random

condition = True

while condition: # True beacuse i want it to run continuously
    
    try:
        computer = random.choice([-1, 0, 1])
        user_input = input("Enter your choice (r for Rock, p for Paper, s for Scissor): ").lower()
        user_dict = {"r": -1, "p": 0, "s": 1}
        revrs_dict = {-1: "Rock", 0: "Paper", 1: "Scissor"}  # Reversing th directory
        
        user = user_dict[user_input]  # might raise KeyError
        
        print(f"You chose -> {revrs_dict[user]}\nComputer chose -> {revrs_dict[computer]}")

        if computer == user:
            print("Damnn, its a DRAW.......!")
        else:
            if computer == -1 and user == 1:
                print("You lose........!")
            elif computer == 1 and user == -1:
                print("You Win........!")
            elif computer == 1 and user == 0:
                print("You lose........!")
            elif computer == 0 and user == 1:
                print("You Win........!")    
            elif computer == 0 and user == -1:
                print("You lose........!")
            elif computer == -1 and user == 0:  # fixed 'o' to 0 here
                print("You win........!")
            else:
                print("Something went wrong :(")

    except KeyError:
        print("Invalid input! Please enter 'r', 'p', or 's'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

    # For exiting the loop
    play_again = input("Play again? (y/n): ").lower() 
    if play_again != 'y':
        condition = False
        print("Thanks for playing!")
