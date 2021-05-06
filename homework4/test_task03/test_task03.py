from task03.task03 import *


def test_of_example_1():
    """Test of example one"""
    assert my_precious_logger("OK") == "OK"


def test_of_example_2():
    """Test of example two"""
    assert (
        my_precious_logger("error: file not found") == "Actually ext wrote into stderr"
    )
