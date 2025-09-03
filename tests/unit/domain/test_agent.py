from unittest.mock import Mock
import random
from domain.agent import Agent
from domain.board import Board
from domain.board_dtos import BoardCells
from domain.checker import Checker
from domain.game import Game
from domain.state import State


class TestAgent:
    def test_select_next_slot_winning_move(self):
        game_state = self.make_game_state_for_board(
            [
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "y", "r", "-", "-", "-", "-"],
                ["y", "r", "y", "r", "y", "r", "y"],
                ["r", "y", "r", "y", "r", "y", "r"],
            ]
        )
        agent = Agent()

        actual = agent.select_next_slot(Checker.RED, game_state)

        expected = 1
        assert actual == expected

    def select_next_slot_stop_other_player_from_winning(self):
        game_state = self.make_game_state_for_board(
            [
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "y", "r", "-", "-", "-", "-"],
                ["y", "r", "y", "r", "y", "r", "y"],
                ["r", "y", "r", "y", "r", "y", "r"],
            ]
        )
        agent = Agent()

        actual = agent.select_next_slot(Checker.YELLOW, game_state)

        expected = 1
        assert actual == expected

    def test_select_next_slot_expands_existing_lines(self):
        game_state = self.make_game_state_for_board(
            [
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "r", "y", "-", "-", "-", "-"],
                ["r", "y", "y", "y", "r", "y", "r"],
            ]
        )
        agent = Agent()

        actual = agent.select_next_slot(Checker.RED, game_state)

        expected = 2
        assert actual == expected

    def test_select_next_slot_only_expands_existing_lines_when_not_a_win_for_other_player(
        self,
    ):
        # If 'y' selects slot 2 (gets two rows of three) then 'r' wins on the next turn, slot 1 is a better choice
        game_state = self.make_game_state_for_board(
            [
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "r", "y", "-", "-"],
                ["-", "-", "y", "y", "r", "-", "-"],
                ["r", "r", "y", "r", "y", "r", "-"],
            ]
        )
        agent = Agent()

        actual = agent.select_next_slot(Checker.YELLOW, game_state)

        expected = 1
        assert actual == expected

    def test_select_next_slot_expands_multiple_existing_lines_if_possible(self):
        game_state = self.make_game_state_for_board(
            [
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["r", "-", "-", "r", "y", "r", "-"],
                ["r", "y", "r", "y", "r", "y", "r"],
            ]
        )
        agent = Agent()

        actual = agent.select_next_slot(Checker.RED, game_state)

        expected = 4
        assert actual == expected

    def test_select_next_slot_blocks_other_player_across_multiple_existing_lines_if_possible(
        self,
    ):
        game_state = self.make_game_state_for_board(
            [
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["r", "-", "-", "r", "r", "-", "-"],
                ["r", "y", "r", "y", "r", "y", "r"],
            ]
        )
        agent = Agent()

        actual = agent.select_next_slot(Checker.YELLOW, game_state)

        expected = 4
        assert actual == expected

    def test_select_next_slot_chooses_middle_as_opening_move(self):
        game_state = self.make_game_state_for_board(
            [
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
            ]
        )
        agent = Agent()

        actual = agent.select_next_slot(Checker.RED, game_state)

        expected = 3
        assert actual == expected

    def test_select_next_slot_chooses_random_if_middle_is_taken(self):
        game_state = self.make_game_state_for_board(
            [
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "-", "-", "-", "-"],
                ["-", "-", "-", "y", "-", "-", "-"],
            ]
        )
        coord = (2, 5)
        random.choice = Mock(return_value = coord)

        agent = Agent()

        actual = agent.select_next_slot(Checker.RED, game_state)
        
        expected = 2
        assert actual == expected

    def make_game_state_for_board(self, cells: BoardCells) -> State:
        return Game(Board(cells)).state()
