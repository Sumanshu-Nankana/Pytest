# we can also use the "-m" option in command line, while running pytest
# -m is used for mark

import mark_pytest
import pytest

@pytest.mark.addition
def test_add():
    assert mark_pytest.add(7, 3) == 10
    assert mark_pytest.add(7) == 9

@pytest.mark.multiplication
def test_product():
    assert mark_pytest.product(5, 5) == 25
    assert mark_pytest.product(5) == 10

@pytest.mark.addition
def test_add_string():
    assert mark_pytest.add("Hello ", "World") == "Hello World"


# So only those test cases will execute for which -m expression marker matched
# pytest test_mark_pytest.py -m addition -v  ==> only test_add & test_add_string test will run
# pytest test_mark_pytest.py -m multiplication -v  ==> only test_product test will run