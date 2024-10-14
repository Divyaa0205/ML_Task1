# Rock, Paper and Scissor Game.

import random


choices = ["rock", "paper", "scissors"]
win_cases = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

def winning_cases(user_choice, computer_choice):
    if computer_choice == user_choice:
        return "Draw"
    elif(user_choice, computer_choice) in win_cases:
        return f"Computer Choice: {computer_choice}\nUser Wins!"
    else:
        return f"Computer Choice: {computer_choice}\nComputer Wins!"


def play_game():
    print("Enter the choice\n1) rock \n2) paper \n3) scissors")
    user_choice = input()
    computer_choice = random.choice(choices)
    
    if user_choice not in choices:
        return "Invalid Choice"
    else:
        return winning_cases(user_choice, computer_choice)

print(play_game())


