from task02.task02 import *


def test_of_work_foo_len():
    presidents = TableData("../task02/example.sqlite", "presidents")
    assert len(presidents) == 3


def test_of_work_access_by_name_of_president():
    presidents = TableData("../task02/example.sqlite", "presidents")
    assert type(presidents["Yeltsin"]) is tuple and presidents["Yeltsin"]


def test_positive_case_checking_of_work_operator_in():
    presidents = TableData("../task02/example.sqlite", "presidents")
    assert "Yeltsin" in presidents


def test_negative_case_checking_of_work_operator_in():
    presidents = TableData("../task02/example.sqlite", "presidents")
    assert "Putin" not in presidents


def test_of_iteration_protocol():
    presidents = TableData("../task02/example.sqlite", "presidents")
    for president in presidents:
        assert type(president) is list
