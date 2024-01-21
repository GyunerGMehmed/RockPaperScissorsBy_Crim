import random

print("Welcome to Rock Paper Scissors game!")

rock = "Rock"
paper = "Paper"
scissors = "Scissors"

# Making an input for the player move
player_choice = input("Choose [r]ock, [p]aper or [s]cissors: ")
if player_choice == "r":
    player_move = rock
elif player_choice == "p":
    player_move = paper
elif player_choice == "s":
    player_move = scissors
else:
    # If the input is invalid exit the game and print the error message
    raise SystemExit("Invalid input. Try again with the choice available.[\'r', \'p', \'s']")

# Computer random choice generator
computer_choice = ''
computer_random_number = random.randint(1, 3)
if computer_random_number == 1:
    computer_choice = rock
elif computer_random_number == 2:
    computer_choice = paper
elif computer_random_number == 3:
    computer_choice = scissors

# print(f"The computer chose: {computer_choice}")

# Deciding the winner
if player_move == rock and computer_choice == scissors or \
        player_move == scissors and computer_choice == paper or \
        player_move == paper and computer_choice == rock:
    print(f"You chose: {player_move}, computer chose: {computer_choice}. \nYou win!")
elif player_move == computer_choice:
    print(f"You chose: {player_move}, Computer chose: {computer_choice}. \nIt's a draw!")
else:
    print(f"You chose: {player_move}, computer chose: {computer_choice}. \nYou lose!")