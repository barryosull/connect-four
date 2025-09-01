from typing import Self
from domain.checker import Checker

type BoardCells = list[list[str]]
type Coord = tuple[int, int]
type Line = list[Coord]
type Move = dict[Coord, list[Line]]

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

    def __init__(self, cells: BoardCells | None = None):
        self.__cells = (
            [row[:] for row in cells]
            if cells is not None
            else [
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
            ]
        )

    #############
    # Comannds
    #############

    def drop_checker(self, checker: Checker, slot: int) -> Coord | None:
        coord = self.find_free_coord(slot)
        if coord is None:
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

    def find_free_coord(self, slot: int) -> Coord | None:
        x = slot
        for i in range(0, self.height()):
            y = self.height() - 1 - i
            if self.__cells[y][x] == "-":
                return (x, y)
        return None

    def is_valid_drop(self, slot: int) -> bool:
        return self.find_free_coord(slot) is not None

    def is_full(self) -> bool:
        return "-" not in self.__cells[0]

    def export_cells(self) -> BoardCells:
        return self.__cells

    def find_winner(self, checker: Checker, coord: Coord) -> Winner | None:
        [x, y] = coord

        directional_lines = self.directional_lines(coord)
        lines_with_coord = self.filter_lines_when_checker_is_at_coord(
            str(checker), coord, directional_lines
        )

        winning_lines = list(
            filter(lambda line: len(line) >= self.WIN_LENGTH, lines_with_coord)
        )
        print(checker, winning_lines)

        # Check for winners
        if len(winning_lines) == 0:
            return None

        return Winner(checker, winning_lines)

    # Bit brute force TBH, there are better algos, but it works
    # Easy room for improvement
    def directional_lines(self, coord: Coord) -> list[Line]:
        [x, y] = coord
        horizontal_coords = [(x, y)]
        vertical_coords = [(x, y)]
        down_right_coords = [(x, y)]
        up_right_coords = [(x, y)]

        for offset in range(1, max(self.height(), self.width())):
            left_x = x - offset
            right_x = x + offset
            up_y = y - offset
            down_y = y + offset

            # Horizontal
            if left_x >= 0:
                horizontal_coords.insert(0, (left_x, y))
            if right_x < self.width():
                horizontal_coords.append((right_x, y))

            # Vertical
            if up_y >= 0:
                vertical_coords.insert(0, (x, up_y))
            if down_y < self.height():
                vertical_coords.append((x, down_y))

            # Diagonal down right
            if left_x >= 0 and up_y >= 0:
                down_right_coords.insert(0, (left_x, up_y))
            if right_x < self.width() and down_y < self.height():
                down_right_coords.append((right_x, down_y))

            # Diagonal up right
            if left_x >= 0 and down_y < self.height():
                up_right_coords.insert(0, (left_x, down_y))
            if right_x < self.width() and up_y >= 0:
                up_right_coords.append((right_x, up_y))

        return [horizontal_coords, vertical_coords, down_right_coords, up_right_coords]

    def filter_lines_when_checker_is_at_coord(
        self, checker: Checker, desired_coord: Coord, directional_lines: list[Line]
    ) -> list[Line]:
        lines = []
        for directional_line in directional_lines:
            checker_line = []

            for coord in directional_line:
                if (
                    coord == desired_coord
                    or self.__cells[coord[1]][coord[0]] == checker
                ):
                    checker_line.append(coord)
                elif len(checker_line) > 1 and desired_coord in checker_line:
                    lines.append(checker_line)
                    checker_line = []
                else:
                    checker_line = []

            if len(checker_line) > 1 and desired_coord in checker_line:
                lines.append(checker_line)
                checker_line = []

        return lines

    def find_line_making_moves(self, checker: Checker) -> Move:
        available_coords = self.available_coords()
        moves = {}
        for coord in available_coords:
            directional_lines = self.directional_lines(coord)
            lines_with_coord = self.filter_lines_when_checker_is_at_coord(
                checker, coord, directional_lines
            )
            if len(lines_with_coord) > 0:
                moves[coord] = lines_with_coord
        return moves

    def available_coords(self) -> Line:
        available = []
        for x in range(0, self.width()):
            coord = self.find_free_coord(x)
            if coord is not None:
                available.append(coord)
        return available

    def __filter_winning_lines(self, checker: Checker, lines: list[Line]) -> list[Line]:
        return list(filter(lambda line: len(line) >= self.WIN_LENGTH, lines))
