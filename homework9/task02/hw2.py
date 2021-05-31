"""
Write a context manager, that suppresses passed exception.
Do it both ways: as a class and as a generator.

with supressor(IndexError):
...    [][2]

"""
from contextlib import contextmanager


class Supressor:
    def __init__(self, error_type):
        self.error_type = error_type

    def __enter__(self):
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is self.error_type:
            return True


@contextmanager
def pass_exception(error_type):
    try:
        yield
    except error_type:
        pass


if __name__ == "__main__":
    with Supressor(IndexError):
        [][2]

    with pass_exception(IndexError):
        [][2]
