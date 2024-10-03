from functions import new_board, make_move, render, get_winner
from functions import human_player, random_ai, find_winning_moves_ai, find_winning_and_losing_moves_ai
from game import play_game, play_game_no_display
from tictactoe import TicTacToeAI, HumanPlayer, RandomAI, WinningMoveAI, WinningAndLosingMoveAI, classMap
import sys

def repeat_stats():
    ''' Function to play 2 AIs multiple times and return result statistics'''

    i1_name = input('Enter AI interface for player X: ')

    if i1_name not in classMap:
        print(f"Error: AI '{i1_name}' not found.")
        sys.exit(1)
    
    i2_name = input('Enter AI interface for player O: ')

    if i2_name not in classMap:
        print(f"Error: AI '{i2_name}' not found.")
        sys.exit(1)

    i1_class = classMap[i1_name]
    i2_class = classMap[i2_name]

    i1 = i1_class()
    i2 = i2_class()

    wins, draws, losses = 0,0,0

    loops = int(input('Enter number of repeated matches you want to test: '))

    for i in range(loops):
        w = play_game_no_display(i1,i2)
        if w == 'X':
            wins += 1
        elif w == 'O':
            losses += 1
        else:
            draws += 1
    
    if wins == losses:
        print(i1_name,'was as good as',i2_name,'over',loops,'games')
        win_rate = round(wins/loops*100,2)
        loss_rate = round(losses/loops*100,2)
        draw_rate = round(draws/loops*100,2)
        print(f'Win Rate: {win_rate}%')
        print(f'Loss Rate: {loss_rate}%')
        print(f'Draw Rate: {draw_rate}%')
    elif wins > losses:
        print('The better AI was',i1_name, 'over', loops, 'games')
        win_rate = round(wins/loops*100,2)
        loss_rate = round(losses/loops*100,2)
        draw_rate = round(draws/loops*100,2)
        print(f'Win Rate: {win_rate}%')
        print(f'Loss Rate: {loss_rate}%')
        print(f'Draw Rate: {draw_rate}%')
    else:
        print('The better AI was',i2_name, 'over', loops, 'games')
        win_rate = round(wins/loops*100,2)
        loss_rate = round(losses/loops*100,2)
        draw_rate = round(draws/loops*100,2)
        print(f'Win Rate: {loss_rate}%')
        print(f'Loss Rate: {win_rate}%')
        print(f'Draw Rate: {draw_rate}%')

if __name__ == '__main__':
    repeat_stats()
