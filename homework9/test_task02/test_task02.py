from task02.hw2 import *


def test_of_work_a_contex_manager_using_class():
    with Supressor(IndexError):
        [][2]
    assert True


def test_of_work_a_contex_manager_using_generator():
    with pass_exception(IndexError):
        [][2]
    assert True
