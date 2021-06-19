from task01.task01 import *


class ColorsEnum(metaclass=SimplifiedEnum):
    __keys = ("RED", "BLUE", "ORANGE", "BLACK")


class SizesEnum(metaclass=SimplifiedEnum):
    __keys = ("XL", "L", "M", "S", "XS")


def test_of_example():
    assert ColorsEnum.RED == "RED"
    assert ColorsEnum.ORANGE == "ORANGE"

    assert SizesEnum.XL == "XL"
    assert SizesEnum.S == "S"
