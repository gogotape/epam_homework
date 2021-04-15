def check_power_of_2(a: int) -> bool:
    if type(a) != int:
        return False
    if a == 0:
        return False
    else:
        return not (bool(a & (a - 1)))
