
from enum import Enum
from board import Board

type Slot = int

class Option(Enum):
    PLAY    = 'play'
    QUIT    = 'quit'
    RESTART = 'restart' 

type Action = Slot|Option

