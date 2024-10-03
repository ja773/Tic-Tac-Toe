import random, copy

def new_board():
    ''' Function to initialise an empty board as a 2D list'''
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None]
    ]


def render(board):
    ''' Function to print a board in a neat readable format'''
    print('   0 1 2')
    print(' '*3 + '-'*5)
    for i in range(3):
        row = str(i) + '| '
        for j in board[i]:
            if j == None:
                row += ' '
            else:
                row += j
            row += ' '
        print(row)
    print(' '*3 + '-'*5)

def get_move():
    ''' Function to convert a user input for a move to a co-ordinate list'''
    coords = [0,0]
    coords[0] = int(input('Enter the row number of your move:'))
    coords[1] = int(input('Enter the column number of your move:'))
    return coords

def make_move(old_board, move_coord, player):
    ''' 
    Function to create an updated board with the input move
    '''
    new_board = copy.deepcopy(old_board)
    new_board[move_coord[0]][move_coord[1]] = player
    return new_board

def is_move_valid(board, move):
    ''' Function to determine if a move is valid'''
    if move[0] not in range(3) or move[1] not in range(3):
        print('Error: The square is not inside the grid!')
        return False
    if board[move[0]][move[1]] is not None:
        print('Error: This square is already taken!')
        return False
    return True

def is_move_valid_ai(board, move):
    ''' Function to determine if a move is valid for an AI input'''
    if move[0] not in range(3) or move[1] not in range(3):
        return False
    if board[move[0]][move[1]] is not None:
        return False
    return True

def get_winner(board):
    ''' Function to determine the winner given a board setup'''
    for row in board:
        if row == ['X','X','X']:
            return 'X'
        if row == ['O','O','O']:
            return 'O'
    for c in range(3):
        col = []
        for r in range(3):
            col.append(board[r][c])
        if col == ['X','X','X']:
            return 'X'
        if col == ['O','O','O']:
            return 'O'
    diag1 = [board[i][i] for i in range(3)]
    if diag1 == ['X','X','X']:
        return 'X'
    if diag1 == ['O','O','O']:
        return 'O'
    diag2 = [board[i][2-i] for i in range(3)]
    if diag2 == ['X','X','X']:
        return 'X'
    if diag2 == ['O','O','O']:
        return 'O'    
    return False

def random_ai(board,player):
    ''' AI engine that plays random moves'''
    poss_moves = []
    for i in range(3):
        for j in range(3):
            if is_move_valid_ai(board,[i,j]):
                poss_moves.append([i,j])
    move = random.choice(poss_moves)
    return move

def find_winning_moves_ai(board,player):
    ''' AI engine that plays a winning move if it exists or a random move'''
    poss_moves = []
    for i in range(3):
        for j in range(3):
            move_coords = [i,j]
            if is_move_valid_ai(board,move_coords):
                poss_moves.append(move_coords)
    for k in range(len(poss_moves)):
        new_board = make_move(board,poss_moves[k],player)
        if get_winner(new_board) == player:
            return poss_moves[k]
    move = random.choice(poss_moves)
    return move

def find_winning_and_losing_moves_ai(board,player):
    ''' AI engine that plays a winning move if it exists or blocks an opponent's winning move or a random move'''
    poss_moves = []
    if player == 'O':
        opp = 'X'
    else:
        opp = 'O'
    for i in range(3):
        for j in range(3):
            move_coords = [i,j]
            if is_move_valid_ai(board,move_coords):
                poss_moves.append(move_coords)
    for k in range(len(poss_moves)):
        new_board = make_move(board,poss_moves[k],player)
        if get_winner(new_board) == player:
            return poss_moves[k]
    for l in range(len(poss_moves)):
        new_board = make_move(board,poss_moves[l],opp)
        if get_winner(new_board) == opp:
            return poss_moves[l]
    move = random.choice(poss_moves)
    return move
