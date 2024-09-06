import random
import solver
import util

# set limit to number of times we are allowed to try a new number
SET_LIMIT = 50

def is_valid(board, row, col, num):
    """Check if placing num at (row, col) is valid."""
    # Check row
    if num in board[row]:
        return False
    # Check column
    if num in [board[i][col] for i in range(9)]:
        return False
    # Check 3x3 subgrid
    box_row = (row // 3) * 3
    box_col = (col // 3) * 3
    for i in range(box_row, box_row + 3):
        for j in range(box_col, box_col + 3):
            if board[i][j] == num:
                return False
    return True

def cons_board(board) -> bool:
    """Try to construct a valid Sudoku board."""
    for column_index in range(9):
        for row_index in range(9):
            if board[column_index][row_index] != 0:
                continue

            # Try different numbers for the empty cell
            attempts = 0
            while attempts < SET_LIMIT:
                attempts += 1
                num = random.randint(1, 9)
                if is_valid(board, column_index, row_index, num):
                    board[column_index][row_index] = num
                    if cons_board(board):
                        return True
                    board[column_index][row_index] = 0  # Undo the placement (backtrack)

            # If we exhausted attempts and couldn't place a number, backtrack
            return False

    # Base case: if the board is fully filled
    return True

def construct_board() -> None:
    board = [[0 for _ in range(9)] for _ in range(9)]
    cons_board(board)
    # util.print_sudoku(board)


construct_board()