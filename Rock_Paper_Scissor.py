import random

user_choice = input("Rock, Paper, or Scissor? ")

while(user_choice.lower() != "rock" and user_choice.lower() != "paper" and user_choice.lower() != "scissor"):
	user_choice = input('\"' + user_choice + "\"" + " is not a valid move. Please enter: Rock, Paper, or Scissor? ")

random = random.randint(1, 3)

if random == 1:
	computer_choice = "rock"
elif random == 2:
	computer_choice = "paper"
else:
	computer_choice = "scissor"

if user_choice.lower() == computer_choice:
	message = "Tie game"
elif user_choice.lower() == "rock" and computer_choice == "paper":
	message = "You lose"
elif user_choice.lower() == "rock" and computer_choice == "scissor":
	message = "You win"
elif user_choice.lower() == "paper" and computer_choice == "rock":
	message = "You win"
elif user_choice.lower() == "paper" and computer_choice == "scissor":
	message = "You lose"
elif user_choice.lower() == "scissor" and computer_choice == "rock":
	message = "You lose"
elif user_choice.lower() == "scissor" and computer_choice == "paper":
	message = "You win"

print("You chose " + user_choice.lower() + " and computer chose " + computer_choice + ". " + message + "!")