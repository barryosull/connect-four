
from domain.agent import Agent
from domain.board import Board
from domain.checker import Checker

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

        actual = agent.select_next_slot(Checker.RED, board)

        expected = 1
        assert(actual == expected)

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

        actual = agent.select_next_slot(Checker.YELLOW, board)

        expected = 1
        assert(sactuallot == expected)

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

        actual = agent.select_next_slot(Checker.RED, board)

        expected = 2
        assert(actual == expected)

    def test_select_next_slot_only_expands_existing_lines_when_not_a_win_for_other_player(self):
        # If 'y' selects slot 2 (gets two rows of three) then 'r' wins on the next turn, slot 1 is a better choice
        board = Board([
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', 'r', 'y', '-', '-'],
            ['-', '-', 'y', 'y', 'r', '-', '-'],
            ['r', 'r', 'y', 'r', 'y', 'r', '-']
        ])
        agent = Agent()

        actual = agent.select_next_slot(Checker.YELLOW, board)

        expected = 1
        assert(actual == expected)

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

        actual = agent.select_next_slot(Checker.RED, board)

        expected = 4
        assert(actual == expected)

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

        actual = agent.select_next_slot(Checker.YELLOW, board)

        expected = 4
        assert(actual == expected)

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

        actual = agent.select_next_slot(Checker.RED, board)

        expected = 3
        assert(actual == expected)

    def test_select_next_slot_chooses_random_if_middle_is_taken(self):
        board = Board([
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', '-', '-', '-', '-'],
            ['-', '-', '-', 'y', '-', '-', '-'],
        ])
        agent = Agent()

        actual = agent.select_next_slot(Checker.RED, board)

        unexpected = 3
        assert(actual != unexpected)


