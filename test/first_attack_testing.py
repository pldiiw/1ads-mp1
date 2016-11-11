"""First Attack testing unit."""

import unittest
from sys import path
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

    def test_new_board(self):
        self.assertEqual(first_attack.new_board(self.n), self.board)

    def test_not_finish(self):
        unplayable_board = [
            [1, 2, 2],
            [2, 2, 1],
            [2, 2, 2]
        ]
        self.assertTrue(first_attack.not_finish(self.board, self.n))
        self.assertFalse(first_attack.not_finish(unplayable_board, 3))
        self.assertTrue(first_attack.not_finish(self.ingame_board, self.n))

    def test_square_valid(self):
        self.assertTrue(first_attack.square_valid(self.ingame_board,
                                                  self.n, 4, 0))
        self.assertFalse(first_attack.square_valid(self.ingame_board,
                                                   self.n, 1, 3))
        self.assertFalse(first_attack.square_valid(self.ingame_board,
                                                   self.n, 1, 1))
        self.assertFalse(first_attack.square_valid(self.ingame_board,
                                                   self.n, -5, 8))

    def test_update(self):
        board_to_update = deepcopy(self.board)
        first_attack.update(board_to_update, 5, 1, 1)
        self.assertEqual(board_to_update, self.ingame_board)
