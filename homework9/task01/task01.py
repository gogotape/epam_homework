"""
Write a function that merges integer from sorted files and returns an iterator

file1.txt:
1
3
5

file2.txt:
2
4
6

list(merge_sorted_files(["file1.txt", "file2.txt"]))
[1, 2, 3, 4, 5, 6]
"""

"""
from pathlib import Path
from typing import List, Union, Iterator


def merge_sorted_files(file_list: List[Union[Path, str], ...]) -> Iterator:
    pass
"""
from pathlib import Path
from typing import Iterator, List, Union


def merge_sorted_files(file_list: List[Union[Path, str]]) -> Iterator:

    data, merged_list = list(), list()
    for file in file_list:
        with open(file) as fi:
            data.append([int(i[-2]) for i in fi.readlines()])

    number_of_integer = 0

    while True:
        try:
            for list_of_integers in data:
                merged_list.append(list_of_integers[number_of_integer])
            number_of_integer += 1
        except IndexError:
            break

    return iter(merged_list)
