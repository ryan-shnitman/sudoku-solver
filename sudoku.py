class Sudoku:

    board = None
    solveable = None

    def __init__(self, board_str=None):
        if board_str:
            self.board = [list(row) for row in board_str] #build board from specified string
            self.size = len(board_str)
        else:
            self.board = [ [0] * 9 for i in range(9)] #blank sudoku board

    def __repr__(self):
        s = ''
        for r in range(9):
            if r%3 == 0:
                s += '--'*17
                s += '\n'
            for c in range(9):
                if c%3 == 0:
                    s += '| '
                if self.board[r][c] == "0":
                    s += "*  "
                else:
                    s += f"{int(self.board[r][c])}  "
            s += '|'
            s += "\n"
        s += '--'*17
        return s
    
    def solve(self):
        def check(x,r,c,board):
            ''' helper function to check if x in board[r][c] doesn't clash; returns bool '''
            if x not in board[r]: #valid for row
                if x not in [board[row][c] for row in range(len(board))]: #valid for col
                    if x not in [ [board[row][col] for col in range(c//3*3, c//3*3+3)] for row in range(r//3*3, r//3*3+3)]: #valid for 3x3 grid
                        return True
            return False
        
        def backtrack(board):
            for r in range(9):
                for c in range(9):
                    if board[r][c] == '0':
                        for x in range(1,10):
                            if check(str(x),r,c,board):
                                board[r][c] = str(x)
                                return backtrack(board)
                        return False
            return True
        
        return backtrack(self.board)
                                


def main():
    sudoku = Sudoku(['530070000',
                    '600195000',
                    '098000060',
                    '800060003',
                    '400803001',
                    '700020006',
                    '060000280',
                    '000419005',
                    '000080079'])
    print(sudoku)
    
    print(sudoku.solve())
    
    print(sudoku)
    
main()