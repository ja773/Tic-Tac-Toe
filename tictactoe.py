from functions import new_board, make_move, render, get_winner
from functions import human_player, random_ai, find_winning_moves_ai, find_winning_and_losing_moves_ai
import sys

# Base class for AI
class TicTacToeAI:
    def make_move(self, board, player):
        raise NotImplementedError("This method should be overridden by subclasses")
    
class RandomAI(TicTacToeAI):
    def make_move(self, board, player):
        random_ai(board,player)

class WinningMoveAI(TicTacToeAI):
    def make_move(self, board, player):
        find_winning_moves_ai(board,player)

class WinningAndLosingMoveAI(TicTacToeAI):
    def make_move(self, board, player):
        find_winning_and_losing_moves_ai(board,player)

class HumanPlayer(TicTacToeAI):
    def make_move(self, board, player):
        human_player(board,player)

classMap = {
    'random_ai' : RandomAI,
    'find_winning_moves_ai' : WinningMoveAI,
    'find_winning_and_losing_moves_ai' : WinningAndLosingMoveAI,
    'human_player' : HumanPlayer
}
