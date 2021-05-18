from task03.hw3 import *


def test_of_example_one():
    assert (
        tic_tac_toe_checker([["-", "-", "o"], ["-", "x", "o"], ["x", "o", "x"]])
        == "unfinished!"
    )


def test_of_example_two():
    assert (
        tic_tac_toe_checker([["-", "-", "o"], ["-", "-", "o"], ["x", "x", "x"]])
        == "x wins!"
    )
