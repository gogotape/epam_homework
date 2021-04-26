"""
In previous homework task 4, you wrote a cache function that remembers other function output value.
Modify it to be a parametrized decorator, so that the following code::

    @cache(times=3)
    def some_function():
        pass


Would give out cached value up to `times` number only.
Example::

    @cache(times=2)
    def f():
        return input('? ')   # careful with input() in python2, use raw_input() instead

f()
    ? 1
    '1'
f()     # will remember previous value
    '1'
f()     # but use it up to two times only
    '1'
f()
    ? 2
    '2'
"""


def cache(**kwargs):  # accepting amount of calling with **kwargs
    def outer(func):
        memo = {"counter": 0}  # dict which remembers amount of calls
        last_value = (
            dict()
        )  # dict which remembers last input value (first call is special)
        flag = (
            dict()
        )  # dict which needs just to remember the fact of first call of function

        def wrapper():
            if memo["counter"] == 0 and not flag:  # first call of function
                result = func()
                last_value["key"] = result
                flag[
                    "now first call is happened"
                ] = "now first call is happened"  # after first call this part of
                # code will no be used
            elif (
                memo["counter"] < kwargs["times"] - 1
            ):  # checking if necessary amount of calls is reached or not
                memo["counter"] += 1
            else:  # if it's reached, now we reset to zero amount of calls and put in dict new 'last value'
                result = func()
                last_value["key"] = result
                memo["counter"] = 0
            return last_value["key"]

        return wrapper

    return outer


@cache(times=2)
def f():
    return input("? ")
