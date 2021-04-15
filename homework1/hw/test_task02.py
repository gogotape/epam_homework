import pytest
from task02 import check_fibonacci


def test_positive_case():
    """Testing that 1, 1, 3, 5 is Fibo Sec"""
    assert check_fibonacci([1, 1, 2, 3, 5])


def test_positive_case1():
    """Testing that 1 Fibo Sec"""
    assert check_fibonacci([1])


def test_positive_case2():
    """Testing that 0,1,1 is Fibo Sec"""
    assert check_fibonacci([0,1,1])


def test_positive_case3():
    """Testing that 0,1,1,2,3,5,8,13,21,34,55 is Fibo Sec"""
    assert check_fibonacci([0,1,1,2,3,5,8,13,21,34,55])


def test_negative_case():
    """Testing that 0,1,1,2,3,5,8,13,21,34,55,1000 is not Fibo Sec"""
    assert not check_fibonacci([0,1,1,2,3,5,8,13,21,34,55,1000])


def test_negative_case1():
    """Testing that 2 is not Fibo Sec"""
    assert not check_fibonacci([2])


def test_negative_case2():
    """Testing that 5,7,12 is not Fibo Sec"""
    assert not check_fibonacci([5,7,12])


