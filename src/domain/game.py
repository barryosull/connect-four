from domain.board import Board
from domain.state import State
from domain.board_dtos import Coord
from domain.checker import Checker
from domain.winner import Winner
from domain.finders import Finders


class Game:

    __last_drop: tuple[Checker, Coord] | None

    def __init__(self, board: Board, players: list[Checker] = [Checker.RED, Checker.YELLOW]):
        self.__board = board
        self.__players = players
        self.__current_player_index = 0
        self.__last_drop = None

    def drop_checker(self, slot: int):
        if (self.winner() is not None):
            return
        
        checker = self.__players[self.__current_player_index]
        drop_coord = self.__board.drop_checker(self.__players[self.__current_player_index], slot)
        if (drop_coord is None):
            return

        self.__last_drop = (checker, drop_coord)
        self.__current_player_index = (self.__current_player_index + 1) % len(self.__players)

    def winner(self) -> Winner| None:
        return (
            Finders().winning_move(self.__board, self.__last_drop[0], self.__last_drop[1]) 
            if self.__last_drop is not None
            else None
        )

    def state(self) -> State: 
        return State(
            self.__board, 
            self.__players,
            self.__players[self.__current_player_index],
            self.winner()
        )
