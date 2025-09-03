from domain.board import Board
from domain.board_dtos import Coord, Line, Moves
from domain.checker import Checker
from domain.winner import Winner


WIN_LENGTH = 4

def winning_move(board: Board, checker: Checker, coord: Coord) -> Winner | None:
    lines_with_coord = __lines_with_coord(board, checker, coord)

    winning_lines = list(
        filter(lambda line: len(line) >= WIN_LENGTH, lines_with_coord)
    )

    # Check for winners
    if len(winning_lines) == 0:
        return None

    return Winner(checker, winning_lines)

def line_making_moves(board: Board, checker: Checker) -> Moves:
    available_coords = board.available_coords()
    moves = {}
    for coord in available_coords:
        lines_with_coord = __lines_with_coord(board, checker, coord)

        if len(lines_with_coord) > 0:
            moves[coord] = lines_with_coord
    return moves


# Search all lines expanding outward from the coord
def __lines_with_coord(board: Board, checker: Checker, coord: Coord) -> list[Line]:
    lines = []
    # up, up right, right, down right
    directions = [(0, 1), (1, 1), (1, 0), (1, -1)]
    for direction in directions:
        line = [coord]

        # Go "left"
        offset = coord
        offset = (offset[0] - direction[0], offset[1] - direction[1])
        while (0 <= offset[0] < board.width() and 0 <= offset[1] < board.height()):
            if board.coord_value(offset) != checker.value:
                break
            line.insert(0, offset)
            offset = (offset[0] - direction[0], offset[1] - direction[1])

        # Go "right"
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
    