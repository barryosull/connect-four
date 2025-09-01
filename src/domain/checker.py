
from enum import Enum
from typing import Self


class Checker(Enum):
    RED = 'r'
    YELLOW = 'y'

    def __str__(self):
        return self.value

    def opponent(self) -> Self:
        if (self == Checker.RED):
            return Checker.YELLOW
        return Checker.RED
