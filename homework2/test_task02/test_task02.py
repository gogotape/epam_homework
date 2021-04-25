from task02.hw2 import *


def test_example_1():
    """Testing list [3,2,3], expecting 3, 2"""
    assert major_and_minor_elem([3, 2, 3]) == (3, 2)


def test_example_2():
    """Testing list [2,2,1,1,1,2,2], expecting 2, 1"""
    assert major_and_minor_elem([2, 2, 1, 1, 1, 2, 2]) == (2, 1)


def test_example_3():
    """Testing list [2,2,2,3,3,3,4,4,5,5,5,6,6,6,6,6,6,6,6,1], expecting 6, 1"""
    assert major_and_minor_elem(
        [2, 2, 2, 3, 3, 3, 4, 4, 5, 5, 5, 6, 6, 6, 6, 6, 6, 6, 6, 1]
    ) == (6, 1)
