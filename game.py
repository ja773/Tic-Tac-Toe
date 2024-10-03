from functions import new_board, make_move, render, get_winner

def play_game(p1,p2):
    ''' Takes 2 interface classes as parameters and plays each other in a game '''
    # Starting the game with an empty board
    board = new_board()
    player1 = True   # to keep track of player

    moves = 0   # to keep track of number of moves played (<9) 
    while not get_winner(board) and moves < 9:
        render(board)
        if player1:
            player = 'X'
            move_coords = p1.make_move(board, player)
        else:
            player = 'O'
            move_coords = p2.make_move(board, player)
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