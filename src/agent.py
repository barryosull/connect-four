
from board import Board, Move, Line, Coord
from checker import Checker
import random

type AvailableLines = dict(Coord, list[Line])

class Agent:

    def select_next_slot(self, checker: Checker, board: Board) -> int:
        
        moves = board.find_line_making_moves(checker.value)
        other_player_moves = board.find_line_making_moves(checker.opponent().value)

        for length in range (0, 3):
            # Best move for player
            best_move = self.__find_best_move_of_length(moves, board, 4 - length, checker)
            if (best_move is not None):
                return best_move[0]

            # Block other players winning moves
            best_move = self.__find_best_move_of_length(other_player_moves, board, 4 - length, checker.opponent())
            if (best_move is not None):
                return best_move[0]

        # Select middle if available
        available = board.available_coords()
        middle = (board.width() // 2, board.height() - 1)
        if middle in available:
            return middle[0]

        # Select random by default, not optimal, but it makes the game more interesting
        return random.choice(available.keys)[0]

    def __find_best_move_of_length(self, moves: list[Move], board: Board, length: int, checker: Checker) -> Coord|None:
        lines_found = 0
        best_move = None
        for move, lines in moves.items():
            expanded_lines = list(filter(lambda line: len(line) == length, lines))
            if len(expanded_lines) > lines_found and (length == 4 or not self.__would_move_let_opponent_win(move, board, checker.opponent())):
                lines_found = len(expanded_lines) 
                best_move = move
        return best_move

    def __would_move_let_opponent_win(self, move: Coord, board: Board, checker: Checker) -> bool:
        if move[1] == 0:
            return False
        move_above = (move[0], move[1] - 1)
        return board.find_winner(checker, move_above) is not None
