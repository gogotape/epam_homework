from task01.task01 import *


def test_of_example_2_files_case():
    assert list(merge_sorted_files(["file1.txt", "file2.txt"])) == [1, 2, 3, 4, 5, 6]


def test_of_3_files_case():
    assert list(merge_sorted_files(["file1.txt", "file2.txt", "file3.txt"])) == [
        1,
        2,
        7,
        3,
        4,
        8,
        5,
        6,
        9,
    ]
