from domain.board import Board, Winner
from domain.checker import Checker
from domain.finders import Finders


class TestFinders:

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
       
        actual = Finders().winning_move(board, Checker.RED, (3, 4))

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

        actual = Finders().winning_move(board, Checker.RED, (3, 2))

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
       
        actual = Finders().winning_move(board, Checker.RED, (1, 2))

        expected = Winner(Checker.RED, [[(1, 2), (2, 3), (3, 4), (4, 5)]])
        print(actual)
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

        actual = Finders().winning_move(board, Checker.RED, (3, 2))

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
        
        actual = Finders().winning_move(board, Checker.RED, (3, 2))

        expected = Winner(
            Checker.RED,
            [
                [(3, 2), (3, 3), (3, 4), (3, 5)],  # Center down
                [(3, 2), (4, 3), (5, 4), (6, 5)],  # Center diagonal down
                [(0, 5), (1, 4), (2, 3), (3, 2)],  # Bottom left diagonal up
            ],
        )
        assert expected == actual

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
       
        actual = Finders().winning_move(board, Checker.RED, (3, 4))

        assert actual is None

    def test_line_making_moves(self):
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

        actual = Finders().line_making_moves(board, Checker.RED)

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