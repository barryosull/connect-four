
import sys
import os
import argparse

from pathlib import Path
from board import Board
from checker import Checker
from actions import Option

from controllers.cli.player_factory import PlayerFactory
from controllers.cli.player_input import PlayerInput
from controllers.cli.player_set_actions import PlayerSetActions, Actions
from controllers.cli.renderer import Renderer

class CLIGame:

    def __init__(self, renderer: Renderer = None, player_factory: PlayerFactory = None):
        self.__renderer = render if (renderer is not None) else Renderer()
        self.__player_factory = player_factory if (player_factory is not None) else PlayerFactory(self.__renderer)

    def play(self):

        option = Option.PLAY
        while (option in [Option.PLAY, Option.RESTART]):
            option = self.__play_game()

    def __play_game(self) -> Option: 

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
            if choice == Option.RESTART:
                return choice

            slot = int(choice)
            
            coord = board.drop_checker(player.checker, slot)
            winner = board.find_winner(coord)

            # Next player
            player = players[0] if player == players[1] else players[1]
            
        self.__renderer.print_board(board, winner)

        if (winner is not None):
            # Todo: Enable and get under test
            '''
            play_again_choice = input("Want to play again (y/n)?")
            if (play_again_choice == "y"):
                return Option.PLAY
            '''

        self.__renderer.print_goodbye()
        return Option.QUIT
