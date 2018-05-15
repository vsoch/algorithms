# Tic Tac Toe!

> Write code to check if a tic tac toe board has a winner. It doesn't have to be a normal sized board!

## Assumptions

 - we assume the board is square, N by N
 - we assume a winning entry is a row, column, or diagonal all of one type


## Strategy 

 - we can iterate through rows, and keep other data structure to record diag/cols


```python

# I want a function to take a list (row, col, diag) and determine if winner

def has_winner(row, board_size=None):
    
    # If not defined, assume size is length of row
    if board_size is None:
        board_size = len(row)

    # Tic tac toe win spans the entire board
    if len(row) == board_size:

        # A winning row must only have one type
        if len(set(row)) == 1:
            return True

    return False

```
```python
def check_board(board):

    # grab columns as we go

    cols = [[] for x in range(len(board))]
    diag = []

    for r in range(len(board)):

        row = board[r]

        # Check if the row has a winner
        if has_winner(row):
            print('We have a winner!')
            return

        # Put a record for the column
        for col in range(len(row)):
            cols[col].append(row[col])
            if col == r:
                diag.append(row[col])

    # Check columns
    for col in board:

        # Check if the row has a winner
        if has_winner(col):
            print('We have a winner!')
            return

    # Check diagonal
    if has_winner(diag):
        print('The diagonal is a winner!')
        return

    print('No winner!')

```


Testing

```python
# Dummy board with winner
board = [[0,0,0], [0,0,1], [1,0,0]]
check_board(board)
# We have a winner!

# No winner
board = [[0,1,0], [1,0,1], [1,0,1]]
check_board(board)
# No winner!

# Diagonal Winner
board = [[0,1,0], [1,0,1], [1,0,0]]
check_board(board)
# The diagonal is a winner!
```
