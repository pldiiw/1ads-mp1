"""First Attack testing unit."""

import unittest
from sys import path, argv
from copy import deepcopy
path.append('..')
from src import first_attack

class FirstAttackTests(unittest.TestCase):
    """All First Attack testing methods."""

    def setUp(self):
        self.n = 5
        self.board = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]
        self.ingame_board = [
            [2, 2, 2, 0, 0],
            [2, 1, 2, 2, 2],
            [2, 2, 2, 0, 0],
            [0, 2, 0, 2, 0],
            [0, 2, 0, 0, 2]
        ]
        self.bicolor_ingame_board = [
            [5, 5, 2, 2, 1],
            [3, 4, 4, 5, 5],
            [4, 4, 2, 0, 2],
            [4, 2, 4, 0, 2],
            [5, 0, 0, 4, 2]
        ]

    def test_new_board(self):
        self.assertEqual(first_attack.new_board(self.n), self.board)

    def test_not_finish(self):
        unplayable_board = [
            [1, 2, 2],
            [2, 2, 1],
            [2, 2, 2]
        ]
        bicolor_unplayable_board = [
            [1, 5, 3],
            [3, 5, 1],
            [5, 5, 5]
        ]

        argv[2] = '0'
        self.assertTrue(first_attack.not_finish(self.board))
        self.assertFalse(first_attack.not_finish(unplayable_board))
        self.assertTrue(first_attack.not_finish(self.ingame_board))

        argv[2] = '1'
        self.assertTrue(first_attack.not_finish(self.bicolor_ingame_board))
        self.assertFalse(first_attack.not_finish(bicolor_unplayable_board))

    def test_square_valid(self):
        argv[2] = '0'
        self.assertTrue(first_attack.square_valid(self.ingame_board,
                                                  self.n, 1, 4, 0))
        self.assertFalse(first_attack.square_valid(self.ingame_board,
                                                   self.n, 3, 1, 3))
        self.assertFalse(first_attack.square_valid(self.ingame_board,
                                                   self.n, 1, 1, 1))
        self.assertFalse(first_attack.square_valid(self.ingame_board,
                                                   self.n, 1, -5, 8))

        argv[2] = '1'
        self.assertTrue(first_attack.square_valid(self.bicolor_ingame_board,
                                                  self.n, 1, 3, 2))
        self.assertTrue(first_attack.square_valid(self.bicolor_ingame_board,
                                                  self.n, 1, 2, 1))
        self.assertFalse(first_attack.square_valid(self.bicolor_ingame_board,
                                                   self.n, 1, 4, 4))
        self.assertFalse(first_attack.square_valid(self.bicolor_ingame_board,
                                                   self.n, 1, 0, 4))
        self.assertTrue(first_attack.square_valid(self.bicolor_ingame_board,
                                                  self.n, 3, 1, 4))
        self.assertTrue(first_attack.square_valid(self.bicolor_ingame_board,
                                                  self.n, 3, 1, 3))
        self.assertFalse(first_attack.square_valid(self.bicolor_ingame_board,
                                                   self.n, 3, 3, 4))
        self.assertFalse(first_attack.square_valid(self.bicolor_ingame_board,
                                                   self.n, 3, 4, 1))
        self.assertFalse(first_attack.square_valid(self.bicolor_ingame_board,
                                                   self.n, 3, 4, 0))

    def test_update(self):
        board_to_update = deepcopy(self.board)
        bicolor_board_to_update = deepcopy(self.board)

        argv[2] = '0'
        first_attack.update(board_to_update, 1, 1, 1)
        self.assertEqual(board_to_update, self.ingame_board)

        argv[2] = '1'
        first_attack.update(bicolor_board_to_update, 1, 4, 0)
        first_attack.update(bicolor_board_to_update, 3, 0, 1)
        self.assertEqual(bicolor_board_to_update, self.bicolor_ingame_board)

if __name__ == "__main__":
    unittest.main()
