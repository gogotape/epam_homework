from task05.hw5 import *


def test_example_1():
    """Testing example 1"""
    assert custom_range(string.ascii_lowercase, "g") == ["a", "b", "c", "d", "e", "f"]


def test_example_2():
    """Testing example 2"""
    assert custom_range(string.ascii_lowercase, "g", "p") == [
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
    ]


def test_example_3():
    """Testing example 3"""
    assert custom_range(string.ascii_lowercase, "p", "g", -2) == [
        "p",
        "n",
        "l",
        "j",
        "h",
    ]


def test_custom_example_1():
    """Testing my example 1"""
    assert custom_range("123456789abcdefgh", "c") == [
        "1",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "a",
        "b",
    ]


def test_custom_example_2():
    """Testing my example 2"""
    assert custom_range("123456789abcd", "a", "7", -1) == ["a", "9", "8"]
