from abc import ABC, abstractmethod
from domain.board import Board
from domain.checker import Checker
from domain.actions import Action, Option


class PlayerInterface(ABC):

    checker: Checker

    @abstractmethod
    def select_action(self, board: Board) -> Action:
        print("Abstract method, please implement")
        return Option.QUIT
