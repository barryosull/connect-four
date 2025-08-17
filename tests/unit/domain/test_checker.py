
from domain.checker import Checker

class TestBoard:

    def test__str__(self):
        checker = Checker.RED;
        assert(str(checker) == Checker.RED.value)

    def test_opponent(self):
        assert(Checker.RED.opponent() == Checker.YELLOW)
        assert(Checker.YELLOW.opponent() == Checker.RED)