# Lets suppose we use some print() statement inside our test cases
# and we want to print those statement
# By default these  print statement not printed
# So we need to use "-s" option
# pytest test_print.py -v -s

import math_func
import pytest
import sys

def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7
    print("Test case 1st Completed")

@pytest.mark.skipif(sys.version_info < (3,3), reason="Do Not run integer product")
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
