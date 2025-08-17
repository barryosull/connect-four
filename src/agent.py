
from board import Board, Coord, Line
from checker import Checker
import random

type AvailableLines = dict(Coord, list[Line])

class Agent:

    def select_next_slot(self, checker: Checker, board: Board) -> int:
        
        moves = board.find_line_making_moves(checker.value)
        other_player_moves = board.find_line_making_moves(checker.opponent().value)

        # Find winning moves
        for coord, lines in moves.items():
            winning_lines = list(filter(lambda line: len(line) >= 4, lines))
            if len(winning_lines) > 0:
                return coord[0]

        # Block other players winning moves
        for coord, lines in other_player_moves.items():
            winning_lines = list(filter(lambda line: len(line) >= 4, lines))
            if len(winning_lines) > 0:
                return coord[0]

        # Extend 3 lines, extend many if possible
        lines_found = 0
        best_slot = None
        for coord, lines in moves.items():
            expanded_lines = list(filter(lambda line: len(line) == 3, lines))
            if len(expanded_lines) > lines_found:
                lines_found = len(expanded_lines) 
                best_slot = coord[0]
        if best_slot is not None:
            return best_slot

        # Block other players line extensions
        lines_found = 0
        best_slot = None
        for coord, lines in other_player_moves.items():
            expanded_lines = list(filter(lambda line: len(line) == 3, lines))
            if len(expanded_lines) > lines_found:
                lines_found = len(expanded_lines) 
                best_slot = coord[0]
        if best_slot is not None:
            return best_slot

        # Extend 2 lines, extend many if possible
        lines_found = 0
        best_slot = None
        for coord, lines in moves.items():
            expanded_lines = list(filter(lambda line: len(line) == 2, lines))
            if len(expanded_lines) > lines_found:
                lines_found = len(expanded_lines) 
                best_slot = coord[0]
        if best_slot is not None:
            return best_slot

        # Block other players line extensions
        lines_found = 0
        best_slot = None
        for coord, lines in other_player_moves.items():
            expanded_lines = list(filter(lambda line: len(line) == 2, lines))
            if len(expanded_lines) > lines_found:
                lines_found = len(expanded_lines) 
                best_slot = coord[0]
        if best_slot is not None:
            return best_slot

        # Select middle if available
        available = board.available_coords()
        middle = (board.width() // 2, board.height() - 1)
        if middle in available:
            return middle[0]

        # Select random by default
        return random.choice(available.keys)[0]



