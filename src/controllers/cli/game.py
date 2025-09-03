from domain.board import Board
from domain.actions import Action, Option
from controllers.cli.player_factory import PlayerFactory
from controllers.cli.renderer import Renderer
from domain.board_dtos import Coord
from domain.checker import Checker
from domain.game import Game


class CLIGame:

    __last_drop: tuple[Checker, Coord] | None

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

        players = self.__player_factory.make_players()
        board = Board()
        game = Game(board, list(players.keys()))
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

