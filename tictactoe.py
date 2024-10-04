from ai_classes import TicTacToeAI, HumanPlayer, RandomAI, WinningMoveAI, WinningAndLosingMoveAI, classMap
from game import play_game
import sys

if __name__ == '__main__':
    # if len(sys.argv) != 3:
    #     print("Usage: python tictactoe.py <AI_for_X> <AI_for_O>")
    #     sys.exit(1)

    # p1_interface = sys.argv[1]
    # p2_interface = sys.argv[2]

    # # Fetch the AI class from the map and instantiate the objects
    # p1_class = classMap[p1_interface]
    # p2_class = classMap[p2_interface]

    # if p1_class is None or p2_class is None:
    #     print(f"Error: AI '{p1_interface}' or '{p2_interface}' not found.")
    #     sys.exit(1)

    # p1 = p1_class()  # Instantiate AI X
    # p2 = p2_class()  # Instantiate AI O

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



