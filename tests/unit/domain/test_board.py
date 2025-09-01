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

    def test_find_winner_none(self):
        board = Board(
            [
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["y", "r", "y", "r", "y", "r", "y"],
                ["y", "r", "y", "r", "y", "r", "y"],
            ]
        )
        last_move_coord = (3, 4)

        actual = board.find_winner(Checker.RED, last_move_coord)

        assert actual is None

    def test_find_winner_horizontal(self):
        board = Board(
            [
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "y", "-"],
                ["y", "r", "r", "r", "r", "y", "y"],
                ["r", "y", "r", "r", "y", "r", "y"],
            ]
        )
        last_move_coord = (3, 4)

        actual = board.find_winner(Checker.RED, last_move_coord)

        expected = Winner(Checker.RED, [[(1, 4), (2, 4), (3, 4), (4, 4)]])
        assert expected == actual

    def test_find_winner_vertical(self):
        board = Board(
            [
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "r", "-", "-", "-"],
                ["-", "-", "-", "r", "y", "-", "-"],
                ["-", "-", "-", "r", "y", "-", "y"],
                ["r", "y", "r", "r", "r", "y", "r"],
            ]
        )
        last_move_coord = (3, 2)

        actual = board.find_winner(Checker.RED, last_move_coord)

        expected = Winner(Checker.RED, [[(3, 2), (3, 3), (3, 4), (3, 5)]])
        assert expected == actual

    def test_find_winner_diagonally_down(self):
        board = Board(
            [
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "r", "-", "-", "-", "-", "-"],
                ["-", "y", "r", "-", "-", "-", "-"],
                ["y", "r", "y", "r", "y", "r", "y"],
                ["r", "y", "r", "y", "r", "y", "r"],
            ]
        )
        last_move_coord = [1, 2]

        actual = board.find_winner(Checker.RED, last_move_coord)

        expected = Winner(Checker.RED, [[(1, 2), (2, 3), (3, 4), (4, 5)]])
        assert expected == actual

    def test_find_winner_diagonally_up(self):
        board = Board(
            [
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "r", "-", "-", "-"],
                ["-", "y", "r", "y", "-", "-", "-"],
                ["y", "r", "y", "r", "y", "r", "y"],
                ["r", "y", "r", "y", "r", "y", "r"],
            ]
        )
        last_move_coord = (3, 2)

        actual = board.find_winner(Checker.RED, last_move_coord)

        expected = Winner(Checker.RED, [[(0, 5), (1, 4), (2, 3), (3, 2)]])
        assert expected == actual

    def test_find_winner_with_multiple_win_lines(self):
        board = Board(
            [
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "r", "-", "-", "-"],
                ["-", "-", "r", "r", "r", "-", "-"],
                ["-", "r", "y", "r", "y", "r", "-"],
                ["r", "y", "y", "r", "y", "y", "r"],
            ]
        )
        last_move_coord = (3, 2)

        actual = board.find_winner(Checker.RED, last_move_coord)

        expected = Winner(
            Checker.RED,
            [
                [(3, 2), (3, 3), (3, 4), (3, 5)],  # Center down
                [(3, 2), (4, 3), (5, 4), (6, 5)],  # Center diagonal down
                [(0, 5), (1, 4), (2, 3), (3, 2)],  # Bottom left diagonal up
            ],
        )
        assert expected == actual

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

    def test_find_line_making_moves(self):
        board = Board(
            [
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "y", "r", "-", "r", "y", "-"],
            ]
        )

        actual = board.find_line_making_moves("r")

        expected = {
            (1, 4): [
                [(1, 4), (2, 5)],
            ],
            (2, 4): [[(2, 4), (2, 5)]],
            (3, 5): [[(2, 5), (3, 5), (4, 5)]],
            (4, 4): [
                [(4, 4), (4, 5)],
            ],
            (5, 4): [[(4, 5), (5, 4)]],
        }
        assert actual == expected
