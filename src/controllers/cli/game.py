
import sys
import os
import argparse

from pathlib import Path
from domain.board import Board
from domain.checker import Checker
from domain.actions import Option
from controllers.cli.player_factory import PlayerFactory
from controllers.cli.player_input import PlayerInput
from controllers.cli.renderer import Renderer


class Game:

    def __init__(
        self,
        renderer: Renderer = None,
        player_factory: PlayerFactory = None
    ):
        self.__renderer = render if (renderer is not None) else Renderer()
        self.__player_factory = player_factory if (
            player_factory is not None) else PlayerFactory(self.__renderer)

    def play(self) -> Option:

        board = Board()

        players = self.__player_factory.make_players()
        player = players[0]

        choice = ""
        winner = None

        while winner is None and not board.is_full():
            self.__renderer.print_board(board)

            choice = player.select_action(board)

            if choice == Option.QUIT:
                break

            slot = int(choice)

            coord = board.drop_checker(player.checker, slot)
            winner = board.find_winner(player.checker, coord)

            # Next player
            player = players[0] if player == players[1] else players[1]

        self.__renderer.print_board(board, winner)
        self.__renderer.print_goodbye()
        return Option.QUIT
