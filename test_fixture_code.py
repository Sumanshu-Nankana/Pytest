from fixture_code import StudentDB
import pytest

# def test_scott_data():
#     db = StudentDB()
#     db.connect('data.json')
#     scott_data = db.get_data('Scott')
#     assert scott_data['id'] == 1
#     assert scott_data['name'] == 'Scott'
#     assert scott_data['result'] == 'pass'


# def test_mark_data():
#     db = StudentDB()
#     db.connect('data.json')
#     mark_data = db.get_data('Mark')
#     assert mark_data['id'] == 2
#     assert mark_data['name'] == 'Mark'
#     assert mark_data['result'] == 'fail'

# Normally we write test-cases as above - the commented part
# But if we notices above code - we are repeating the code 
# i.e. initializing the Class or creating an object of a class and connecting with database
# But if we 100 of test, - we need to repeat same code 100 times
# also these initialization is resource intensive
# ======================================================================================


# So we have 2 solutions:
# 1) Setup and TearDown method
# 2) Pytest Fixture

# METHOD -1 - SETUP and TEARDOWN METHOD
# These method are inhertited from 'module' class
# These will automatically call at starting of code

# db = None
# def setup_module(module):
#     print("** Setup Method ***")
#     global db
#     db = StudentDB()
#     db.connect('data.json')

# def teardown_module(module):
#     print("** Tear Down Method ***")
#     # Here we can close your connection etc
#     # we don't have any close method
#     # Just cretaing dummy method
#     db.close()

# # Now we can remove those repeated statements
# def test_scott_data():
#     scott_data = db.get_data('Scott')
#     assert scott_data['id'] == 1
#     assert scott_data['name'] == 'Scott'
#     assert scott_data['result'] == 'pass'


# def test_mark_data():
#     mark_data = db.get_data('Mark')
#     assert mark_data['id'] == 2
#     assert mark_data['name'] == 'Mark'
#     assert mark_data['result'] == 'fail'

# =============================================================================
# METHOD - 2
# Pytest Fixture
# Instead of using Setup and teardown method 
# We can use pytest fixture  @pytest.fixture
# So it automatically called at starting
# if we not mention scope='module'
# This method called twice - but we want it only once.

@pytest.fixture(scope='module')
def db():
    print("** Started **")
    db = StudentDB()
    db.connect('data.json')
    return db

def test_scott_data(db):
    scott_data = db.get_data('Scott')
    assert scott_data['id'] == 1
    assert scott_data['name'] == 'Scott'
    assert scott_data['result'] == 'pass'


def test_mark_data(db):
    mark_data = db.get_data('Mark')
    assert mark_data['id'] == 2
    assert mark_data['name'] == 'Mark'
    assert mark_data['result'] == 'fail'

# ===================================================

# To add the tear-down functionality
# we can replace above method with below code
# instead of return we can use 'yield'
# @pytest.fixture(scope='module')
# def db():
#     print("** Started **")
#     db = StudentDB()
#     db.connect('data.json')
#     yield db
#     print("** Tear Down **")
#     db.close()