
from domain.board import Board
from domain.actions import Action, Option
from controllers.cli.player_factory import PlayerFactory
from controllers.cli.renderer import Renderer


class Game:
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
        board = Board()
        state = board.state()

        players = self.__player_factory.make_players()
        player = players[0]

        choice: Action

        while state.winner is None and not state.is_full:
            self.__renderer.print_board(state)

            choice = player.select_action(board)

            if choice == Option.QUIT:
                break

            slot = int(choice)

            board.drop_checker(player.checker, slot)
            
            state = board.state()

            # Next player
            player = players[0] if player == players[1] else players[1]
            

        self.__renderer.print_board(state)
        self.__renderer.print_goodbye()
        return Option.QUIT

