
type BoardCells = list[list[str]]
type Coord = tuple[int, int]
type Line = list[Coord]

# Todo Move to its own file
class Winner:

    def __init__(self, checker: str, lines: list[list[Coord]]):
        self.checker = checker
        self.lines = lines

    def __eq__(self, other):
        return self.checker == other.checker and self.lines == other.lines

    def is_in_list(self, coord: Coord) -> bool:
        for line in self.lines:
            if coord in line:  
                return True
        return False

class Board:

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
    
    def drop_checker(self, checker: str, slot: int) -> Coord|None:
        coord = self.__find_free_coord(slot)
        if (coord is None):
            return None
        self.__cells[coord[1]][coord[0]] = checker.value
        return coord
    
    def __find_free_coord(self, slot: int) -> Coord|None:
        x = slot        
        for i in range (0, self.height()): 
            y = self.height() - 1 - i
            if self.__cells[y][x] == '-':
                return [x, y]
        return None

    
    #############
    # Queries 
    #############

    def width(self) -> int:
        return len(self.__cells[0])

    def height(self) -> int:
        return len(self.__cells)

    def is_valid_drop(self, slot: int) -> bool: 
        return self.__find_free_coord(slot) is not None

    def game_can_continue(self) -> bool:
        return self.winner() is None and self.is_full == False

    def is_full(self) -> bool:
        return '-' not in self.__cells[0]

    def export_cells(self) -> BoardCells:
        return self.__cells

    def find_winner(self, last_move: Coord) -> Winner|None:

        [x, y] = last_move
        checker = self.__cells[y][x]

        horizontal_line = [[x, y]]
        vertical_line = [[x, y]]
        down_right_line = [[x, y]]
        up_right_line = [[x, y]]

        for offset in range(1, max(self.height(), self.width())):
            left_x = x - offset
            right_x = x + offset
            up_y = y - offset
            down_y = y + offset

            # Horizontal
            if (left_x >= 0):
                horizontal_line.insert(0, [left_x, y])
            if (right_x < self.width()):
                horizontal_line.append([right_x, y])

            # Vertical
            if (up_y >= 0):
                vertical_line.insert(0, [x, up_y])
            if (down_y < self.height()):
                vertical_line.append([x, down_y])

            # Diagonal down right
            if left_x >= 0 and up_y >= 0:
                down_right_line.insert(0, [left_x, up_y])
            if right_x < self.width() and down_y < self.height():
                down_right_line.append([right_x, down_y])

            # Diagonal up right
            if left_x >= 0 and down_y < self.height():
                up_right_line.insert(0, [left_x, down_y])
            if right_x < self.width() and up_y >= 0:
                up_right_line.append([right_x, up_y])

        winning_lines = self.__filter_winning_lines(checker, [horizontal_line, vertical_line, down_right_line, up_right_line])
        
        # Check for winners
        if len(winning_lines) == 0:
            return None

        return Winner(checker, winning_lines)

    def __filter_winning_lines(self, checker: str, lines: list[Line]) -> list[Line]:
        winning_lines = []
        for line in lines:
            winning_line = []
            for pos in line:
                if self.__cells[pos[1]][pos[0]] == checker:
                    winning_line.append(pos)
                else:
                    winning_line = []
                if len(winning_line) == 4:
                    winning_lines.append(winning_line)
                    break
        return winning_lines
