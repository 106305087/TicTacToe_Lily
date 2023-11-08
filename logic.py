# This file is where game logic lives. No input
# or output happens here. The logic in this file
# should be unit-testable.


def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


def get_winner(board):
  #check row
  for row in board:
    if len(set(row)) == 1 and row[0]!='':
      return row[0]

  #check columns
  for i in range(len(board)):
    column = [board[j][i] for j in range(len(board))]
    if len(set(column)) == 1 and board[0][i]!='':
      return board[0][i]

  #check diagonals
  top_left_to_bottom_right = [board[i][i] for i in range(len(board))]
  if len(set(top_left_to_bottom_right)) == 1 and board[0][0] != '':
    return board[0][0]

  top_right_to_bottom_left = [board[i][len(board)-i-1] for i in range(len(board))]
  if len(set(top_right_to_bottom_left)) == 1 and board[0][len(board)-1] != '':
    return board[0][len(board)-1]

  return None


def other_player(player):
    """Given the character for a player, returns the other player."""
    return "O" if player == "X" else "X"

def is_board_full(board):
    for row in board:
        for cell in row:
            if cell is None:
                return False
    return True
