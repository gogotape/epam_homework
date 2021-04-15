from task03.task03 import find_maximum_and_minimum


def test_positive_case1():
    """Testing first file"""
    assert find_maximum_and_minimum("test_file1")


def test_positive_case2():
    """Testing second file"""
    assert find_maximum_and_minimum("test_file2")


def test_positive_case3():
    """Testing file which contains only one value"""
    assert find_maximum_and_minimum("test_file3")


def test_negative_case1():
    """Testing file which contains non-integer values"""
    assert find_maximum_and_minimum("test_file4")
