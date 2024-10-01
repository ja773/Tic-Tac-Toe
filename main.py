


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
