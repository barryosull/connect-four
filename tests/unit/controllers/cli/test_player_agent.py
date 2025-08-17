
from domain.checker import Checker
from controllers.cli.player_agent import PlayerAgent

class TestPlayerAgent:
    
    def test_select_action(self, mocker):
        agent = mocker.Mock()
        renderer = mocker.Mock()
        board = mocker.Mock()
        player_agent = PlayerAgent(Checker.RED, agent, renderer, sleep_time = 0)

        choice = 1
        agent.select_next_slot.return_value = choice

        actual = player_agent.select_action(board)

        assert(actual == choice)