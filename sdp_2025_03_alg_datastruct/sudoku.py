def solve_sudoku(board):
    # Find next empty cell
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                # Try numbers 1-9
                for num in range(1, 10):
                    if is_safe(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board): # Recurse
                            return True
                        board[row][col] = 0 # Backtrack
                return False # No number works here
    return True # All cells filled

def is_safe(board, row, col, num):
    # Check row and column
    for x in range(9):
        if board[row][x] == num or board[x][col] == num:
            return False
    # Check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[i + start_row][j + start_col] == num:
                return False
    return True
