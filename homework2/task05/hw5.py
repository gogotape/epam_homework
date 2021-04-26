"""
Some of the functions have a bit cumbersome behavior when we deal with
positional and keyword arguments.

Write a function that accept any iterable of unique values and then
it behaves as range function:


import string


assert = custom_range(string.ascii_lowercase, 'g') == ['a', 'b', 'c', 'd', 'e', 'f']
assert = custom_range(string.ascii_lowercase, 'g', 'p') == ['g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o']
assert = custom_range(string.ascii_lowercase, 'p', 'g', -2) == ['p', 'n', 'l', 'j', 'h']

"""


import string


def custom_range(s, *args):
    out = []
    if len(args) == 1:
        for i in range(s.index((s[0])), s.index((args[0]))):
            out.append(s[i])
    elif len(args) == 2:
        for i in range(s.index((args[0])), s.index((args[1]))):
            out.append(s[i])
    elif len(args) == 3:
        for i in range(s.index(args[0]), s.index(args[1]), args[2]):
            out.append(s[i])
    else:
        print("Expected 1, 2 or 3 positional arguments, but", len(args), 'got')
    return out

