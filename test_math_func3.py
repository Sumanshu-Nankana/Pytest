# we have one more option as maxfail
# pytest test_math_func3.py -v --maxfail=2
# which means it will wait for maximum number of failure before exit
# Lets create 1 failure and then run using --maxfail==1 and --maxfail==2

import math_func

def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7

def test_product():
    assert math_func.product(5, 5) == 25
    # we have introduce this failure
    # So if we introduce only this failure and run 
    # pytest test_math_func3.py -v --maxfail=1
    # So as soon as this failure aris count of maxfail hits 1
    # Thus, next test cases even not execute
    assert math_func.product(5) == 11

# if we run as: pytest test_math_func3.py -v --maxfail=1 ==> it did not execute other test cases as soon as it encounters 1 failure
# if we run as pytest test_math_func3.py -v --maxfail=2 ==> It executes other test cases as well, becase max failure count is not 2, it's only 1

# Lets write two more test cases to add strings and product strings

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
