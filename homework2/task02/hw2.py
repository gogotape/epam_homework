"""
Given an array of size n, find the most common and the least common elements.
The most common element is the element that appears more than n // 2 times.
The least common element is the element that appears fewer than other.

You may assume that the array is non-empty and the most common element
always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3, 2

Example 2:

Input: [2,2,1,1,1,2,2]
Output: 2, 1

"""
from typing import List


def major_and_minor_elem(inp: List) -> tuple:
    d = dict()
    for i in inp:
        d[i] = d.get(i, 0) + 1
    most_common = 0
    least_common = 1000
    most_common_element = None
    least_common_element = None
    for key, times in d.items():
        if times > most_common:
            most_common = times
            most_common_element = key
        if times < least_common:
            least_common = times
            least_common_element = key
    return (most_common_element, least_common_element)
