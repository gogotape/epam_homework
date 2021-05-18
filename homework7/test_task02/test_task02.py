from task02.hw2 import *


def test_of_example_one():
    assert backspace_compare("a##c", "#a#c") is True


def test_of_example_two():
    assert backspace_compare("a##c", "#a#c") is True


def test_of_example_three():
    assert backspace_compare("a#c", "b") is False
