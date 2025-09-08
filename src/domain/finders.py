from domain.board import Board
from domain.board_dtos import Coord, Moves
from domain.checker import Checker
from domain.winner import Winner
from domain.line_finder import LineFinder, DefaultLineFinder


class Finders:

    WIN_LENGTH = 4

    __line_finder: LineFinder

    def __init__(self, line_finder: LineFinder = DefaultLineFinder()):
        self.__line_finder = line_finder

    def winning_move(self, board: Board, checker: Checker, coord: Coord) -> Winner | None:
        lines_with_coord = self.__line_finder.lines_with_coord(board, checker, coord)

        winning_lines = list(
            filter(lambda line: len(line) >= self.WIN_LENGTH, lines_with_coord)
        )

        # Check for winners
        if len(winning_lines) == 0:
            return None

        return Winner(checker, winning_lines)

    def line_making_moves(self, board: Board, checker: Checker) -> Moves:
        available_coords = board.available_coords()
        moves = {}
        for coord in available_coords:
            lines_with_coord = self.__line_finder.lines_with_coord(board, checker, coord)

            if len(lines_with_coord) > 0:
                moves[coord] = lines_with_coord
        return moves
        