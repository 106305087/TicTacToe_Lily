def check_winner_pythonic(board):
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

def make_empty_board():
    return [
        [None, None, None],
        [None, None, None],
        [None, None, None],
    ]


if __name__ == '__main__':
    board = make_empty_board()
    current = 1
    winner = None
    while winner is None and current < 9:
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

        if current%2 == 1:
          board[row-1][column-1] = 'O'
        else:
          board[row-1][column-1] = 'X'
        current += 1
        winner = check_winner_pythonic(board)
    if winner is not None:
      print('{} won!'. format(winner))
    elif winner is None:
      print("It's a draw")
