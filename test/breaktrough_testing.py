"""Breaktrough testing unit."""

import sys
import unittest
sys.path.append('..')
from src import breaktrough

class BreaktroughTests(unittest.TestCase):
    """All breaktrough testing methods.
    """

    def setUp(self):
        self.width = 3
        self.height = 5
        self.board = [
            [1, 1, 1],
            [1, 1, 1],
            [0, 0, 0],
            [2, 2, 2],
            [2, 2, 2]
        ]

    def test_new_board(self):
        self.assertEqual(
            breaktrough.new_board(self.height, self.width),
            self.board)

    def test_coordinates_within_board(self):
        # Inside board
        self.assertTrue(
            breaktrough.coordinates_within_board(self.height, self.width, 1, 3)
        )
        # Outside board
        self.assertFalse(
            breaktrough.coordinates_within_board(self.height, self.width, 5, 0)
        )
        self.assertFalse(
            breaktrough.coordinates_within_board(self.height, self.width, 0, 8)
        )
        self.assertFalse(
            breaktrough.coordinates_within_board(self.height, self.width, -2, 6)
        )

    def test_pawn_exist(self):
        # White pawn
        self.assertTrue(
            breaktrough.pawn_exist(self.board, 0, 0)
        )
        # Black pawn
        self.assertTrue(
            breaktrough.pawn_exist(self.board, 0, 4)
        )
        # Empty square
        self.assertFalse(
            breaktrough.pawn_exist(self.board, 0, 2)
        )

    def test_pawn_belong_to_player(self):
        self.assertTrue(
            breaktrough.pawn_belong_to_player(self.board, 1, 0, 0)
        )
        self.assertFalse(
            breaktrough.pawn_belong_to_player(self.board, 2, 1, 2)
        )

    def test_move_direction(self):
        self.assertEqual(
            breaktrough.move_direction(1),
            1
        )
        self.assertEqual(
            breaktrough.move_direction(2),
            -1
        )

    def test_pawn_facing_squares(self):
        self.assertEqual(
            breaktrough.pawn_facing_squares(self.board, self.height, 1, 2, 1),
            [0, 0]
        )
        self.assertEqual(
            breaktrough.pawn_facing_squares(self.board, self.height, 2, 1, 3),
            [0, 0, 0]
        )
        self.assertEqual(
            breaktrough.pawn_facing_squares(self.board, self.height, 2, 0, 4),
            [2, 2]
        )

    def test_pawn_facing_columns(self):
        long_board = [
            [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1],
            [0, 1, 1, 1, 2, 1, 0, 2, 0, 0, 0]
        ]
        self.assertEqual(
            breaktrough.pawn_facing_columns(self.width, 2),
            [1, 2]
        )
        self.assertEqual(
            breaktrough.pawn_facing_columns(len(long_board[0]), 8),
            [7, 8, 9]
        )
        self.assertEqual(
            breaktrough.pawn_facing_columns(len(long_board[0]), 10),
            [9, 10]
        )
        self.assertEqual(
            breaktrough.pawn_facing_columns(len(long_board[0]), 0),
            [0, 1]
        )


    def test_pawn_can_move(self):
        self.assertTrue(
            breaktrough.pawn_can_move(self.board, self.height, 1, 0, 1)
        )
        self.assertTrue(
            breaktrough.pawn_can_move(self.board, self.height, 2, 3, 2)
        )
        self.assertFalse(
            breaktrough.pawn_can_move(self.board, self.height, 2, 4, 1)
        )

    def test_pawn_available_moves(self):
        long_board = [
            [1, 0, 1, 1, 0, 1, 0, 0, 1, 1, 1],
            [0, 1, 1, 1, 2, 1, 0, 2, 0, 0, 0]
        ]
        self.assertEqual(
            breaktrough.pawn_available_moves(long_board,
                                             len(long_board),
                                             len(long_board[0]),
                                             1,
                                             10,
                                             0
                                            ),
            [9, 10]
        )
        self.assertEqual(
            breaktrough.pawn_available_moves(long_board,
                                             len(long_board),
                                             len(long_board[0]),
                                             2,
                                             7,
                                             1
                                            ),
            [6, 7, 8]
        )
        self.assertEqual(
            breaktrough.pawn_available_moves(long_board,
                                             len(long_board),
                                             len(long_board[0]),
                                             1,
                                             2,
                                             0
                                            ),
            []
        )

    def test_move_pawn(self):
        board = [
            [1, 0],
            [2, 0]
        ]
        board_after = [
            [0, 0],
            [1, 0]
        ]
        breaktrough.move_pawn(board, 0, 0, 0)
        self.assertEqual(board, board_after)

    def test_flatten(self):
        two_dim_l = [
            [1, 2, 3, 4],
            [5, 6],
            [7, 8, 9],
            [10]
        ]
        one_dim_l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        self.assertEqual(
            breaktrough.flatten(two_dim_l),
            one_dim_l
        )

    def test_still_has_pawns(self):
        no_black = [
            [0, 0],
            [1, 0],
            [0, 0]
        ]
        no_white = [
            [2, 0],
            [0, 2],
            [0, 2]
        ]
        self.assertFalse(
            breaktrough.still_has_pawns(no_black, 2)
        )
        self.assertFalse(
            breaktrough.still_has_pawns(no_white, 1)
        )
        self.assertTrue(
            breaktrough.still_has_pawns(self.board, 2)
        )
        self.assertTrue(
            breaktrough.still_has_pawns(self.board, 1)
        )

    def test_someone_won(self):
        black_reached_line_board = [
            [1, 1, 2],
            [0, 1, 0],
            [0, 2, 2]
        ]
        white_reached_line_board = [
            [0, 0, 0],
            [0, 1, 0],
            [1, 2, 2]
        ]
        white_supremacy_board = [
            [1, 1, 0],
            [0, 0, 1],
            [0, 0, 0]
        ]
        black_supremacy_board = [
            [0, 0, 0],
            [0, 2, 0],
            [0, 0, 0]
        ]
        self.assertTrue(
            breaktrough.someone_won(black_reached_line_board)
        )
        self.assertTrue(
            breaktrough.someone_won(white_reached_line_board)
        )
        self.assertTrue(
            breaktrough.someone_won(black_supremacy_board)
        )
        self.assertTrue(
            breaktrough.someone_won(white_supremacy_board)
        )
        self.assertFalse(
            breaktrough.someone_won(self.board)
        )

    def test_select_random_pawn(self):
        white_unique_choice = [
            [0, 1, 1],
            [0, 1, 1],
            [1, 1, 1]
        ]
        black_unique_choice = [
            [2, 2, 2],
            [2, 0, 2],
            [0, 0, 2]
        ]
        self.assertTrue(
            breaktrough.select_random_pawn(white_unique_choice,
                                           len(white_unique_choice),
                                           len(white_unique_choice[0]),
                                           1
                                          ),
            (1, 0)
        )
        self.assertTrue(
            breaktrough.select_random_pawn(black_unique_choice,
                                           len(black_unique_choice),
                                           len(black_unique_choice[0]),
                                           2
                                          ),
            (2, 2)
        )

    def test_ai_turn(self):
        black_line_reach = [
            [1, 1, 1],
            [2, 2, 2],
            [2, 2, 2]
        ]
        white_supremacy = [
            [1],
            [2],
            [0]
        ]
        self.assertTrue(
            breaktrough.ai_turn(black_line_reach,
                                len(black_line_reach),
                                len(black_line_reach[0]),
                                2
                               ),
            2
        )
        self.assertTrue(
            breaktrough.ai_turn(white_supremacy,
                                len(white_supremacy),
                                len(white_supremacy[0]),
                                1
                               ),
            1
        )

if __name__ == "__main__":
    unittest.main()
