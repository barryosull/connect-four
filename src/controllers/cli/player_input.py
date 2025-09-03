from domain.checker import Checker
from domain.actions import Action, Option
from controllers.cli.renderer import Renderer
from controllers.cli.player_interface import PlayerInterface
from domain.state import State


# Player that takes input from the CLI
class PlayerInput(PlayerInterface):
    
    QUIT_CHAR = "q"

    def __init__(self, checker: Checker, renderer: Renderer):
        self.checker = checker
        self.__renderer = renderer

    def select_action(self, state: State) -> Action:
        action = self.__ask_for_valid_input(state)

        if isinstance(action, Option):
            return action
        
        available_slots = map(
            lambda coord: coord[0], state.board.available_coords()
        )

        while action not in available_slots:
            action = self.__ask_for_valid_input(state, is_slot_full=True)
            self.__renderer.print_board(state)

            if isinstance(action, Option):
                return action

        return action

    def __ask_for_valid_input(self, state: State, is_slot_full: bool = False) -> Action:
        # valid chars
        slots_chars = [str(i) for i in range(1, state.board.width() + 1)]
        char_options = [self.QUIT_CHAR] + slots_chars

        choice = ""
        while choice not in char_options:
            if is_slot_full:
                self.__renderer.print_board(state)
                print("Slot is full, please select another slot")
                is_slot_full = False
            elif choice != "":
                self.__renderer.print_board(state)
                print("Please enter a valid character")

            choice = input(
                f"Player '{str(self.checker)}', "
                + f"select a slot (1 - {str(state.board.width())}), or 'q' to quit: "
            )

        if choice == self.QUIT_CHAR:
            return Option.QUIT

        return int(choice) - 1
