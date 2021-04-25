from task03.hw3 import *


def test_example_given_in_task():
    """Testing example given in task"""
    assert combinations([1, 2], [3, 4]) == [(1, 3), (1, 4), (2, 3), (2, 4)]


def test_example_with_more_longer_lists():
    """Testing list another example"""
    assert len(combinations([1, 2, 3], [4, 5, 6], [7, 8, 9])) == 27
