from controllers.cli.player_factory import PlayerFactory
from controllers.cli.player_input import PlayerInput
from controllers.cli.player_set_input import PlayerSetInput
from controllers.cli.player_agent import PlayerAgent
from domain.checker import Checker
from unittest.mock import Mock

class TestPlayerFactory:
    
    def test_make_input_and_agent_by_default(self, mocker):
        renderer = mocker.Mock()
        factory = PlayerFactory(renderer)
        args = Mock()
        args.player1Actions = None
        args.player2Actions = None

        players = factory.make_players(args)

        assert len(list(players.keys())) == 2
        assert isinstance(players[Checker.RED], PlayerInput)
        assert isinstance(players[Checker.YELLOW], PlayerAgent)

    def test_make_set_actions_from_cli_args(self, mocker):
        renderer = mocker.Mock()
        factory = PlayerFactory(renderer)

        args = Mock()
        args.player1Actions = [ "1", "1", "1", "1"]
        args.player2Actions = [ "2", "2", "2", "2"]
       
        players = factory.make_players(args)

        set_action_players = list(
            filter(lambda player: isinstance(player, PlayerSetInput), list(players.values()))
        )
        assert len(set_action_players) == 2
