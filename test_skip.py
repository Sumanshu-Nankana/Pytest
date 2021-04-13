# we can also skip the test cases using decorator
# @pytest.mark.skip(reason="msg")
# So when we run:   pytest test_skip.py -v
# One test case will be skipped and rest 3 will execute

import math_func
import pytest

def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7

@pytest.mark.skip(reason="Do Not run integer product")
def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10

def test_add_strings():
    result = math_func.add('Hello', ' World')
    assert result == "Hello World"
    assert type(result) is str
    assert 'Heldoo' not in result

def test_product_strings():
    assert math_func.product('Hello ', 3) == 'Hello Hello Hello '
    assert math_func.product('Hello ') == 'Hello Hello '
    assert type(math_func.product('Hello ')) is str is str
    assert 'Hello ' in math_func.product('Hello ')
