def test_simplest():
    assert True

'''
Compare to `unittest`:

from unittest import TestCase

class TestSimple(TestCase):
    def test_simple(self):
        self.assertTrue(True)

'''

def is_empty(value):
    return len(value) == 0

def test_empty_list():
    assert is_empty([]) is True

def test_empty_dict():
    assert is_empty({}) is True

def test_list_is_not_empty():
    assert is_empty([1,2,3]) is False

def test_dict_is_not_empty():
    assert is_empty({"item": 1}) is False

'''
We want a function that can default to False if the inputs are garbage.
'''
# def test_integer_is_false():
#     assert is_empty(1) is False

'''
This test has an error like this:

________________________________________ test_integer_is_false ________________________________________

    def test_integer_is_false():
>       assert is_empty(1) is False

chapter3/simplest_test.py:34: 
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _

value = 1

    def is_empty(value):
>       return len(value) == 0
E       TypeError: object of type 'int' has no len()

chapter3/simplest_test.py:16: TypeError

'''

def is_empty2(value):
    try:
        return len(value) == 0
    except TypeError:
        return False

def test_integer_is_false():
    assert is_empty2(1) is False

# def assert_flow_control(value):
#     """
#     An example on flow control with bare asserts
#     """
#     assert value
#     return 'got a value of expected type!'

# def test_assert_false():
#     assert_flow_control(False)


def test_long_strings():
    string = ("This is a very, very, long string that has some differences"
            " that are hard to catch")
    expected = ("This is a very, very long string that hes some differences"
            " that are hard to catch")
    assert string == expected

def test_nested_dictionaries():
    result = {
        'first': 12,
        'second': 13,
        'others': {
            'success': True,
            'msg': 'A success message!',
        },
    }
    expected = {
        'first': 12,
        'second': 13,
        'others': {
            'success': True,
            'msg': 'A sucess message!',
        },
    }

    assert result == expected
