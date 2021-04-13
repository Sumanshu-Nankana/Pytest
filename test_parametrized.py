import parametrized_code
import pytest

# # testing integers addition
# def test_add():
#     assert parametrized_code.add(7, 3) == 10


# # testing float addition
# def test_add_float():
#     assert parametrized_code.add(10.5, 25.5) == 36

# # testing string addition
# def test_add_strings():
#     assert parametrized_code.add("Hello ", "World") =="Hello World"


# # if we look above commented code - we could see
# # To test just add function, we need to write 3 test cases
# # yes, we can write 3 assert statements with in one function
# # But still we need to call add() function from code file which is parametrized.py 3 times
# # example

# # call al function
# def test_all():
#     assert parametrized_code.add(7, 3) == 10
#     assert parametrized_code.add(10.5, 25.5) == 36
#     assert parametrized_code.add("Hello ", "World") =="Hello World"

# So instead of doing all these - we can use parametrization
# using decorator as @pytest.mark.parametrize('input_parameters output_para',iterable)

@pytest.mark.parametrize('x, y, result',
                            [
                                (7, 3, 10),
                                (10.5, 25.5, 36),
                                ("Hello ", "World", "Hello World")
                            ]
                        )
def test_functions(x, y, result):
    assert parametrized_code.add(x, y) == result