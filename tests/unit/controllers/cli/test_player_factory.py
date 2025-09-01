from controllers.cli.player_factory import PlayerFactory
from controllers.cli.player_input import PlayerInput
from controllers.cli.player_set_input import PlayerSetInput
from controllers.cli.player_agent import PlayerAgent


class TestPlayerFactory:
    def test_make_input_and_agent_by_default(self, mocker):
        renderer = mocker.Mock()
        factory = PlayerFactory(renderer)
        no_cli_args = []

        players = factory.make_players(no_cli_args)

        assert len(players) == 2
        assert isinstance(players[0], PlayerInput)
        assert isinstance(players[1], PlayerAgent)

    def test_make_set_actions_from_cli_args(self, mocker):
        renderer = mocker.Mock()
        factory = PlayerFactory(renderer)
        cli_args = [
            "--player1Actions",
            "1",
            "1",
            "1",
            "1",
            "--player2Actions",
            "2",
            "2",
            "2",
            "2",
        ]

        players = factory.make_players(cli_args)

        set_action_players = list(
            filter(lambda player: isinstance(player, PlayerSetInput), players)
        )
        assert len(set_action_players) == 2
