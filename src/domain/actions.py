
from enum import Enum
from domain.board import Board

type Slot = int


class Option(Enum):
    QUIT = 'quit'


type Action = Slot | Option
