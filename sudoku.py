import copy
import requests


class Sudoku:
    board = None

    def __init__(self, board_str=None, difficulty="easy"):
        # build board from string if provided
        if board_str:
            self.board = [list(row) for row in board_str]
        # if no board provided, grab random board from website of specified difficulty
        else:
            response = requests.get(f"https://sugoku.herokuapp.com/board?difficulty={difficulty}")
            board = response.json()['board']
            self.board = [[str(board[r][c]) for c in range(9)] for r in range(9)]

    def __repr__(self):
        s = ''
        for r in range(9):
            if r % 3 == 0:
                s += '--' * 17
                s += '\n'
            for c in range(9):
                if c % 3 == 0:
                    s += '| '
                if self.board[r][c] == "0":
                    s += "*  "
                else:
                    s += f"{int(self.board[r][c])}  "
            s += '|'
            s += "\n"
        s += '--' * 17
        return s

    def solve(self):

        def check(x, r, c, board):
            """ helper function to check if x in board[r][c] doesn't clash; returns bool """
            if x not in board[r]:  # valid for row
                if x not in [board[row][c] for row in range(len(board))]:  # valid for col
                    grid = []
                    for i in range(r // 3 * 3, r // 3 * 3 + 3):
                        for j in range(c // 3 * 3, c // 3 * 3 + 3):
                            grid.append(board[i][j])
                    if x not in grid:  # valid for 3x3 grid
                        return True
            return False

        def board_update(x, r, c, board):
            """ helper function to update board[r][c] to x and return the new board """
            new_board = copy.deepcopy(board)
            new_board[r][c] = x
            return new_board

        def backtrack(board):
            """ recursive function to fill empty cells with valid assignments and backtrack when not possible """
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '0':
                        pos_vals = []
                        for x in range(1, 10):
                            if check(str(x), r, c, board):
                                pos_vals.append(str(x))
                        if pos_vals:
                            return any([backtrack(board_update(x, r, c, board)) for x in pos_vals])
                        else:
                            return False
            self.board = board
            return True

        copy_board = copy.deepcopy(self.board[:])  # duplicate self.board to pass into backtrack
        return backtrack(copy_board)
