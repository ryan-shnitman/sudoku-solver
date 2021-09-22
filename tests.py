import unittest
from time import time
from sudoku import Sudoku
from copy import deepcopy

solvable_board = Sudoku(['530070000',
                             '600195000',
                             '098000060',
                             '800060003',
                             '400803001',
                             '700020006',
                             '060000280',
                             '000419005',
                             '000080079'])

solvable_board_original = deepcopy(solvable_board)

unsolvable_board = Sudoku(['516849732',
                               '307605000',
                               '809700065',
                               '135060907',
                               '472591006',
                               '968370050',
                               '253186074',
                               '684207500',
                               '791050608'])

unsolvable_board_original = deepcopy(unsolvable_board)


class TestSolve(unittest.TestCase):

    def test_solvable(self):
        start = time()
        solvable = solvable_board.solve()
        end = time()
        print(f"Time: {end - start} \n")
        self.assertEqual(solvable, True, "Should be True")

    def test_solvable_board(self):
        self.assertNotEqual(solvable_board.board, solvable_board_original, "Should have been altered")

    def test_unsolvable(self):
        start = time()
        solvable = unsolvable_board.solve()
        end = time()
        print(f"Time: {end - start} \n")
        self.assertEqual(solvable, False, "Should be False")

    def test_unsolvable_board(self):
        self.assertEqual(unsolvable_board.board, unsolvable_board_original.board, "Should be unaltered")



if __name__ == '__main__':
    unittest.main()
