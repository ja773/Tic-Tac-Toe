import pytest
from unittest.mock import patch

# Import the functions you want to test
from functions import *

# Sample board setups for testing
@pytest.fixture
def empty_board():
    return new_board()

@pytest.fixture
def mid_game_board():
    return [
        ['X', 'O', 'X'],
        ['O', None, None],
        ['X', 'O', None]
    ]

@pytest.fixture
def winning_board():
    return [
        ['X', 'X', 'X'],
        ['O', 'O', None],
        [None, None, 'O']
    ]

@pytest.fixture
def almost_won_board():
    return [
        ['X', 'X', None],
        ['O', None, None],
        ['O', None, None]
    ]


def test_new_board():
    expected_board = [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]
    assert new_board() == expected_board


def test_render(capsys):
    board = [
        [None, 'X', 'O'],
        ['O', 'X', None],
        [None, None, 'X']
    ]
    render(board)
    expected_output = "   0 1 2\n   -----\n0|   X O \n1| O X   \n2|     X \n   -----\n"
    captured = capsys.readouterr()
    assert captured.out == expected_output


@patch('builtins.input', side_effect=['1', '2'])
def test_get_move(mock_input):
    expected_move = [1, 2]
    assert get_move() == expected_move


def test_make_move():
    old_board = [
        [None, None, None],
        ['O', 'X', None],
        [None, None, 'X']
    ]
    move_coord = [0, 1]
    player = 'O'
    expected_board = [
        [None, 'O', None],
        ['O', 'X', None],
        [None, None, 'X']
    ]
    assert make_move(old_board, move_coord, player) == expected_board


def test_is_move_valid():
    board = [
        [None, 'X', 'O'],
        ['O', 'X', None],
        [None, None, 'X']
    ]
    valid_move = [2, 1]
    invalid_move_taken = [0, 1]  # Already taken
    invalid_move_outside = [3, 3]  # Outside the grid

    assert is_move_valid(board, valid_move) == True
    assert is_move_valid(board, invalid_move_taken) == False
    assert is_move_valid(board, invalid_move_outside) == False


def test_get_winner():
    # Horizontal win
    board1 = [
        ['X', 'X', 'X'],
        [None, 'O', 'O'],
        [None, None, None]
    ]
    # Vertical win
    board2 = [
        ['X', 'O', None],
        ['X', 'O', None],
        ['X', None, 'O']
    ]
    # Diagonal win
    board3 = [
        ['X', 'O', 'O'],
        [None, 'X', None],
        [None, None, 'X']
    ]
    # No win
    board4 = [
        ['X', 'O', 'X'],
        ['X', 'O', 'O'],
        ['O', 'X', 'O']
    ]

    assert get_winner(board1) == 'X'
    assert get_winner(board2) == 'X'
    assert get_winner(board3) == 'X'
    assert get_winner(board4) == False

def test_random_ai(empty_board):
    player = 'X'
    move = random_ai(empty_board, player)
    assert isinstance(move, list), "random_ai should return a list"
    assert len(move) == 2, "Move should be a coordinate with two values"
    assert empty_board[move[0]][move[1]] is None, "random_ai should return a valid empty move"

# Test find_winning_moves_ai function
def test_find_winning_moves_ai(almost_won_board):
    player = 'X'
    move = find_winning_moves_ai(almost_won_board, player)
    assert move == [0, 2], "AI should pick the winning move"

def test_find_winning_moves_ai_no_winning_move(mid_game_board):
    player = 'X'
    move = find_winning_moves_ai(mid_game_board, player)
    assert move in [[1, 1], [1, 2], [2, 2]], "AI should return any valid move if no winning move exists"

# Test find_winning_and_losing_moves_ai function
def test_find_winning_and_losing_moves_ai_winning(almost_won_board):
    player = 'X'
    move = find_winning_and_losing_moves_ai(almost_won_board, player)
    assert move == [0, 2], "AI should play the winning move"

def test_find_winning_and_losing_moves_ai_blocking(mid_game_board):
    player = 'O'
    move = find_winning_and_losing_moves_ai(mid_game_board, player)
    assert move == [1, 1], "AI should block opponent's winning move"

# Test minimax_score function
def test_minimax_score_winning(winning_board):
    player = 'X'
    opp = 'O'
    score = minimax_score(winning_board, opp, player)
    assert score == 10, "minimax_score should return 10 for a winning board"

def test_minimax_score_losing(winning_board):
    player = 'O'
    opp = 'X'
    score = minimax_score(winning_board, player, player)
    assert score == -10, "minimax_score should return -10 for a losing board"

def test_minimax_score_draw(empty_board):
    score = minimax_score(empty_board, 'X', 'X')
    assert score == 0, "minimax_score should return 0 for a draw"

# Test minimax_ai function
def test_minimax_ai_optimal_move(almost_won_board):
    player = 'X'
    move = minimax_ai(almost_won_board, player)
    assert move == [0, 2], "minimax_ai should pick the optimal move to win"

def test_minimax_ai_random_move(mid_game_board):
    player = 'O'
    move = minimax_ai(mid_game_board, player)
    assert move in [[1, 1], [1, 2], [2, 2]], "minimax_ai should pick an optimal move from available ones"

# Skipping the human_player function test because it requires user input