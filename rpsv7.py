import sys
import random
from enum import Enum

def rps():
    game_count = 0
    player_wins = 0
    python_wins = 0
    
    def play_rps():
        nonlocal player_wins
        nonlocal python_wins
        
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3
            
        playerchoice = input("\nEnter your choice...\n1 For Rock, \n2 For Paper,\n3 For Scissors.\n\n")
        
        if playerchoice not in ["1", "2", "3"]:
            print("You must enter 1, 2 or 3")
            play_rps()

        player = int(playerchoice)
            
        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\nYou Chose {str(RPS(player)).replace('RPS.', '').title()}.")
        print(f"Python Chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")
        
        def decide_winner(player, computer):
            nonlocal player_wins
            nonlocal python_wins
            
            if player == 1 and computer == 3:
                player_wins += 1
                return"🥳  You Win! 🥳\n"
            elif player == 2 and computer == 1:
                player_wins += 1
                return"🥳  You Win! 🥳\n"
            elif player == 3 and computer == 2:
                player_wins += 1
                return"🥳  You Win! 🥳\n"
            elif player == computer: 
                return"🙄  Tie Game! 🙄\n"
            else:
                python_wins += 1
                return"🐍  Python Wins! 🐍\n"
            
        game_result = decide_winner(player, computer)
        
        print(game_result)
            
        nonlocal game_count
        game_count += 1
        
        print("\nGame Count: " + str(game_count))
        print("\nPlayer Wins: " + str(player_wins))
        print("\nPythons Wins: " + str(python_wins))
        
            
        print("\nPlay Again?\n")
        
        while True:
            playagain = input("\nY to play again \nor Q to quit\n")
            if playagain.lower() not in ["y", "q"]:
                continue
            else:
                break
            
        if playagain.lower() == "y":
            return play_rps()
        else:
            print("\n🎉 🎆  🎊 🎈 🎇 🥳  🍾 🍾")
            print("\nThank you for playing 🤩\n")
            # playagain = False  # either way would break the while loop
            # break 
            sys.exit("\n    Bye! 👋 🤧 🖖\n")
        
    return play_rps


rock_paper_scissors = rps()

if __name__ == "__main__":
    rock_paper_scissors()