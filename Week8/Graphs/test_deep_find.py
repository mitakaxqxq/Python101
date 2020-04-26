import unittest
from deep_find import *


class TestDeepFindDfsFunction(unittest.TestCase):

    def test_raises_exception_when_main_data_is_not_dictionary(self):
        exc = None
        try:
            deep_find_dfs([1, 2], 1)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Main data must be dictionary!')

    def test_returns_false_when_key_is_not_in_data(self):
        expected = False
        result = deep_find_dfs({2: 1}, 3)

        self.assertEqual(expected, result)

    def test_returns_correct_value_in_dictionary_with_only_basic_data_types(self):
        expected = 1
        result = deep_find_dfs({2: 1}, 2)

        self.assertEqual(expected, result)

    def test_returns_false_in_dictionary_with_string(self):
        expected = False
        result = deep_find_dfs({2: '21'}, 1)

        self.assertEqual(expected, result)

    def test_raises_exception_when_nested_data_is_not_dictionary(self):
        exc = None
        try:
            deep_find_dfs({1: [1, 2], 2: 1}, 3)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), "Type of iterable objects's values must be dictionaries!")

    def test_returns_false_when_key_is_not_in_nested_data(self):
        expected = False
        result = deep_find_dfs({1: {3: 4, 5: 6}, 2: 1}, 7)

        self.assertEqual(expected, result)

    def test_returns_correct_value_in_nested_dictionary(self):
        expected = 6
        result = deep_find_dfs({1: {3: 4, 5: 6}, 2: 1}, 5)

        self.assertEqual(expected, result)

    def test_returns_false_in_nested_dictionary_with_string(self):
        expected = False
        result = deep_find_dfs({1: {3: '21', 5: '22'}, 2: 1}, 7)

        self.assertEqual(expected, result)

    def test_returns_correct_value_in_list_of_dictionaries(self):
        expected = 229
        result = deep_find_dfs({1: [{3: 4, 5: 6}, {7: 229}], 2: 1}, 7)

        self.assertEqual(expected, result)


class TestDeepFindBfsFunction(unittest.TestCase):
    def test_raises_exception_when_main_data_is_not_dictionary(self):
        exc = None
        try:
            deep_find_bfs([1, 2], 1)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Main data must be dictionary!')

    def test_returns_false_when_key_is_not_in_data(self):
        expected = False
        result = deep_find_bfs({2: 1}, 3)

        self.assertEqual(expected, result)

    def test_returns_correct_value_in_dictionary_with_only_basic_data_types(self):
        expected = 1
        result = deep_find_bfs({2: 1}, 2)

        self.assertEqual(expected, result)

    def test_returns_false_in_dictionary_with_string(self):
        expected = False
        result = deep_find_bfs({2: '21'}, 1)

        self.assertEqual(expected, result)

    def test_raises_exception_when_nested_data_is_not_dictionary(self):
        exc = None
        try:
            deep_find_bfs({1: [1, 2], 2: 1}, 3)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), "Type of iterable objects's values must be dictionaries!")

    def test_returns_false_when_key_is_not_in_nested_data(self):
        expected = False
        result = deep_find_bfs({1: {3: 4, 5: 6}, 2: 1}, 7)

        self.assertEqual(expected, result)

    def test_returns_correct_value_in_nested_dictionary(self):
        expected = 6
        result = deep_find_bfs({1: {3: 4, 5: 6}, 2: 1}, 5)

        self.assertEqual(expected, result)

    def test_returns_false_in_nested_dictionary_with_string(self):
        expected = False
        result = deep_find_bfs({1: {3: '21', 5: '22'}, 2: 1}, 7)

        self.assertEqual(expected, result)

    def test_returns_correct_value_in_list_of_dictionaries(self):
        expected = 229
        result = deep_find_bfs({1: [{3: 4, 5: 6}, {7: 229}], 2: 1}, 7)

        self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
