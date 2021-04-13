import math_func

def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7
    assert math_func.add(6) == 10 # wrong test case
    # and 1 test passed and 1 test failed

def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10


# If we run this file as: pytest test_math_func1.py -v => It will execute all test cases
# and at last it shows report, how many passed and how many failed

# we can also use -x option => as : pytest test_math_func1.py -x -v
# which means processing terminate as soon as first test case failed
# it will not even execute rest test cases
# So in this case as first test will fail, it will not even execute 2nd test case 

# if we don't want to see the "Error Information" of failed test case
# we can off the trace using --tb=no    parameter
# pytest test_math_func1.py --tb=no -v
