from task02.task02 import *


# i didn't figured out how to create "mock" object instead of real web site
def test_example():
    """Test example"""
    assert count_dots_on_i("https://en.wikipedia.org/wiki/Mock_object") == 5153
