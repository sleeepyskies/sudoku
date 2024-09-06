import util

demo_board = [
    [3, 0, 6, 5, 0, 8, 4, 0, 0],
    [5, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 8, 7, 0, 0, 0, 0, 3, 1],
    [0, 0, 3, 0, 1, 0, 0, 8, 0],
    [9, 0, 0, 8, 6, 3, 0, 0, 5],
    [0, 5, 0, 0, 9, 0, 6, 0, 0], 
    [1, 3, 0, 0, 0, 0, 2, 5, 0],
    [0, 0, 0, 0, 0, 0, 0, 7, 4],
    [0, 0, 5, 2, 0, 6, 3, 0, 0]
]

def solveSudoku(board) -> bool:
    # find the first empty postition in the board
    for column_index in range(9):
        for row_index in range(9):
            # print(column_index, row_index)
            # we have reached final board position, and it is not 0 -> sudoku solved !! :)
            if column_index == row_index == 8 and board[column_index][row_index] != 0:
                util.print_sudoku(board)
                return True

            # empty position found
            if board[column_index][row_index] == 0:
                # test all nums in this position
                for test_num in range(1, 10):
                    # if test_num is valid in this position, continue algorithm
                    if convert_indices_to_list(board, column_index, row_index, test_num):
                        solveSudoku(board)
    
    return False

def is_list_valid(nums) -> bool:
    """
    Returns if a list of numbers contains any number expect 0 more than once.
    If yes, return false, if not return true.
    Additionally checks for invalid entries.
    """
    occurence_map = {i : 0 for i in range(1, 10)}

    for num in nums:    
        # ignore 0
        if num == 0:
            continue

        # increase occurence
        occurence_map[num] += 1

        # illegal entry or too many of one number 
        if num not in range(10) or occurence_map[num] > 1:
            return False
    
    # list is valid
    return True

def convert_indices_to_list(board, column_index, row_index, updated_value) -> bool:
    """
    Takes a sudoku board as well as the current indices and 
    the new value to test, and checks whether it will make the board invalid.
    """
    # add entry
    board[column_index][row_index] = updated_value

    # set row_list
    row_list = board[column_index]

    column_list = []
    # set column_list
    for i in range(9):
        column_list.append(board[i][row_index])

    # set box_index, first find box index
    x = (column_index // 3) * 3
    y = (row_index // 3) * 3

    box_list = []
    # set box_list
    for i in range(3):
        for j  in range(3):
            box_list.append(board[i][j])

    return is_list_valid(row_list) and (column_list) and (box_list)

def main(): 
    solveSudoku(demo_board)

main()