import unittest
from deep_update import *


class TestDeepUpdateFunction(unittest.TestCase):
    def test_raises_exception_when_main_data_is_not_dictionary(self):
        exc = None
        try:
            deep_update([1, 2], 1, 2)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Main data must be dictionary!')

    def test_raises_exception_when_NESTED_data_is_not_dictionary(self):
        exc = None
        try:
            deep_update({1: [1, 2], 2: 3}, 1, 2)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), "Type of iterable objects's values must be dictionaries!")

    def test_correctly_returns_empty_dictionary(self):
        result = deep_update({}, 1, 2)
        expected = {}

        self.assertEqual(result, expected)

    def test_correctly_returns_dictionary_with_key_not_replaced(self):
        result = deep_update({1: 2}, 3, 2)
        expected = {1: 2}

        self.assertEqual(result, expected)

    def test_correctly_returns_dictionary_with_key_replaced(self):
        result = deep_update({1: 2}, 1, 2)
        expected = {2: 2}

        self.assertEqual(result, expected)

    def test_correctly_returns_dictionary_with_replaced_nested_keys_in_list(self):
        my_dict = {1: 2, 3: [{4: 2, 5: 8}, {4: 229, 7: 89}]}
        result = deep_update(my_dict, 4, 'a')
        expected = {1: 2, 3: [{'a': 2, 5: 8}, {'a': 229, 7: 89}]}

        self.assertEqual(result, expected)

    def test_correctly_returns_dictionary_with_replaced_nested_keys_in_list_and_nested_dictionary(self):
        my_dict = {1: 2, 3: [{4: 2, 5: 8}, {4: 229, 7: 89}], 6: {4: 78}}
        result = deep_update(my_dict, 4, 'a')
        expected = {1: 2, 3: [{'a': 2, 5: 8}, {'a': 229, 7: 89}], 6: {'a': 78}}

        self.assertEqual(result, expected)

    def test_correctly_returns_dictionary_with_replaced_nested_keys_in_tuple_and_nested_dictionary(self):
        my_dict = {1: 2, 3: ({4: 2, 5: 8}, {4: 229, 7: 89}), 6: {4: 78}}
        result = deep_update(my_dict, 4, 'a')
        expected = {1: 2, 3: ({'a': 2, 5: 8}, {'a': 229, 7: 89}), 6: {'a': 78}}

        self.assertEqual(result, expected)

    def test_correctly_returns_dict_with_replaced_key_of_nested_dict_and_tuple_in_which_there_are_nested_keys(self):
        my_dict = {1: 2, 4: ({4: 2, 5: 8}, {4: 229, 7: 89}), 6: {4: 78}}
        result = deep_update(my_dict, 4, 'a')
        expected = {1: 2, 'a': ({'a': 2, 5: 8}, {'a': 229, 7: 89}), 6: {'a': 78}}

        self.assertEqual(result, expected)

    def test_correctly_returns_dict_with_replaced_key_of_nested_dict_and_list_in_which_there_are_nested_keys(self):
        my_dict = {1: 2, 4: [{4: 2, 5: 8}, {4: 229, 7: 89}], 6: {4: 78}}
        result = deep_update(my_dict, 4, 'a')
        expected = {1: 2, 'a': [{'a': 2, 5: 8}, {'a': 229, 7: 89}], 6: {'a': 78}}

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
