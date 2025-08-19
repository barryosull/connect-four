
from typing import Self
from domain.checker import Checker
type BoardCells = list[list[str]]
type Coord = tuple[int, int]
type Line = list[Coord]
type Moves = dict[Coord, list[Line]]

# Should be moved to own file
class Winner:

    def __init__(self, checker: Checker, lines: list[list[Coord]]):
        self.checker = checker
        self.lines = lines

    def __eq__(self, other: Self):
        return self.checker == other.checker and self.lines == other.lines

    def is_in_list(self, coord: Coord) -> bool:
        for line in self.lines:
            if coord in line:  
                return True
        return False

class Board:

    WIN_LENGTH = 4

    def __init__(self, cells: BoardCells|None = None):
        self.__cells = [row[:] for row in cells] if cells is not None else [
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-']
        ]

    #############
    # Comannds 
    #############
    
    def drop_checker(self, checker: Checker, slot: int) -> Coord|None:
        coord = self.find_free_coord(slot)
        if (coord is None):
            return None
        self.__cells[coord[1]][coord[0]] = checker.value
        return coord

    
    #############
    # Queries 
    #############

    def width(self) -> int:
        return len(self.__cells[0])

    def height(self) -> int:
        return len(self.__cells)

    def find_free_coord(self, slot: int) -> Coord|None:
        x = slot        
        for i in range (0, self.height()): 
            y = self.height() - 1 - i
            if self.__cells[y][x] == '-':
                return (x, y)
        return None

    def is_valid_drop(self, slot: int) -> bool: 
        return self.find_free_coord(slot) is not None

    def is_full(self) -> bool:
        return '-' not in self.__cells[0]

    def export_cells(self) -> BoardCells:
        return self.__cells

    def find_winner(self, checker: Checker, coord: Coord) -> Winner|None:
        [x, y] = coord

        lines_with_coord = self.find_lines_with_coord(checker, coord)
    
        winning_lines = list(filter(lambda line: len(line) >= self.WIN_LENGTH , lines_with_coord))
        
        # Check for winners
        if len(winning_lines) == 0:
            return None

        return Winner(checker, winning_lines)

    # Search all lines expanding outward from the coord
    def find_lines_with_coord(self, checker: Checker, coord: Coord) -> list[Line]:
        lines = []
        # up, up right, right, down right
        directions = [(0, 1), (1, 1), (1, 0), (1, -1)]
        for direction in directions:
            line = [coord]

            # Go "left"
            offset = coord
            offset = (offset[0] - direction[0], offset[1] - direction[1])
            while (0 <= offset[0] < self.width() and 0 <= offset[1] < self.height()):
                if self.__cells[offset[1]][offset[0]] != checker.value:
                    break
                line.insert(0, offset)
                offset = (offset[0] - direction[0], offset[1] - direction[1])

            # Go "right"
            offset = coord
            offset = (offset[0] + direction[0], offset[1] + direction[1])
            while (0 <= offset[0] < self.width() and 0 <= offset[1] < self.height()):
                if self.__cells[offset[1]][offset[0]] != checker.value:
                    break
                line.append(offset)
                offset = (offset[0] + direction[0], offset[1] + direction[1])

            if (len(line) > 1):
                lines.append(line)
        return lines

    def find_line_making_moves(self, checker: Checker) -> Moves:
        available_coords =  self.available_coords()
        moves = {}
        for coord in available_coords:
            lines_with_coord = self.find_lines_with_coord(checker, coord)
            if (len(lines_with_coord) > 0):
                moves[coord] = lines_with_coord
        return moves

    def available_coords(self) -> Line:
        available = []
        for x in range(0, self.width()):
            coord = self.find_free_coord(x)
            if (coord is not None):
                available.append(coord)
        return available

    def __filter_winning_lines(self, checker: Checker, lines: list[Line]) -> list[Line]:
        return list(filter(lambda line: len(line) >= self.WIN_LENGTH , lines))
    