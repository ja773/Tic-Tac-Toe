from main import new_board, make_move, is_move_valid, get_move, render, get_winner

# Starting the game with an empty board
board = new_board()
player1 = True          #to keep track of player

while not get_winner(board):
    render(board)
    if player1:
        print('Make a move for X')
    else:
        print('Make a move for O')
    move_coords = get_move()
    while not is_move_valid(board,move_coords):
        move_coords = get_move()
    if player1:
        board = make_move(board, move_coords, 'X')
    else:
        board = make_move(board, move_coords, 'O')
    player1 = not player1

render(board)
print('Winner is ',get_winner(board))

