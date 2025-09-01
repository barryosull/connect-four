import sys
import argparse
from domain.checker import Checker
from domain.agent import Agent
from controllers.cli.player_interface import PlayerInterface
from controllers.cli.player_input import PlayerInput
from controllers.cli.player_agent import PlayerAgent
from controllers.cli.player_set_input import PlayerSetInput, Actions
from controllers.cli.renderer import Renderer


class PlayerFactory:
    def __init__(self, renderer: Renderer):
        self.__renderer = renderer

    def make_players(self, cli_args: list[str] = sys.argv[1:]) -> list[PlayerInterface]:
        parser = argparse.ArgumentParser(
            prog="Connect Four", description="Play a game of connect four"
        )

        parser.add_argument("-p1", "--player1Actions", nargs="*", type=str)
        parser.add_argument("-p2", "--player2Actions", nargs="*", type=str)

        parsed_args = parser.parse_args(cli_args)

        player1 = self.make_player(Checker.RED, parsed_args.player1Actions)
        player2 = self.make_player(Checker.YELLOW, parsed_args.player2Actions)

        return [player1, player2]

    def make_player(self, checker: Checker, player_actions: Actions):
        if player_actions is not None:
            return PlayerSetInput(checker, player_actions)
        if checker == Checker.YELLOW:
            return PlayerAgent(checker, Agent(), self.__renderer)

        return PlayerInput(checker, self.__renderer)
