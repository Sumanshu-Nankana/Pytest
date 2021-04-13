# This is our main code

# Test cases will be in test_math_func
# Run the test cases using pytest as : pytest <name-of-test-file>
# pytest test_math_func.py
# we can also use -v flag (verbose) for more detail as : pytest test_math_func.py -v
# we can also run only using : pytest or py.test  (without providing the file name)
# it will automatically detect test_math_func file ; because we added test_ as a prefix


def add(x, y=2):
    return x + y

def product(x, y=2):
    return x * y