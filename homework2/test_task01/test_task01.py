from task01.hw1 import *


def test_positive_case1():
    """Testing of work 1st func"""
    assert get_longest_diverse_words("data.txt")


def test_positive_case2():
    """Testing of work 2st func"""
    assert get_rarest_char("data.txt")


def test_positive_case3():
    """Testing of work 3st func"""
    assert count_punctuation_chars("data.txt")


def test_positive_case4():
    """Testing of work 4st func"""
    assert count_non_ascii_chars("data.txt")


def test_positive_case5():
    """Testing of work 5st func"""
    assert get_most_common_non_ascii_char("data.txt")
