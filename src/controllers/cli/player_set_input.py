from domain.actions import Action, Option
from domain.checker import Checker
from domain.board import Board
from controllers.cli.player_interface import PlayerInterface
from controllers.cli.player_input import PlayerInput

type Actions = list[Action]

# Player with hard coded inputs, as if they entered them via the cli
# Used in testing


class PlayerSetInput(PlayerInterface):
    def __init__(self, checker: Checker, input: list[str]):
        self.__input = input.copy()
        self.checker = checker

    def select_action(self, board: Board) -> Action:
        if len(self.__input) == 0:
            return Option.QUIT
        action = self.__input.pop(0)
        if action == PlayerInput.QUIT_CHAR:
            return Option.QUIT
        if action.isdigit():
            return int(action) - 1
        return Option.QUIT


