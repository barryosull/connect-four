
from abc import ABC, abstractmethod
from domain.board import Board
from domain.checker import Checker
from domain.actions import Action


class PlayerInterface(ABC):

    checker = '-'

    @abstractmethod
    def select_action(self, board: Board) -> Action:
        print("Abstract method, please implement")
        return Option.QUIT
