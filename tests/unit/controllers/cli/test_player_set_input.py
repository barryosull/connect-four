from domain.actions import Option
from domain.checker import Checker
from controllers.cli.player_set_input import PlayerSetInput


class TestPlayerSetInput:
    def test_configure_action_input(self, mocker):
        board = mocker.Mock()
        inputs = ["1", "2", "3", "q"]
        player = PlayerSetInput(Checker.RED, inputs)
        expected = [0, 1, 2, Option.QUIT]

        for expected_action in expected:
            assert expected_action == player.select_action(board)

    def test_last_action_quit(self, mocker):
        board = mocker.Mock()
        inputs = ["1", "2", "3"]
        player = PlayerSetInput(Checker.RED, inputs)

        for input_str in inputs:
            player.select_action(board)

        action = player.select_action(board)
        assert action == Option.QUIT
