from task03.task03 import *


def testing_class_Filter():
    """ Testing class Filter """
    positive_even = Filter(lambda a: a % 2 == 0 and a > 0 and isinstance(a, int))
    assert positive_even.apply(range(10)) == [2, 4, 6, 8]


def testing_my_make_filter_func():
    """ Testing my make filter func """
    assert my_own_make_filter(sample_data, name="polly", type="bird") == {
        "is_dead": True,
        "kind": "parrot",
        "type": "bird",
        "name": "polly",
    }
