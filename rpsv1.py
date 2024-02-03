import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

print("")

playerchoice = input("Enter your choice...\n1 For Rock, \n2 For Paper, or \n3 For Scissors:\n\n")

player = int(playerchoice)

if player < 1 or player > 3:
    sys.exit("You must enter 1, 2 or 3")
    
computerchoice = random.choice("123")

computer = int(computerchoice)

print("")
print("You Chose " + str(RPS(player)).replace('RPS.', '') + ".")
print("Python Chose " + str(RPS(computer)).replace('RPS.', '') + ".") 
print("")

if player == 1 and computer == 3:
    print("🥳 You Win!\n")
elif player == 2 and computer == 1:
    print("🥳 You Win!\n")
elif player == 3 and computer == 2:
    print("🥳 You Win!\n")
elif player == computer: 
    print("🙄 Tie Game!\n")
else:
    print("🐍 Python Wins!\n")
    