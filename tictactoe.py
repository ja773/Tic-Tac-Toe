from ai_classes import TicTacToeAI, HumanPlayer, RandomAI, WinningMoveAI, WinningAndLosingMoveAI, classMap
from game import play_game
import sys

if __name__ == '__main__':
    i1_name = input('Enter interface for player X: ')

    if i1_name not in classMap:
        print(f"Error: Interface '{i1_name}' not found.")
        sys.exit(1)
    
    i2_name = input('Enter interface for player O: ')

    if i2_name not in classMap:
        print(f"Error: Interface '{i2_name}' not found.")
        sys.exit(1)

    i1_class = classMap[i1_name]
    i2_class = classMap[i2_name]

    i1 = i1_class()
    i2 = i2_class()

    print('Player X is ',i1_name)
    print('Player O is ',i2_name)

    # Play the game
    play_game(i1,i2)



