from task04.task04 import check_sum_of_four


def test_positive_case1():
    """Testing the easiest case"""
    assert check_sum_of_four([1], [2], [3], [-6])


def test_positive_case2():
    """Testing more harder case"""
    assert check_sum_of_four([1], [2], [3], [-6])


def test_negative_case1():
    """Testing case with absentee excepted result"""
    assert not check_sum_of_four([1], [2], [3], [-5])
