
from actions import Option
from checker import Checker
from board import Board
from controllers.cli.player_set_actions import PlayerSetActions

class TestPlayerSetActions:

    def test_configure_action_input(self, mocker):
        board = mocker.Mock()
        actions = [0, 1, 2, Option.QUIT]
        player = PlayerSetActions(Checker.RED, actions)

        for action in actions:
            assert(action == player.select_action(board))

    def test_last_action_quit(self, mocker):
        board = mocker.Mock()
        actions = [0, 1, 2]
        player = PlayerSetActions(Checker.RED, actions)

        for action in actions:
            player.select_action(board)

        action = player.select_action(board)
        assert(action == Option.QUIT)
