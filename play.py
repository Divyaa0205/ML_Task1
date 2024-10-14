# Rock, Paper and Scissor Game

import random
import sys

choices = ["rock", "paper", "scissors"]
win_cases = {"rock": "scissors", "paper": "rock", "scissors": "paper"}

def winning(user, computer):
    if computer == user:
        return "Draw"
    elif(user, computer) in win_cases:
        return "User Wins!"
    else:
        return "Computer Wins"

def play
