from Quoridor import Cell, Board, Player, QuoridorGame
import unittest


class UnitTests(unittest.TestCase):

    def test_QuoridorGame_place_fence(self):
        """Test place_fence method"""

        # create game object
        q = QuoridorGame()

        # test bad input
        self.assertFalse(q.place_fence(1, 7, (6, 5)))  # no h or v
        self.assertFalse(q.place_fence(4, 'h', (6, 5)))  # no player 4
        self.assertFalse(q.place_fence(1, 'h', 'z'))  # not a tuple

        # ----------------------------- horizontal tests ------------------------------------
        # player 1 places fence at col 6 row 5
        self.assertTrue(q.place_fence(1, 'h', (6, 5)))  # player 1: 9 fences remaining

        # player 1 attempts to place fence at col 7 row 5 out of turn
        self.assertFalse(q.place_fence(1, 'h', (7, 5)))

        # player 2 attempts to place fence at col 6 row 5
        self.assertFalse(q.place_fence(2, 'h', (6, 5)))

        # player 2 attempts to place fence at col 6 row 0
        self.assertFalse(q.place_fence(2, 'h', (6, 0)))

        # player 2 places fence at col 6 row 1
        self.assertTrue(q.place_fence(2, 'h', (6, 1)))  # player 2: 9 fences remaining

        # player 1 attempts to place fence at col 6 row 5
        self.assertFalse(q.place_fence(1, 'h', (6, 5)))

        # player 1 attempts to place fence at col 7 row 0
        self.assertFalse(q.place_fence(1, 'h', (7, 0)))

        # player 1 places fence at col 7 row 5
        self.assertTrue(q.place_fence(1, 'h', (7, 5)))  # player 1: 8 fences remaining

        # player 2 places fence at col 0 row 4
        self.assertTrue(q.place_fence(2, 'h', (0, 4)))  # player 2: 8 fences remaining

        # ----------------------------- vertical tests ------------------------------------
        # player 1 places fence at col 6 row 5
        self.assertTrue(q.place_fence(1, 'v', (6, 5)))  # player 1: 7 fences remaining

        # player 1 attempts to place fence at col 7 row 5 out of turn
        self.assertFalse(q.place_fence(1, 'v', (7, 5)))

        # player 2 attempts to place fence at col 6 row 5
        self.assertFalse(q.place_fence(2, 'v', (6, 5)))

        # player 2 attempts to place fence at col 0 row 6
        self.assertFalse(q.place_fence(2, 'v', (0, 6)))

        # player 2 places fence at col 6 row 1
        self.assertTrue(q.place_fence(2, 'v', (6, 1)))  # player 2: 7 fences remaining

        # player 1 attempts to place fence at col 6 row 5
        self.assertFalse(q.place_fence(1, 'v', (6, 5)))

        # player 1 attempts to place fence at col 0 row 7
        self.assertFalse(q.place_fence(2, 'v', (0, 7)))

        # player 1 places fence at col 7 row 5
        self.assertTrue(q.place_fence(1, 'v', (7, 5)))  # player 1: 6 fences remaining

        # player 2 places fence at col 5 row 0
        self.assertTrue(q.place_fence(2, 'v', (5, 0)))  # player 2: 6 fences remaining

        # ----------------------------- fence limit test ------------------------------------
        # player 1 places fence at col 8 row 5
        self.assertTrue(q.place_fence(1, 'v', (8, 5)))  # player 1: 5 fences remaining

        # player 2 places fence at col 4 row 0
        self.assertTrue(q.place_fence(2, 'v', (4, 0)))  # player 2: 5 fences remaining

        # player 1 places fence at col 4 row 4
        self.assertTrue(q.place_fence(1, 'h', (4, 4)))  # player 1: 4 fences remaining

        # player 2 places fence at col 4 row 8
        self.assertTrue(q.place_fence(2, 'h', (4, 8)))  # player 2: 4 fences remaining

        # player 1 places fence at col 1 row 4
        self.assertTrue(q.place_fence(1, 'h', (1, 4)))  # player 1: 3 fences remaining

        # player 2 places fence at col 1 row 8
        self.assertTrue(q.place_fence(2, 'h', (1, 8)))  # player 2: 3 fences remaining

        # player 1 places fence at col 2 row 4
        self.assertTrue(q.place_fence(1, 'h', (2, 4)))  # player 1: 2 fences remaining

        # player 2 places fence at col 2 row 8
        self.assertTrue(q.place_fence(2, 'h', (2, 8)))  # player 2: 2 fences remaining

        # player 1 places fence at col 3 row 4
        self.assertTrue(q.place_fence(1, 'h', (3, 4)))  # player 1: 1 fences remaining

        # player 2 places fence at col 3 row 8
        self.assertTrue(q.place_fence(2, 'h', (3, 8)))  # player 2: 1 fences remaining

        # player 1 places fence at col 3 row 4
        self.assertTrue(q.place_fence(1, 'v', (3, 4)))  # player 1: 0 fences remaining

        # player 2 places fence at col 3 row 8
        self.assertTrue(q.place_fence(2, 'v', (3, 8)))  # player 2: 0 fences remaining

        # player 1 places fence at col 3 row 7
        self.assertFalse(q.place_fence(1, 'v', (3, 7)))  # player 1: no fences!

        # player 2 places fence at col 3 row 7
        self.assertFalse(q.place_fence(2, 'v', (3, 7)))  # player 2: no fences!


    def test_QuoridorGame_move_pawn(self):
        """Test move_pawn method"""

        # create game object
        q = QuoridorGame()

        # ----------------------------- fence blocking test ------------------------------------
        # player 1 blocks player 2 pawn
        self.assertTrue(q.place_fence(1, 'h', (4, 8)))

        # player 2 attempts to move through fence
        self.assertFalse(q.move_pawn(2, (4, 7)))

        # player 2 attempts to move too far away
        self.assertFalse(q.move_pawn(2, (8, 7)))

        # player 2 attempts to move too far away
        self.assertFalse(q.move_pawn(2, (7, 8)))

        # player 2 sidesteps fence
        self.assertTrue(q.move_pawn(2, (5, 8)))

        # player 1 blocks player 2 pawn again
        self.assertTrue(q.place_fence(1, 'h', (5, 8)))

        # player 2 attempts to move through fence
        self.assertFalse(q.move_pawn(2, (5, 7)))

        # player 2 sidesteps fence
        self.assertTrue(q.move_pawn(2, (6, 8)))

        # player 1 attempts a diagonal move
        self.assertFalse(q.move_pawn(1, (5, 1)))

        # player 1 attempts to move off board
        self.assertFalse(q.move_pawn(1, (4, -1)))

        # player 1 moves
        self.assertTrue(q.move_pawn(1, (4, 1)))

        # player 2 blocks player 1
        self.assertTrue(q.place_fence(2, 'h', (4, 2)))

        # player 1 attempts to move through fence
        self.assertFalse(q.move_pawn(1, (4, 2)))

        # player 1 sidesteps fence
        self.assertTrue(q.move_pawn(1, (5, 1)))

        # player 2 blocks player 1 again
        self.assertTrue(q.place_fence(2, 'v', (5, 1)))

        # player 1 attempts to move through fence
        self.assertFalse(q.move_pawn(1, (4, 1)))

        # player 1 moves
        self.assertTrue(q.move_pawn(1, (5, 2)))

        # player 2 blocks player 1 again
        self.assertTrue(q.place_fence(2, 'v', (6, 2)))

        # player 1 attempts to move through fence
        self.assertFalse(q.move_pawn(1, (6, 2)))

        # player 1 moves
        self.assertTrue(q.move_pawn(1, (5, 3)))

        # player 2 blocks player 1 backward movement
        self.assertTrue(q.place_fence(2, 'h', (5, 3)))

        # player 1 attempts to move through fence
        self.assertFalse(q.move_pawn(1, (5, 2)))

        # ----------------------------- pawn face-off test ------------------------------------

        # player 1 moves
        self.assertTrue(q.move_pawn(1, (5, 4)))

        # player 2 moves
        self.assertTrue(q.move_pawn(2, (6, 7)))

        # player 1 moves
        self.assertTrue(q.move_pawn(1, (5, 5)))

        # player 2 moves
        self.assertTrue(q.move_pawn(2, (6, 6)))

        # player 1 moves
        self.assertTrue(q.move_pawn(1, (5, 6)))  # face-off

        # player 2 attempts to move into opponent
        self.assertFalse(q.move_pawn(2, (5, 6)))

        # player 2 attempts to move diagonally with no fence
        self.assertFalse(q.move_pawn(2, (5, 5)))

        # player 2 jumps over opponent
        self.assertTrue(q.move_pawn(2, (4, 6)))

        q.print_board()
