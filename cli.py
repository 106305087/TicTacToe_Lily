# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner, other_player


# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    current_player = 'O'  # X starts the game
    winner = None
    while winner is None and not is_board_full(board):
        for i in board:
          print(i)
        player = input('Enter your move for row and column, ex: 1 2: ').split()

        if len(player) != 2:
          print('Please enter only two number, row and column, ex: 1 2')
          continue
        row, column = int(player[0]), int(player[1])
        if row < 1 or row >3 or column < 1 or column > 3:
          print('Please enter the correct row and column number.')
          continue
        if board[row-1][column-1] is not None:
          print('Please enter the other places.')
          continue

        board[row-1][column-1] = current_player
        current_player = other_player(current_player)
        winner = get_winner(board)
        print(is_board_full(board))
    if winner is not None:
      print('{} won!'. format(winner))
    elif winner is None:
      print("It's a draw")
