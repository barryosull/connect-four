from domain.board_dtos import BoardCells, Coord, Line
from domain.checker import Checker
from domain.winner import Winner


class Board:

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
        self.__last_drop = None


    #############
    # Comannds
    #############

    def drop_checker(self, checker: Checker, slot: int) -> Coord:
        coord = self.__find_free_coord(slot)
        if coord is None:
            return
        self.__cells[coord[1]][coord[0]] = checker.value
        return coord


    #############
    # Queries
    #############

    def width(self) -> int:
        return len(self.__cells[0])

    def height(self) -> int:
        return len(self.__cells)
    
    def coord_value(self, coord: Coord) -> str:
        [x, y] = coord
        return self.__cells[y][x]
    
    def winner(self) -> Winner| None:
        return (
            self.__searcher.find_winning_move(self.__last_drop[0], self.__last_drop[1]) 
            if self.__last_drop is not None
            else None
        )
        
    # TODO: Use free slots everywhere instead
    def available_coords(self) -> Line:
        available = []
        for x in range(0, self.width()):
            coord = self.__find_free_coord(x)
            if coord is not None:
                available.append(coord)
        return available

    def is_full(self) -> bool:
        return "-" not in self.__cells[0]
    
    def __find_free_coord(self, slot: int) -> Coord | None:
        x = slot
        for i in range(0, self.height()):
            y = self.height() - 1 - i
            if self.__cells[y][x] == "-":
                return (x, y)
        return None
