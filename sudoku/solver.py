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

def is_valid(board: list[list[int]]):
    """
    Checks if the given matrix is valid. This includes checking the 
    dimensions, validity of rows, columns, boxes and diagonals, as well
    as the values the board holds.
    """
    # define return value
    valid : bool = True

    # check the dimensions are 9x9
    valid = valid and len(board) == 9
    valid = valid and all(len(row) == 9 for row in board)

    # check rows
    valid = valid and all(check_row(row) for row in board)

    # check columns
    valid = valid and check_columns()

def check_row(row: list[int]) -> bool:
    """
    Checks if the given row of a sudoku is valid. A valid row contains no more 
    than 1 of each digit excluding 0.
    """
    # map of digit to number of occurences
    occurence_map : dict[int, int] = {i : 0 for i in range(1, 10)}

    for num in row:
        # we dont care about empty spaces
        if num == 0:
            continue

        # if we encounter a number not in range(1, 10), sudoku is invalid
        if num not in range(1, 10):
            return False

        # increment number of occurences by 1 
        occurence_map[num] += 1
    
    # check that each number only appears once
    return all(value == 1 or value == 0 for value in occurence_map.values())

def check_columns(board: list[list[int]]) -> bool:
    """
    Checks whether the given board contains valid columns or not. 
    A valid row contains no more than 1 of each digit excluding 0.
    """
    valid : bool = True

    # indicates what column we are currently checking
    for current_colummn in range(1, 10):
        # map of digit to number of occurences
        occurence_map : dict[int, int] = {i : 0 for i in range(1, 10)}
        
        # go over each row to find all values in a column
        for row in board:
            print(row[current_colummn - 1])
            print(occurence_map)
            print(current_colummn)
            # we dont care about empty spaces
            if row[current_colummn - 1] == 0:
                continue

            # we do not need to validate that only digits between 1 and 9 appear
            # since we do this in check_row()

            # increment number of occurences by 1 
            occurence_map[current_colummn - 1] += 1

        # check that each number only appears once
        valid = valid and all(value == 1 or value == 0 for value in occurence_map.values())
    
    return valid



def checkBox():
    pass

def checkDiagonal():
    pass

def checkValues():
    pass

# temp main function for debugging
def main():
    print(check_columns(demo_board))

main()