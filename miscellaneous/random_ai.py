from functions import new_board, make_move, is_move_valid_ai, render, get_winner, random_ai

# Starting the game with an empty board
board = new_board()
player1 = True   # to keep track of player

moves = 0   # to keep track of number of moves played (<9) 
while not get_winner(board) and moves < 9:
    render(board)
    if player1:
        player = 'X'
    else:
        player = 'O'
    move_coords = random_ai(board, player)
    while not is_move_valid_ai(board,move_coords):
        move_coords = random_ai(board, player)
    if player1:
        board = make_move(board, move_coords, 'X')
    else:
        board = make_move(board, move_coords, 'O')
    player1 = not player1
    moves += 1

render(board)
if not get_winner(board):
    print('This game was a draw')
else:
    print('Winner is ',get_winner(board))

