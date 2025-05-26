import sys
import random
import argparse

def guess_num(name = "Player 1"):
    player_wins = 0

    def play_game():
        nonlocal player_wins
        nonlocal name

        player_choice = int(input("Enter your choice of number between 1 to 10 : "))

        if player_choice not in range(1,11,1):
            print("Wrong choice!...")
            return play_game()
        python_choice = random.choice(range(1,11))

        print(f"Python's choice is : {python_choice}")

        if player_choice == python_choice:
            print(f"Congratulations! {name}, You guessed it right!")
        else:
            print(f"Oops, Wrong guess... Try again")
            return play_game()
        
        def play_again():
            play = input("Want to play again? (Y/N)")
            if((play == 'Y') or (play == 'y')):
                return play_game()
            elif((play == 'N') or (play == 'n')):
                print(f"Bye {name}!")
                sys.exit(0)
            else:
                return play_again()
        
        play_again()
    
    return play_game()

parser = argparse.ArgumentParser(
    description="Guessing the Number Game"
)

parser.add_argument(
    "-n", "--name", metavar="name",
    required=True, help="The name of the player."
)

args = parser.parse_args()
print(f"Hi {args.name}. Welcome to the Guessing the Number Game!")
guess_num(args.name)