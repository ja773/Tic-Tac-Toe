# tic-tac-toe
A simple command-line tic-tac-toe game.

The game supports human input and AI engines.

So far, supported players are:
- 'human_player'
- 'random_ai'
- 'find_winning_moves_ai'
- 'find_winning_and_losing_moves_ai'

To play with these engines, run:
python tictactoe.py <player 1> <player 2>

This would start a game between the 2 players.
The 2 players have to be one of the supported players to work.

Additionally, you can compare how different AI engines play against each other and gather statistics by running:
python random_statistics.py

Following the prompts will let you see win and draw rates for the matched engines over a set number of games.
