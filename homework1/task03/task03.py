"""
Write down the function, which reads input line-by-line, and find maximum and minimum values.
Function should return a tuple with the max and min values.

For example for [1, 2, 3, 4, 5], function should return [1, 5]

We guarantee, that file exists and contains line-delimited integers.

To read file line-by-line you can use this snippet:

with open("some_file.txt") as fi:
    for line in fi:
        ...

"""
from typing import Union


def find_maximum_and_minimum(file_name: str) -> Union[list, str]:
    try:
        file = open(file_name)
        file.close()
    except FileNotFoundError:
        return "There is no such file in this directory!"
    with open(file_name) as f:
        try:
            [int(i) for i in f.readlines()]
        except ValueError:
            return "file must contain only integers!"
    with open(file_name) as f:
        numbers_list = [int(i) for i in f.readlines()]
        a = min(numbers_list)
        b = max(numbers_list)
        return [a, b]
