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

    def test_can_still_play(self):
        unplayable_board = [
            [0, 0, 0, 0],
            [0, 1, 0, 1],
            [0, 0, 1, 2],
            [0, 1, 2, 2]
        ]

        self.assertTrue(pleiadis.can_still_play(self.board, 4, 1))
        self.assertTrue(pleiadis.can_still_play(self.board, 4, 2))
        self.assertTrue(pleiadis.can_still_play(self.ingame_board, 4, 1))
        self.assertTrue(pleiadis.can_still_play(self.ingame_board, 4, 1))
        self.assertTrue(pleiadis.can_still_play(unplayable_board, 4, 1))
        self.assertFalse(pleiadis.can_still_play(unplayable_board, 4, 2))

    def test_get_adjacent_squares(self):
        self.assertEqual(
            pleiadis.get_adjacent_squares(self.ingame_board, 2, 2),
            [1, 0, 0, 0, 0, 0, 0, 2]
        )
        self.assertEqual(
            pleiadis.get_adjacent_squares(self.ingame_board, 3, 0),
            [0, 0, 0]
        )

    def test_get_non_sym_pawns(self):
        board = [
            [0, 0, 2, 0, 0],
            [1, 1, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 1, 0, 2, 1],
        ]

        self.assertEqual(
            pleiadis.get_non_sym_pawns(board, 5, 2),
            [(0, 1), (1, 1), (1, 4)]
        )
        self.assertEqual(
            pleiadis.get_non_sym_pawns(board, 5, 1),
            [(2, 0), (3, 4)]
        )

    def test_select_random_square(self):
        board = [
            [1, 0, 0, 0, 1],
            [0, 0, 0, 0, 0],
            [0, 1, 2, 1, 0],
            [0, 1, 0, 1, 0],
            [0, 0, 0, 0, 0]
        ]
        board_two = [
            [0, 0, 0, 2],
            [0, 2, 0, 2],
            [2, 0, 0, 0],
            [0, 2, 0, 0]
        ]

        self.assertEqual(
            pleiadis.select_random_square(board, 5, 2),
            (2, 0)
        )
        self.assertEqual(
            pleiadis.select_random_square(board_two, 4, 1),
            (3, 3)
        )

if __name__ == "__main__":
    unittest.main()
