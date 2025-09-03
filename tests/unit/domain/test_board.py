from domain.board import Board, Winner
from domain.checker import Checker


class TestBoard:

    def test_width(self):
        board = Board()
        assert board.width() == 7

    def test_height(self):
        board = Board()
        assert board.height() == 6

    def test_drop_checker_in_empty_slot(self):
        board = Board()
        checker_coord = board.drop_checker(Checker.RED, 2)
        assert checker_coord == (2, 5)

    def test_drop_checker_in_half_full_slot(self):
        board = Board()
        board.drop_checker(Checker.RED, 2)
        board.drop_checker(Checker.RED, 2)
        checker_coord = board.drop_checker(Checker.RED, 2)
        assert (2, 3) == checker_coord

    def test_drop_checker_in_full_slot(self):
        board = Board()
        for i in range(0, board.height()):
            board.drop_checker(Checker.RED, 2)

        checker_coord = board.drop_checker(Checker.RED, 2)

        assert checker_coord is None

    def test_is_full(self):
        empty_board = Board()  # Default empty board
        nearly_full_board = Board(
            [
                ["r", "y", "r", "y", "-", "y", "r"],
                ["r", "y", "r", "y", "r", "y", "r"],
                ["y", "r", "y", "r", "y", "r", "y"],
                ["y", "r", "y", "r", "y", "r", "y"],
                ["r", "y", "r", "y", "r", "y", "r"],
                ["r", "y", "r", "y", "r", "y", "r"],
            ]
        )
        full_board = Board(
            [
                ["r", "y", "r", "y", "r", "y", "r"],
                ["r", "y", "r", "y", "r", "y", "r"],
                ["y", "r", "y", "r", "y", "r", "y"],
                ["y", "r", "y", "r", "y", "r", "y"],
                ["r", "y", "r", "y", "r", "y", "r"],
                ["r", "y", "r", "y", "r", "y", "r"],
            ]
        )

        assert not empty_board.is_full()
        assert not nearly_full_board.is_full()
        assert full_board.is_full()

    def test_available_coords(self):
        board = Board(
            [
                ["-", "-", "-", "-", "-", "r", "-"],
                ["-", "-", "-", "-", "r", "r", "y"],
                ["-", "-", "-", "y", "r", "r", "y"],
                ["-", "-", "r", "y", "y", "y", "r"],
                ["-", "r", "y", "r", "y", "r", "y"],
                ["-", "y", "r", "y", "r", "y", "r"],
            ]
        )

        coords = board.available_coords()

        expected = [(0, 5), (1, 3), (2, 2), (3, 1), (4, 0), (6, 0)]
        assert coords == expected

