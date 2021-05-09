from task02.hw2 import *


def test_of_example():
    """Testing of example"""
    assert custom_sum.__doc__ == "This function can sum any objects which have __add___"
    assert custom_sum.__name__ == "custom_sum"
    assert str(custom_sum.__original_func).startswith("<function custom_sum at")
