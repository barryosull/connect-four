
from actions import Action, Option
from checker import Checker
from board import Board
from player_interface import PlayerInterface

type Actions = list[Action]

class PlayerSetActions(PlayerInterface):

    def __init__(self, checker: Checker, actions: Actions):
        self.__actions = actions.copy()
        self.checker = checker 

    def select_action(self, board: Board) -> Action:
        if len(self.__actions) == 0:
            return Option.QUIT
        return self.__actions.pop(0)
