def solve_n_queens(n):
    def backtrack(row):
        if row == n:
            # All queens placed; copy current board configuration
            solutions.append(["".join(r) for r in board])
            return

        for col in range(n):
            # Check if current position (row, col) is safe
            if col in cols or (row + col) in pos_diag or (row - col) in neg_diag:
                continue

            # "Choose": Place the queen
            board[row][col] = "Q"
            cols.add(col)
            pos_diag.add(row + col)
            neg_diag.add(row - col)

            # "Explore": Move to the next row
            backtrack(row + 1)

            # "Unchoose" (Backtrack): Remove queen to try next column
            board[row][col] = "."
            cols.remove(col)
            pos_diag.remove(row + col)
            neg_diag.remove(row - col)

    solutions = []
    board = [["."] * n for _ in range(n)]
    cols, pos_diag, neg_diag = set(), set(), set()
    backtrack(0)
    return solutions
