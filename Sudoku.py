# Simran Hundal

# const board to be solved
# 0 stands in for non given value
Sudoku = [
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


# function to display Sudoku board
def display(board):
    print_line()

    for i in range(9):
        if i % 3 == 0 and i != 0:
            print_line()

        print("| ", end="")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            # only go to new line after the whole row has been printed
            if j < 8:
                print(str(board[i][j]) + " ", end="")

            else:
                print(str(board[i][j]) + " |")
    print_line()


def print_line():
    print("---------------------------")


# function to find first non given digit on sudoku board
def empty_digit(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == 0:
                # row and column index of empty digit
                return i, j

    return None


# using backtracking to find solution
def solve_board(board):
    isempty = empty_digit(board)
    if not isempty:
        # if board has no empty spaces it is solved
        return True

    row, col = isempty

    for i in range(1, 10):
        # check if number is valid with current board
        if is_valid(board, i, (row, col)):
            board[row][col] = i
            # if it is valid keep going to find values for other empty digits
            if solve_board(board):
                return True
            # setting back to 0 if solution was not found
            board[row][col] = 0
    # exiting for loop means no solution was found
    return False


# function to check if a given digit is valid with current Sudoku board
def is_valid(board, num, pos):
    # check column
    for i in range(9):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    # check row
    for i in range(9):
        if board[pos[0]][i] == num and pos[1] != i:
            return False
    # check box
    # finding box cords
    xbox = pos[0] // 3
    ybox = pos[1] // 3

    for i in range(xbox*3, xbox*3 + 3):
        for j in range(ybox*3, ybox*3 + 3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


print("Unsolved Board")
display(Sudoku)
solve_board(Sudoku)
print("Solved Board")
display(Sudoku)
