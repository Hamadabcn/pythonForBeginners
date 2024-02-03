import sys
import random
from enum import Enum

def rps(name='PlayerOne'):
    game_count = 0
    player_wins = 0
    python_wins = 0
    
    def play_rps():
        nonlocal name
        nonlocal player_wins
        nonlocal python_wins
        
        class RPS(Enum):
            ROCK = 1
            PAPER = 2
            SCISSORS = 3
            
        playerchoice = input(f"\n{name}, please enter your choice...\n1 For Rock, \n2 For Paper,\n3 For Scissors.\n\n")
        
        if playerchoice not in ["1", "2", "3"]:
            print(f"\n{name}, please enter 1, 2 or 3\n")
            play_rps()

        player = int(playerchoice)
            
        computerchoice = random.choice("123")

        computer = int(computerchoice)

        print(f"\n{name}, you Chose {str(RPS(player)).replace('RPS.', '').title()}.\n")
        print(f"Python Chose {str(RPS(computer)).replace('RPS.', '').title()}.\n")
        
        def decide_winner(player, computer):
            nonlocal name
            nonlocal player_wins
            nonlocal python_wins
            
            if player == 1 and computer == 3:
                player_wins += 1
                return f"🥳  {name} you win! 🥳\n"
            elif player == 2 and computer == 1:
                player_wins += 1
                return f"🥳  {name} you win! 🥳\n"
            elif player == 3 and computer == 2:
                player_wins += 1
                return f"🥳  {name} you win! 🥳\n"
            elif player == computer: 
                return"🙄  Tie game! 🙄\n"
            else:
                python_wins += 1
                return f"🐍  Python Wins! 🐍\nBad Luck You Loss, {name}...😣😒"
            
        game_result = decide_winner(player, computer)
        
        print(game_result)
            
        nonlocal game_count
        game_count += 1
        
        print(f"\nGame Count: {game_count}")
        print(f"\n{name} wins: {player_wins}")
        print(f"\nPythons Wins: {python_wins}")
        
            
        print(f"\nDo you want to play again, {name}?\n")
        
        while True:
            playagain = input("Y to play again \nor Q to quit\n")
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
            sys.exit(f"\n    Bye {name}! 👋 🤧 🖖\n")
        
    return play_rps

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personalized game experience."
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="Then name of the person playing the game."
    )

    args = parser.parse_args()
    
    rock_paper_scissors = rps(args.name)
    rock_paper_scissors()
    
    # py rps.py -n "name of the player" to start the game