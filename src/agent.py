
from board import Board, Coord, Line
from checker import Checker

type AvailableLines = dict(Coord, list[Line])

class Agent:

    def select_next_slot(self, checker: Checker, board: Board) -> int:
        return 0

