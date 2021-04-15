from task05.task05 import find_maximal_subarray_sum


def test_positive_case():
    """Testing of example"""
    assert find_maximal_subarray_sum([1, 3, -1, -3, 5, 3, 6, 7], 3)


def test_positive_case1():
    """Testing list with len = 1"""
    assert find_maximal_subarray_sum([1], 1)


