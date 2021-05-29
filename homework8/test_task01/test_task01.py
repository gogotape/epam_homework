from task01.task01 import *


def test_of_example():
    """Testing important moments"""
    storage = KeyValueStorage("../task01/task1.txt")
    assert storage.name == "kek"
    assert storage["name"] == "kek"
    assert type(storage["power"]) is int
