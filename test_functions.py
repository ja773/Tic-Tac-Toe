import pytest
from io import StringIO
from unittest.mock import patch

# Import the functions you want to test
from functions import new_board, render, get_move, make_move, is_move_valid, get_winner


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
