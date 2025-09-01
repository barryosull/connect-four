from domain.board import Board, Moves, Coord
from domain.checker import Checker
import random


# Simple heuristic based agent that triesd to choose the best move
class Agent:
    def select_next_slot(self, checker: Checker, board: Board) -> int:
        moves = board.find_line_making_moves(checker)
        other_player_moves = board.find_line_making_moves(checker.opponent())

        for offset in range(0, 3):
            length = Board.WIN_LENGTH - offset

            # Best move for player
            best_move = self.__find_best_move_of_length(moves, board, length, checker)
            if best_move is not None:
                return best_move[0]

            # Block other players moves, but only potential rows of 3 or above
            best_move = None
            if length != 2:
                best_move = self.__find_best_move_of_length(
                    other_player_moves, board, length, checker.opponent()
                )
            if best_move is not None:
                return best_move[0]

        # Select middle if available, as it's the best position if
        # there are no others
        available = board.available_coords()
        middle = (board.width() // 2, board.height() - 1)
        if middle in available:
            return middle[0]

        # Select random by default, not optimal, but it makes the game
        # more interesting
        return random.choice(available)[0]

    def __find_best_move_of_length(
        self, moves: Moves, board: Board, length: int, checker: Checker
    ) -> Coord | None:
        lines_found = 0
        best_move = None
        for move, lines in moves.items():
            expanded_lines = list(filter(lambda line: len(line) == length, lines))
            # Find best move, but make sure it doesnt let the other player
            # win immedaitely afterwards (skip for winning move)
            if len(expanded_lines) > lines_found and (
                length == Board.WIN_LENGTH
                or not self.__would_move_let_opponent_win(
                    move, board, checker.opponent()
                )
            ):
                lines_found = len(expanded_lines)
                best_move = move
        return best_move

    def __would_move_let_opponent_win(
        self, move: Coord, board: Board, checker: Checker
    ) -> bool:
        if move[1] == 0:
            return False
        move_above = (move[0], move[1] - 1)
        return board.find_winner(checker, move_above) is not None
