def check_power_of_2(a: int) -> bool:
    if type(a) != int:
        return 'The input value must be an integer'
    if a == 0:
        return False
    else:
        return not (bool(a & (a - 1)))
