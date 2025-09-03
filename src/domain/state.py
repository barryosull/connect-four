from dataclasses import dataclass
from domain.board import Board
from domain.checker import Checker
from domain.winner import Winner


@dataclass
class State:
    board: Board
    players: list[Checker]
    current_player: Checker
    winner: Winner | None