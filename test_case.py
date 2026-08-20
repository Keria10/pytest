import pytest

class TestClass:
    def test_one(self):
        a = 2
        b = 2
        assert a+b ==4

    def test_two(self):
        a = 3
        b = 4
        assert a+b == 8
    def test_three(self):
        a = 4
        b = 6
        assert a+b == 10