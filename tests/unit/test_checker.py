
from checker import Checker

class TestBoard:

    def test__str__(self):
        checker = Checker.RED;
        assert(str(checker) == Checker.RED.value)