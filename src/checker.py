
from enum import Enum

class Checker(Enum):
    RED    = 'r'
    YELLOW    = 'y'

    def __str__(self):
        return self.value