
from agent import Agent
from board import Board
from checker import Checker

class TestAgent:

    def test_select_winning_move(self):
        board = Board([
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', 'y', 'r', '-', '-', '-', '-'],
            ['y', 'r', 'y', 'r', 'y', 'r', 'y'],
            ['r', 'y', 'r', 'y', 'r', 'y', 'r']
        ])
        agent = Agent()

        slot = agent.select_next_slot(Checker.RED, board)

        expected = 1
        assert(slot == expected)

    # def select_other_player_win_blocking_slot()


    ### Helper tests for iteration ###
