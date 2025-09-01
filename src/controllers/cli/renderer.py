import os
from pathlib import Path
from domain.board import Board, Winner
from domain.checker import Checker

# Renders to the console


class Renderer:
    def print_board(self, board: Board, winner: Winner | None = None):
        cells = board.export_cells()

        # Cell colours
        char_to_colour = {"r": 31, "y": 33}

        padding = "     "

        # Clear the termninal
        os.system("clear")

        self.__print_title()

        col_count = board.width()
        lines = padding + " "

        # Slot numbers
        for row_i in range(board.width()):
            lines += f" {str(row_i + 1)}"
        lines += "\n"

        # Slots with edges
        for y, row in enumerate(cells):
            line = f"{padding}|"
            for x, cell in enumerate(row):
                # Bold and color
                color = char_to_colour.get(cell, 38)
                bg_color = 47 if winner and winner.is_in_list((x, y)) else 40
                weight = 1 if cell != "-" else 0
                cell_char = cell if cell != "-" else "-"

                format = f"{weight};{color};{bg_color}"
                line += f" \033[{format}m{cell_char}\033[0m"
            line += " |"
            lines += f"{line}\n"

        # bottom
        lines += f"{padding}{('=' * ((col_count * 2) + 3))}\n"

        print(lines)

        if winner is not None:
            self.print_winner(winner.checker)
            return

        if board.is_full():
            self.print_board_is_full()

    def __print_title(self):
        # Todo: Fix relative path, not sure of the python way to do this yet
        file_path = Path("src/controllers/cli//title.txt")
        title = file_path.read_text()
        print(title)

    def print_agent_thinking(self, checker: Checker):
        print(f"Player '{checker}' is thinking . . .")

    def print_winner(self, checker: Checker):
        print(f"The winner is '{checker}'")

    def print_board_is_full(self):
        print("Board is full, no more moves left")

    def print_goodbye(self):
        print("Thanks for playing!")
        print()
