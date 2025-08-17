
import sys
import argparse
from checker import Checker
from controllers.cli.player_input import PlayerInput
from controllers.cli.player_set_actions import PlayerSetActions, Actions
from controllers.cli.renderer import Renderer

class PlayerFactory:

    def __init__(self, renderer: Renderer):
        self.__renderer = renderer

    def make_players(self, cli_args: list[str] = sys.argv[1:]): 
        parser = argparse.ArgumentParser(
            prog='Connect Four',
            description='Play a game of connect four'
        )

        parser.add_argument(
            '-p1', 
            '--player1Actions',
            nargs="*",
            type=str
        )
        parser.add_argument(
            '-p2', 
            '--player2Actions',
            nargs="*",
            type=str
        )

        parsed_args = parser.parse_args(cli_args)

        player1 = self.make_player(Checker.RED, parsed_args.player1Actions)
        player2 = self.make_player(Checker.YELLOW, parsed_args.player2Actions)

        return [player1, player2]

    def make_player(self, checker: str, player_actions: Actions):
        if (player_actions is None):
            return PlayerInput(checker, self.__renderer)
        return PlayerSetActions(checker, player_actions)
