"""
WORKFLOW OF PROJECT:
1- Input from user(Rock, paper, scissor)
2- Computer choice (Computer will choose randomly not conditionally)
3- Result print

Cases:
A- Rock
Rock - Rock = tie
Rock - Paper = Paper win
Rock - scissor = Rock win

B- Paper
Paper - Paper = tie
Paper - Rock = Paper win
Paper - Scissor = Scissor win

C- Scissor
Scissor - Scissor = tie
Scissor - Rock = Rock win
Scissor - Paper = Scissor win

"""
import random
items = ["Rock", "Paper", "Scissor"]

user = input("Enter your choice = Rock, Paper, Scissor= ")
computer = random.choice(items)

print(f"User choice : {user} , Computer choice : {computer}")

if user == computer:
    print("Both chooses same : Match Tie!!!")

elif user == "Rock":
    if computer == "Paper":
        print("Computer Win!")
    else:
        print("You win!")

elif user == "Paper":
    if computer == "Scissor":
        print("Computer Win!")
    else:
        print("You win!")

elif user == "Scissor":
    if computer == "Paper":
        print("You win!")
    else:
        print("Computer win!")
