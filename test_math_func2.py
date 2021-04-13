import math_func

def test_add():
    assert math_func.add(7, 3) == 10
    assert math_func.add(7) == 9
    assert math_func.add(5) == 7

def test_product():
    assert math_func.product(5, 5) == 25
    assert math_func.product(5) == 10

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


# If out of 2 tests in file, we want to run only 1 test
# we need to mention test case name as well while runnin pytest command as
# pytest <name-of-file>::<function_which_we_want_to_run>
# pytest test_math_func2.py::test_add_strings

# we can pass expression as well while running pytest
# -k is used for expression
# So it execute only those test cases which contains that particular string
# pytest <file-name> -k <test_case_function_expression>
# pytest test_math_func2.py -k "add"
# So using above command test_add and test_add_strings test cases will execute only.

# we can also use 'OR' operator while giving expression
# pytest test_math_func2.py -k "add or string"
# So out of 4 test cases only 3 will execute i.e.
# test_add, test_add_strings , test_product_string

# we can also use 'and' operator while using expression
# pytest test_math_func2.py -k "add and string" -v
# So only 1 test case will run i.e. test_add_strings