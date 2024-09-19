import random

# Options for the game
choices = ["rock", "paper", "scissors"]

print("*** Welcome to Rock, Paper, Scissors Game! ***")

while True:
    print("\nChoose: rock, paper, or scissors (or type 'exit' to quit)")
    user_choice = input("Your choice: ").lower()

    if user_choice == "exit":
        print("thank you so much for playing this wondorfull and fun game")
        break

    if user_choice not in choices:
        print("Invalid choice! Please choose 'rock', 'paper', or 'scissors'.")
        continue

    # Computer makes a random choice
    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("oops!Computer wins!")