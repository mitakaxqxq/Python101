import unittest
from deep_find_all import *


class TestDeepFindAllDfsFunction(unittest.TestCase):
    def test_raises_exception_when_main_data_is_not_dictionary(self):
        exc = None
        try:
            deep_find_all_dfs([1, 2], 2)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Main data must be dictionary!')

    def test_raises_exception_when_data_in_nested_data_structure_is_not_dictionary(self):
        exc = None
        try:
            deep_find_all_dfs({1: [1, 2], 2: 1}, 1)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), "Type of iterable objects's values must be dictionaries!")

    def test_returns_correct_value_of_simple_dictionary(self):
        expected = [2]
        result = deep_find_all_dfs({1: 2, 3: 4}, 1)

        self.assertEqual(expected, result)

    def test_returns_empty_list_in_dictionary_with_no_such_key(self):
        expected = []
        result = deep_find_all_dfs({1: 2, 3: 4}, 4)

        self.assertEqual(expected, result)

    def test_returns_correct_values_in_dictionary_with_nested_dictionary(self):
        expected = [{4: 2, 5: 8}, 2]
        result = deep_find_all_dfs({1: 2, 3: 4, 4: {4: 2, 5: 8}}, 4)

        self.assertEqual(expected, result)

    def test_returns_correct_values_in_dictionary_with_nested_dictionary_in_data_structure(self):
        expected = [2, 229]
        result = deep_find_all_dfs({1: 2, 3: 4, 5: [{4: 2, 5: 8}, {4: 229, 7: 89}]}, 4)

        self.assertEqual(expected, result)


class TestDeepFindAllBfsFunction(unittest.TestCase):
    def test_raises_exception_when_main_data_is_not_dictionary(self):
        exc = None
        try:
            deep_find_all_bfs([1, 2], 2)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Main data must be dictionary!')

    def test_raises_exception_when_data_in_nested_data_structure_is_not_dictionary(self):
        exc = None
        try:
            deep_find_all_bfs({1: [1, 2], 2: 1}, 1)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), "Type of iterable objects's values must be dictionaries!")

    def test_returns_correct_value_of_simple_dictionary(self):
        expected = [2]
        result = deep_find_all_bfs({1: 2, 3: 4}, 1)

        self.assertEqual(expected, result)

    def test_returns_empty_list_in_dictionary_with_no_such_key(self):
        expected = []
        result = deep_find_all_bfs({1: 2, 3: 4}, 4)

        self.assertEqual(expected, result)

    def test_returns_correct_values_in_dictionary_with_nested_dictionary(self):
        expected = [{4: 2, 5: 8}, 2]
        result = deep_find_all_bfs({1: 2, 3: 4, 4: {4: 2, 5: 8}}, 4)

        self.assertEqual(expected, result)

    def test_returns_correct_values_in_dictionary_with_nested_dictionary_in_data_structure(self):
        expected = [98, 2, 229]
        result = deep_find_all_bfs({1: 2, 3: 4, 5: [{4: 2, 5: 8}, {4: 229, 7: 89}], 4: 98}, 4)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
