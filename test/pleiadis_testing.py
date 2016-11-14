"""Pleaidis unit test."""

import unittest
from sys import path
path.append('..')
from src import pleiadis

class PleiadisTests(unittest.TestCase):
    """All Pleiadis testing methods."""

    def setUp(self):
        self.n = 4
        self.board = [
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0],
            [0, 0, 0, 0]
        ]
        self.ingame_board = [
            [0, 0, 0, 0],
            [0, 1, 0, 0],
            [0, 0, 1, 0],
            [0, 0, 0, 2]
        ]

    def test_new_board(self):
        self.assertEqual(pleiadis.new_board(self.n), self.board)

    def test_square_valid(self):
        self.assertFalse(
            pleiadis.square_valid(self.ingame_board, self.n, 1, 6, -2)
        )
        self.assertTrue(
            pleiadis.square_valid(self.ingame_board, self.n, 2, 3, 2)
        )
        self.assertFalse(
            pleiadis.square_valid(self.ingame_board, self.n, 2, 2, 1)
        )
        self.assertTrue(
            pleiadis.square_valid(self.ingame_board, self.n, 1, 3, 0)
        )
        self.assertFalse(
            pleiadis.square_valid(self.ingame_board, self.n, 1, 3, 3)
        )
        self.assertFalse(
            pleiadis.square_valid(self.ingame_board, self.n, 1, 1, 1)
        )

    def test_count(self):
        self.assertEqual(
            pleiadis.count([1, 1, 0, 4, 5, 1, 1, 8, 0, 0, 1], 1),
            5
        )
        self.assertEqual(pleiadis.count(['ab', 'bc', 'ab'], 'ab'), 2)
        self.assertEqual(pleiadis.count([[1, 1], [0, 0], [1, 2]], [1, 2]), 1)

    def test_not_finish(self):
        unplayable_board = [
            [0, 0, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 2],
            [0, 1, 2, 2]
        ]
        self.assertTrue(pleiadis.not_finish(self.board, 4))
        self.assertTrue(pleiadis.not_finish(self.ingame_board, 4))
        self.assertFalse(pleiadis.not_finish(unplayable_board, 4))

    def test_get_adjacent_squares(self):
        self.assertEqual(
            pleiadis.get_adjacent_squares(self.ingame_board, 2, 2),
            [1, 0, 0, 0, 0, 0, 0, 2]
        )
        self.assertEqual(
            pleiadis.get_adjacent_squares(self.ingame_board, 3, 0),
            [0, 0, 0]
        )

if __name__ == "__main__":
    unittest.main()
