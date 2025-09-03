from abc import ABC, abstractmethod
from domain.board import Board
from domain.checker import Checker
from domain.actions import Action, Option
from domain.state import State


class PlayerInterface(ABC):

    checker: Checker

    @abstractmethod
    def select_action(self, state: State) -> Action:
        print("Abstract method, please implement")
        return Option.QUIT
