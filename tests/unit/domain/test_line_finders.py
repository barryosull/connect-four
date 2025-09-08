
from domain.board import Board
from domain.checker import Checker
from domain.line_finder import TorusLineFinder

class TestTorusLineFinder:

    def test_finds_lines_looping_around_edges(self):
        board = Board(
            [
                ["y", "y", "-", "-", "-", "-", "y"],
                ["r", "y", "-", "-", "-", "-", "y"],
                ["r", "y", "-", "-", "-", "-", "r"],
                ["y", "r", "-", "-", "-", "y", "r"],
                ["y", "r", "r", "y", "r", "y", "y"],
                ["r", "y", "r", "r", "y", "r", "y"],
            ]
        )
       
        lines = TorusLineFinder().lines_with_coord(board, Checker.YELLOW, (0, 0))

        print(lines)

        expected = [
            [(5, 4), (6, 5), (0, 0), (1, 1)], # Down diagonal
            [(6, 0), (0, 0), (1, 0)],         # Horizontal 
            [(6, 1), (0, 0), (1, 5)]          # Up diagonal
        ]

        assert lines == expected
