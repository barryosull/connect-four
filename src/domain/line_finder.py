
from abc import ABC, abstractmethod
from domain.board import Board
from domain.board_dtos import Coord, Line
from domain.checker import Checker


class LineFinder(ABC):

    @abstractmethod
    def lines_with_coord(self, board: Board, checker: Checker, coord: Coord) -> list[Line]:
        pass

    @abstractmethod
    def __str__(self):
        pass

class DefaultLineFinder(LineFinder):

    # Search all lines expanding outward from the coord, stopping at the edges
    def lines_with_coord(self, board: Board, checker: Checker, coord: Coord) -> list[Line]:
        lines = []
        # up, up right, right, down right
        directions = [(0, 1), (1, 1), (1, 0), (1, -1)]
        for direction in directions:
            line = [coord]

            # go direction
            offset = coord
            offset = (offset[0] - direction[0], offset[1] - direction[1])
            while (0 <= offset[0] < board.width() and 0 <= offset[1] < board.height()):
                if board.coord_value(offset) != checker.value:
                    break
                line.insert(0, offset)
                offset = (offset[0] - direction[0], offset[1] - direction[1])

            # go opposite direction
            offset = coord
            offset = (offset[0] + direction[0], offset[1] + direction[1])
            while (0 <= offset[0] < board.width() and 0 <= offset[1] < board.height()):
                if board.coord_value(offset) != checker.value:
                    break
                line.append(offset)
                offset = (offset[0] + direction[0], offset[1] + direction[1])

            if (len(line) > 1):
                lines.append(line)
        return lines
    
    def __str__(self):
        return "Default"
    
class TorusLineFinder(LineFinder):
    def lines_with_coord(self, board: Board, checker: Checker, coord: Coord) -> list[Line]:
        lines = []
        # up, up right, right, down right
        directions = [(0, 1), (1, 1), (1, 0), (1, -1)]
        for direction in directions:
            line = [coord]

            # go direction
            offset = coord
            offset = (
                (offset[0] - direction[0]) % board.width(), 
                (offset[1] - direction[1]) % board.height(),
            )
            while (offset not in line):
                if board.coord_value(offset) != checker.value:
                    break
                line.insert(0, offset)
                offset = (
                    (offset[0] - direction[0]) % board.width(), 
                    (offset[1] - direction[1]) % board.height(),
                )

            # go opposite direction
            offset = coord
            offset = (
                (offset[0] + direction[0]) % board.width(), 
                (offset[1] + direction[1]) % board.height(),
            )
            while (0 <= offset[0] < board.width() and 0 <= offset[1] < board.height()):
                if board.coord_value(offset) != checker.value:
                    break
                line.append(offset)
                offset = (
                    (offset[0] + direction[0]) % board.width(), 
                    (offset[1] + direction[1]) % board.height(),
                )

            if (len(line) > 1):
                lines.append(line)
        return lines

    def __str__(self):
        return "Torus"
