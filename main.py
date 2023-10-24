import random
import sys

choises = ["paper", "scissors", "rock"]

def play_game(player_choice):
    computer = random.choice(choises)

    if player_choice not in choises:
        print("Invalid choice. Choose from 'rock', 'scissor', or 'paper'.")
        return

    print("Player: ", player_choice)
    print("Computer: ", computer)

    if player_choice == computer:
        print("It's a tie!")

    elif player_choice == "rock":
        if computer == "paper":
            print("You lose!")
        if computer == "scissors":
            print("You win!")

    elif player_choice == "paper":
        if computer == "scissors":
            print("You lose!")
        if computer == "rock":
            print("You win!")

    elif player_choice == "scissors":
        if computer == "rock":
            print("You lose!")
        if computer == "paper":
            print("You win!")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python main.py <choice>")
        sys.exit(1)

    player_choice = sys.argv[1].lower()
    play_game(player_choice)
