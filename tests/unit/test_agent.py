
from agent import Agent
from board import Board
from checker import Checker

class TestAgent:

    def test_select_next_slot_winning_move(self):
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

    def select_next_slot_stop_other_player_from_winning(self):
        board = Board([
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', 'y', 'r', '-', '-', '-', '-'],
            ['y', 'r', 'y', 'r', 'y', 'r', 'y'],
            ['r', 'y', 'r', 'y', 'r', 'y', 'r']
        ])
        agent = Agent()

        slot = agent.select_next_slot(Checker.YELLOW, board)

        expected = 1
        assert(slot == expected)


    def test_select_next_slot_expands_existing_lines(self):
        board = Board([
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', 'r', 'y', '-', '-', '-', '-'],
            ['r', 'y', 'y', 'y', 'r', 'y', 'r']
        ])
        agent = Agent()

        slot = agent.select_next_slot(Checker.RED, board)

        expected = 2
        assert(slot == expected)

    def test_select_next_slot_expands_multiple_existing_lines_if_possible(self):
        board = Board([
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['r', '-', '-', 'r', 'y', 'r', '-'],
            ['r', 'y', 'r', 'y', 'r', 'y', 'r']
        ])
        agent = Agent()

        slot = agent.select_next_slot(Checker.RED, board)

        expected = 4
        assert(slot == expected)

    def test_select_next_slot_blocks_other_player_across_multiple_existing_lines_if_possible(self):
        board = Board([
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['r', '-', '-', 'r', 'r', '-', '-'],
            ['r', 'y', 'r', 'y', 'r', 'y', 'r']
        ])
        agent = Agent()

        slot = agent.select_next_slot(Checker.YELLOW, board)

        expected = 4
        assert(slot == expected)

    def test_select_next_slot_chooses_middle_as_opening_move(self):
        board = Board([
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
        ])
        agent = Agent()

        slot = agent.select_next_slot(Checker.RED, board)

        expected = 3
        assert(slot == expected)


