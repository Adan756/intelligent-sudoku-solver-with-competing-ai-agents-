import random

def is_valid(board, row, col, num):
    # row
    for i in range(9):
        if board[row][i] == num:
            return False

    # col
    for i in range(9):
        if board[i][col] == num:
            return False

    # box
    start_row, start_col = 3*(row//3), 3*(col//3)
    for i in range(3):
        for j in range(3):
            if board[start_row+i][start_col+j] == num:
                return False

    return True


def solve(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                nums = list(range(1,10))
                random.shuffle(nums)

                for num in nums:
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve(board):
                            return True
                        board[row][col] = 0

                return False
    return True


def generate_sudoku(difficulty="easy"):
    board = [[0]*9 for _ in range(9)]
    solve(board)

    # remove numbers
    difficulty_map = {
        "easy": 30,
        "medium": 40,
        "hard": 50,
        "extreme": 55,
        "expert": 60
    }

    remove = difficulty_map.get(difficulty, 40)

    for _ in range(remove):
        row = random.randint(0,8)
        col = random.randint(0,8)
        board[row][col] = 0

    return board