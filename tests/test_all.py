import pytest


class TestClass:
    value = 0

    def test_this_is_a_demo(self):
        self.value = 1
        assert self.value == 1, "value wasn't 1"
