
from domain.actions import Option
from domain.checker import Checker
from domain.board import Board
from controllers.cli.player_input import PlayerInput

class TestPlayerInput:

    def setup(self, mocker):
        self.renderer = mocker.Mock()
        self.board = Board()

        self.player = PlayerInput(Checker.RED, self.renderer)
        
    def test_select_action_slot_is_parsed_and_converted(self, mocker, monkeypatch):
        self.setup(mocker)
        choose_slot = '3'
        converted_slot = 2 # Player input starts at one, domain slots start at 0
        self.override_inputs(monkeypatch, [choose_slot])

        actual = self.player.select_action(self.board)

        assert(actual == converted_slot)

    def test_select_action_quit(self, mocker, monkeypatch): 
        self.setup(mocker)
        input_char = PlayerInput.QUIT_CHAR
        self.override_inputs(monkeypatch, [input_char])

        actual = self.player.select_action(self.board)

        assert(actual == Option.QUIT)

    def test_select_action_asks_again_if_input_is_invalid(self, mocker, monkeypatch):
        self.setup(mocker)
        invalid_chars = ['a', 'dsfsdf', '341234', '[', '-']
        valid_char = PlayerInput.QUIT_CHAR
        self.override_inputs(monkeypatch, invalid_chars + [valid_char])

        actual = self.player.select_action(self.board)

        assert(actual == Option.QUIT)

    def select_actions_asks_again_if_slot_is_full(self, mocker, monkeypatch):
        self.setup(mocker)
        full_slot = 2
        full_slot_input = '3'
        empty_slot = 0;
        empty_slot_input = '1'
        board = self.make_board_with_full_slot(full_slot)

        inputs = [full_input_slot, empty_slot_input]
        self.override_inputs(monkeypatch, invalid_chars + [valid_char])

        actual = self.player.select_action(board)

        assert(actual == empty_slot)

    def override_inputs(self, monkeypatch, inputs: list[str]):
        inputs = iter(inputs)
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    def make_board_with_full_slot(self, slot: int) -> Board:
        board = Board()
        for i in range(0, board.height()):
            board.drop_checker(checker.RED, slot)
        return board
