from functions import new_board, make_move, render, get_winner
from functions import human_player, random_ai, find_winning_moves_ai, find_winning_and_losing_moves_ai
from game import play_game
import sys

# Base class for AI
class TicTacToeAI:
    def make_move(self, board, player):
        raise NotImplementedError("This method should be overridden by subclasses")
    
class RandomAI(TicTacToeAI):
    def make_move(self, board, player):
        return random_ai(board,player)

class WinningMoveAI(TicTacToeAI):
    def make_move(self, board, player):
        return find_winning_moves_ai(board,player)

class WinningAndLosingMoveAI(TicTacToeAI):
    def make_move(self, board, player):
        return find_winning_and_losing_moves_ai(board,player)

class HumanPlayer(TicTacToeAI):
    def make_move(self, board, player):
        return human_player(board,player)

classMap = {
    'random_ai' : RandomAI,
    'find_winning_moves_ai' : WinningMoveAI,
    'find_winning_and_losing_moves_ai' : WinningAndLosingMoveAI,
    'human_player' : HumanPlayer
}

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python tictactoe.py <AI_for_X> <AI_for_O>")
        sys.exit(1)

    p1_interface = sys.argv[1]
    p2_interface = sys.argv[2]

    # Fetch the AI class from the map and instantiate the objects
    p1_class = classMap[p1_interface]
    p2_class = classMap[p2_interface]

    if p1_class is None or p2_class is None:
        print(f"Error: AI '{p1_interface}' or '{p2_interface}' not found.")
        sys.exit(1)

    p1 = p1_class()  # Instantiate AI X
    p2 = p2_class()  # Instantiate AI O

    print('Player X is ',p1_interface)
    print('Player O is ',p2_interface)

    # Play the game
    play_game(p1,p2)



