from task02.task02 import *


def morning_discount(price):
    return price * 0.5


def elder_discount(price):
    return price * 0.1


def test_of_example():
    morning_order = Order(100, morning_discount)
    elder_order = Order(1000, elder_discount)
    assert morning_order.final_price() == 50.0
    assert elder_order.final_price() == 100.0
