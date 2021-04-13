import math_func

# in test_ file, the testing function should be start from test_

# we can give multiple assert as well
def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7
    # assert math_func.add(6) == 10 - This is wrong test case so gave assertion error
    # and 1 test passed and 1 test failed

def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10

# if we don not provide test_ prefix in test function name
# test case will not be recognized,
# only those test cases will be reconized where test_ prefix is mentioned.

