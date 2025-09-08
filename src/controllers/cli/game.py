import domain.board as board
from domain.actions import Action, Option
from controllers.cli.player_factory import PlayerFactory
from controllers.cli.renderer import Renderer
from domain.game import Game
import argparse

from domain.line_finder import DefaultLineFinder, LineFinder, TorusLineFinder


class CLIGame:

    def __init__(
        self,
        renderer: Renderer = Renderer(),
        player_factory: PlayerFactory | None = None
    ):
        self.__renderer = renderer if (renderer is not None) else Renderer()
        self.__player_factory = (
            player_factory
            if (player_factory is not None)
            else PlayerFactory(self.__renderer)
        )

    def play(self) -> Option:
        args = self.__parse_args()

        line_finder_strategy = self.__make_line_finder_strategy(args)

        players = self.__player_factory.make_players(args, line_finder_strategy)

        fresh_board = board.make_empty_board(args.width, args.height)
        
        game = Game(fresh_board, list(players.keys()), line_finder_strategy)
        state = game.state()

        choice: Action

        while state.winner is None and not state.board.is_full():
            self.__renderer.print_board(state)

            choice = players[state.current_player].select_action(state)

            if choice == Option.QUIT:
                break

            slot = int(choice)

            game.drop_checker(slot)
            
            state = game.state()            
            

        self.__renderer.print_board(state)
        self.__renderer.print_goodbye()
        return Option.QUIT
    
    def __parse_args(self): 
        parser = argparse.ArgumentParser(
            prog="Connect Four", description="Play a game of connect four"
        )

        parser.add_argument("-m", "--mode", type=str, default="default")
        parser.add_argument("-p1", "--player1Actions", nargs="*", type=str)
        parser.add_argument("-p2", "--player2Actions", nargs="*", type=str)
        parser.add_argument("-w", "--width", type=int, default=7)
        parser.add_argument("-he", "--height", type=int, default=6)
        return parser.parse_args()

    def __make_line_finder_strategy(self, args) -> LineFinder:
        match (args.mode):
            case "torus":
                return TorusLineFinder()
            case default:
                return DefaultLineFinder()