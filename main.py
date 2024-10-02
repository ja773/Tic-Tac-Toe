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
    new_board = old_board
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