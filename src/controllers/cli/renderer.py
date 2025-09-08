import os
from pathlib import Path
from domain.state import State
from domain.checker import Checker


# Renders to the console
class Renderer:
    def print_board(self, state: State):

        # Cell colours
        char_to_colour = {"r": 31, "y": 33}

        padding = "     "

        # Clear the termninal
        os.system("clear")

        self.__print_title(state)

        col_count = state.board.width()
        lines = padding + " "

        # Slot numbers
        for row_i in range(col_count):
            lines += f" {str(row_i + 1)}"
        lines += "\n"

        # Slots with edges
        for y in range(0, state.board.height()):
            line = f"{padding}|"
            for x in range(0, state.board.width()):
                # Bold and color
                cell = state.board.coord_value((x, y))
                color = char_to_colour.get(cell, 38)
                bg_color = 47 if state.winner and state.winner.is_in_list((x, y)) else 40
                weight = 1 if cell != "-" else 0
                cell_char = cell if cell != "-" else "-"

                format = f"{weight};{color};{bg_color}"
                line += f" \033[{format}m{cell_char}\033[0m"
            line += " |"
            lines += f"{line}\n"

        # bottom
        lines += f"{padding}{('=' * ((col_count * 2) + 3))}\n"

        print(lines)

        if state.winner is not None:
            self.print_winner(state.winner.checker)
            return

        if state.board.is_full():
            self.print_board_is_full()

    def __print_title(self, state: State):
        # Todo: Fix relative path, not sure of the python way to do this yet
        file_path = Path("src/controllers/cli//title.txt")
        title = file_path.read_text()
        print(title)

        mode = f"Mode: {state.mode}"
        print(mode)
        print()

    def print_agent_thinking(self, checker: Checker):
        print(f"Player '{checker}' is thinking . . .")

    def print_winner(self, checker: Checker):
        print(f"The winner is '{checker}'")

    def print_board_is_full(self):
        print("Board is full, no more moves left")

    def print_goodbye(self):
        print("Thanks for playing!")
        print()
