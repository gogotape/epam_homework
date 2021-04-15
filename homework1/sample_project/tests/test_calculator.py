import pytest

from calculator.calc import check_power_of_2


def test_positive_case():
    """Testing that actual powers of 2 give True"""
    assert check_power_of_2(65536)


def test_negative_case1():
    """Testing that non-powers of 2 give False"""
    assert not check_power_of_2(12)    


def test_negative_case2():
    """Testing that zero is not power of 2. give False"""
    assert not check_power_of_2(0)


def test_negative_case3():
    """Testing that non-int input() will not crash the program"""
    assert 'The input value must be an integer'