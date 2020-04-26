import unittest
from deep_apply import *


class TestMyFuncFunction(unittest.TestCase):
    def test_raises_exception_when_parameter_is_not_int(self):
        exc = None
        try:
            my_func('a')
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Wrong value - x must be int!')

    def test_returns_correct_value(self):
        expected = 3
        result = my_func(1)

        self.assertEqual(expected, result)


class TestDeepApplyFunction(unittest.TestCase):
    def test_raises_exception_when_func_is_not_of_function_type(self):
        exc = None
        try:
            deep_apply('my_func', 'aa')
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Func must be of type function!')

    def test_raises_exception_when_main_data_is_not_dictionary(self):
        exc = None
        try:
            deep_apply(my_func, 'aa')
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Main data must be dictionary!')

    def test_raises_exception_when_nested_data_is_not_dictionary(self):
        exc = None
        try:
            deep_apply(my_func, {1: ['aa', 2]})
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), "Type of iterable objects's values must be dictionaries!")

    def test_returns_correctly_empty_dictionary(self):
        expected = {}
        result = deep_apply(my_func, {})

        self.assertEqual(expected, result)

    def test_returns_correctly_dictionary_with_applied_function_over_main_keys(self):
        my_dict = {1: 3, 2: 5}
        expected = {3: 3, 4: 5}
        result = deep_apply(my_func, my_dict)

        self.assertEqual(expected, result)

    def test_returns_correctly_dictionary_with_applied_function_over_main_and_nested_keys(self):
        my_dict = {1: 2, 4: 6, 6: {4: 78}}
        expected = {3: 2, 6: 6, 8: {6: 78}}
        result = deep_apply(my_func, my_dict)

        self.assertEqual(expected, result)

    def test_returns_correctly_dict_with_applied_function_over_main_and_nested_keys_and_dicts_in_list(self):
        my_dict = {1: 2, 4: [{4: 2, 5: 8}, {4: 229, 7: 89}], 6: {4: 78}}
        expected = {3: 2, 6: [{6: 2, 7: 8}, {6: 229, 9: 89}], 8: {6: 78}}
        result = deep_apply(my_func, my_dict)

        self.assertEqual(expected, result)

    def test_returns_correctly_dict_with_applied_function_over_main_and_nested_keys_and_dicts_in_tuple(self):
        my_dict = {1: 2, 4: ({4: 2, 5: 8}, {4: 229, 7: 89}), 6: {4: 78}}
        expected = {3: 2, 6: ({6: 2, 7: 8}, {6: 229, 9: 89}), 8: {6: 78}}
        result = deep_apply(my_func, my_dict)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()