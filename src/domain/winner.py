from domain.board_dtos import Coord
from domain.checker import Checker

class Winner:
    def __init__(self, checker: Checker, lines: list[list[Coord]]):
        self.checker = checker
        self.lines = lines        

    def __eq__(self, other):
        if not isinstance(other, Winner):
            return False
        return self.checker == other.checker and self.lines == other.lines

    def is_in_list(self, coord: Coord) -> bool:
        for line in self.lines:
            if coord in line:
                return True
        return False
