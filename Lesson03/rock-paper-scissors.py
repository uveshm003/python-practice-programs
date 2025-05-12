import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    SCISSORS = 2
    PAPER = 3

playerChoice = (input("Enter...\n1 for Rock\n2 for scissors\n3 for paper\n"))


player = int(playerChoice)

if player < 1 | player > 3:
    sys.exit("Please enter a valid value")

computerChoice = random.choice("123")

computer = int(computerChoice)

print("\nYou chose " + str(RPS(player).name) + "\nCompute Chose " + str(RPS(computer).name) + "\n")

isDraw = player == computer
computerWins = (player == 1 & computer == 3 | player == 2 & computer == 1 | player == 3 & computer == 2) 
if isDraw:
    print("Game Draw!")
elif computerWins:    
    print("Computer Wins")
else:
    print("Player Wins")
sys.exit()