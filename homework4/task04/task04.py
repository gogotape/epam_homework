"""
Write a function that takes a number N as an input and returns N FizzBuzz numbers*
Write a doctest for that function.
Write a detailed instruction how to run doctests**.

That how first steps for the instruction may look like:
 - Install Python 3.8 (https://www.python.org/downloads/)
 - Install pytest `pip install pytest`
 - Clone the repository <path your repository>
 - Checkout branch <your branch>
 - Open terminal
 - ...


Definition of done:
 - function is created
 - function is properly formatted
 - function has doctests
 - instructions how to run doctest with the pytest are provided

You will learn:
 - the most common test task for developers
 - how to write doctests
 - how to run doctests
 - how to write instructions


fizzbuzz(5)
["1", "2", "fizz", "4", "buzz"]

* https://en.wikipedia.org/wiki/Fizz_buzz
** Энциклопедия профессора Фортрана page 14, 15, "Робот Фортран, чисть картошку!"
"""
from typing import List


def fizzbuzz(n: int) -> List[str]:
    """A function that takes a number N as an input
    and returns N FizzBuzz numbers
       >>> fizzbuzz(5)
       ['1', '2', 'fizz', '4', 'buzz']
       >>> fizzbuzz(11)
       ['1', '2', 'fizz', '4', 'buzz', 'fizz', '7', '8', 'fizz', 'buzz', '11']"""
    out = list()
    for number in range(1, n + 1):
        if number % 3 == 0 and number % 5 == 0:
            out.append("fizz buzz")
        elif number % 3 == 0:
            out.append("fizz")
        elif number % 5 == 0:
            out.append("buzz")
        else:
            out.append(str(number))
    return out


if __name__ == "__main__":
    import doctest

    doctest.testmod()
