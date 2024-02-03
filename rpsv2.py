import sys
import random
from enum import Enum

class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3
    
playagain = True

while playagain:

    playerchoice = input("\nEnter your choice...\n1 For Rock, \n2 For Paper,\n3 For Scissors.\n\n")

    player = int(playerchoice)

    if player < 1 or player > 3:
        sys.exit("You must enter 1, 2 or 3")
        
    computerchoice = random.choice("123")

    computer = int(computerchoice)

    print("\nYou Chose " + str(RPS(player)).replace('RPS.', '') + ".")
    print("Python Chose " + str(RPS(computer)).replace('RPS.', '') + ".\n") 

    if player == 1 and computer == 3:
        print("🥳  You Win! 🥳\n")
    elif player == 2 and computer == 1:
        print("🥳  You Win! 🥳\n")
    elif player == 3 and computer == 2:
        print("🥳  You Win! 🥳\n")
    elif player == computer: 
        print("🙄  Tie Game! 🙄\n")
    else:
        print("🐍  Python Wins! 🐍\n")
        
    playagain = input("\nPlay Again? \nY to play again \nor Q to quit \n\n")
    
    if playagain.lower() == "y":
        continue
    else:
        print("\n🎉 🎆 🎉 🎊 🎈 🎇 🥳 🎈 🎊 🍾 🍾 \n")
        print("Thank you for playing 🤩\n")
        #playagain = False  # either way would break the while loop
        break

sys.exit("Bye! 👋 🤧 🖖\n")
        