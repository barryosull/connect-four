from enum import Enum

type Slot = int


class Option(Enum):
    QUIT = "quit"


type Action = Slot | Option
