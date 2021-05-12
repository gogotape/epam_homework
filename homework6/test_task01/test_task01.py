from task01.counter import *


def simple_test_1():
    user_01 = User()
    assert user_01.get_created_instances() == 1


def simple_test_2():
    user_01 = User()
    user_02 = User()
    assert user_01.get_created_instances() == 2
    user_01.reset_instances_counter()
    user_03 = User()
    assert user_03.get_created_instances() == 1
