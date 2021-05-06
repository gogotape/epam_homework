import os

from task01.task01 import read_magic_number


def test_of_2():
    """Test of 2"""
    with open(r"..\task01\data.txt", "w") as fi:
        fi.write("2")
    assert read_magic_number(r"..\task01\data.txt")
    os.remove(r"..\task01\data.txt")


def test_of_3():
    """Test of 3"""
    with open(r"..\task01\data.txt", "w") as fi:
        fi.write("3")
    assert not read_magic_number(r"..\task01\data.txt")
    os.remove(r"..\task01\data.txt")


def test_of_1():
    """Test of 1"""
    with open(r"..\task01\data.txt", "w") as fi:
        fi.write("1")
    assert read_magic_number(r"..\task01\data.txt")
    os.remove(r"..\task01\data.txt")


def test_of_some_string():
    """Test of some str"""
    with open(r"..\task01\data.txt", "w") as fi:
        fi.write("some_string")
    assert read_magic_number(r"..\task01\data.txt") == "This is not a number"
    os.remove(r"..\task01\data.txt")


def test_of_7():
    """Test of 7"""
    with open(r"..\task01\data.txt", "w") as fi:
        fi.write("7")
    assert not read_magic_number(r"..\task01\data.txt")
    os.remove(r"..\task01\data.txt")


def test_of_float_line():
    """Test of 1.00000000000001"""
    with open(r"..\task01\data.txt", "w") as fi:
        fi.write("1.00000000000001")
    assert read_magic_number(r"..\task01\data.txt")
    os.remove(r"..\task01\data.txt")
