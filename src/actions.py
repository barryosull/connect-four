
from enum import Enum
from board import Board

type Slot = int

class Option(Enum):
    PLAY    = 'play'
    QUIT    = 'quit'

type Action = Slot|Option

