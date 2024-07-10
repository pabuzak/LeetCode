board = [["5","3",".",".","7",".",".",".","."],
         ["6",".",".","1","9","5",".",".","."],
         [".","9","8",".",".",".",".","6","."],
         ["8",".",".",".","6",".",".",".","3"],
         ["4",".",".","8",".","3",".",".","1"],
         ["7",".",".",".","2",".",".",".","6"],
         [".","6",".",".",".",".","2","8","."],
         [".",".",".","4","1","9",".",".","5"],
         [".",".",".",".","8",".",".","7","9"]]

valid = True
valid_list = []

### first condition where each row contains the digits 1-9 without repetition
for i in range(len(board)): # represents row
    for j in range(len(board)): # represents col
        if board[i][j] in valid_list:
            valid = False
        elif board[i][j] != ".":
            valid_list.append(board[i][j])
    valid_list = []


### second condition where each column must contain the digits 1-9 without repetiion
for i in range(len(board)): # represents row
    for j in range(len(board)): # represents col
        if board[j][i] in valid_list:
            valid = False
        elif board[j][i] != ".":
            valid_list.append(board[j][i])
    valid_list = []

### third condition where each of the nine 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition
for i in range(len(board)): # represents row
    for j in range(0,3): # represents col
        if board[j][i] in valid_list:
            valid = False
        elif board[j][i] != ".":
            valid_list.append(board[j][i])
    
    if (i+1)%3 == 0:
        valid_list = []

for i in range(len(board)): # represents row
    for j in range(3,6): # represents col
        if board[j][i] in valid_list:
            valid = False
        elif board[j][i] != ".":
            valid_list.append(board[j][i])
    if (i+1)%3 == 0:
        valid_list = []

for i in range(len(board)): # represents row
    for j in range(6,9): # represents col
        if board[j][i] in valid_list:
            valid = False
        elif board[j][i] != ".":
            valid_list.append(board[j][i])
    if (i+1)%3 == 0:
        valid_list = []

print(valid)