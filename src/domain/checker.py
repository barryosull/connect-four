from enum import Enum


class Checker(Enum):
    RED = "r"
    YELLOW = "y"

    def __str__(self):
        return self.value

    def opponent(self) -> "Checker":
        if self == Checker.RED:
            return Checker.YELLOW
        return Checker.RED
