"""
Given a dictionary (tree), that can contains multiple nested structures.
Write a function, that takes element and finds the number of occurrences
of this element in the tree.

Tree can only contains basic structures like:
    str, list, tuple, dict, set, int, bool
"""
from typing import Any

# Example tree:
example_tree = {
    "first": ["RED", "BLUE"],
    "second": {
        "simple_key": ["simple", "list", "of", "RED", "valued"],
    },
    "third": {
        "abc": "BLUE",
        "jhl": "RED",
        "complex_key": {
            "key1": "value1",
            "key2": "RED",
            "key3": ["a", "lot", "of", "values", {"nested_key": "RED"}],
        },
    },
    "fourth": "RED",
}

counter = 0


def find_occurrences(tree: dict, element: Any) -> int:
    global counter
    for item in tree:
        if type(tree[item]) is dict:
            find_occurrences(tree[item], element)
        elif type(tree[item]) is list:
            for value in tree[item]:
                if type(value) is not dict:
                    if value == element:
                        counter += 1
                else:
                    find_occurrences(value, element)
        elif type(tree[item]) is str:
            if tree[item] == element:
                counter += 1
    return counter
