import sys
import argparse
from domain.checker import Checker
from domain.agent import Agent
from controllers.cli.player_interface import PlayerInterface
from controllers.cli.player_input import PlayerInput
from controllers.cli.player_agent import PlayerAgent
from controllers.cli.player_set_input import PlayerSetInput
from controllers.cli.renderer import Renderer


class PlayerFactory:
    def __init__(self, renderer: Renderer):
        self.__renderer = renderer

    def make_players(self, parsed_args) -> dict[Checker, PlayerInterface]:
        return {
            Checker.RED: self.make_player(Checker.RED, parsed_args.player1Actions),
            Checker.YELLOW: self.make_player(Checker.YELLOW, parsed_args.player2Actions) 
        }

    def make_player(self, checker: Checker, player_actions: list[str] | None):
        if player_actions is not None:
            return PlayerSetInput(checker, player_actions)
        if checker == Checker.YELLOW:
            return PlayerAgent(checker, Agent(), self.__renderer)

        return PlayerInput(checker, self.__renderer)
