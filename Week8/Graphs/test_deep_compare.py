import unittest
from deep_compare import *


class TestDeepCompareFunction(unittest.TestCase):
    def test_returns_true_when_comparing_two_empty_strings(self):
        result = deep_compare('', '')
        expected = True

        self.assertEqual(result, expected)

    def test_returns_true_when_comparing_two_empty_lists(self):
        result = deep_compare([], [])
        expected = True

        self.assertEqual(result, expected)

    def test_returns_true_when_comparing_two_empty_dictionaries(self):
        result = deep_compare({}, {})
        expected = True

        self.assertEqual(result, expected)

    def test_returns_true_when_comparing_two_dictionaries_with_same_keys_and_values(self):
        result = deep_compare({1: 2, 3: 4}, {3: 4, 1: 2})
        expected = True

        self.assertEqual(result, expected)

    def test_returns_false_when_comparing_two_dictionaries_with_same_keys_and_different_values(self):
        result = deep_compare({1: 2, 3: 4}, {3: 4, 1: 3})
        expected = True

        self.assertEqual(result, expected)

    def test_returns_false_when_comparing_two_different_dictionaries(self):
        result = deep_compare({1: [{1: 2, 3: 4}]}, {2: {3: 4, 1: 3}})
        expected = False

        self.assertEqual(result, expected)

    def test_returns_true_when_comparing_two_equal_dictionaries_with_different_positions_of_values(self):
        result = deep_compare({1: [{3: 5}, {2: 1, 3: 1, 4: 2}]}, {1: [{2: 1, 3: 1, 4: 2}, {3: 5}]})
        expected = True

        self.assertEqual(result, expected)

    def test_returns_true_when_comparing_two_equal_strings(self):
        result = deep_compare('123', '123')
        expected = True

        self.assertEqual(result, expected)

    def test_returns_false_when_comparing_two_different_strings(self):
        result = deep_compare('123', '1232')
        expected = False

        self.assertEqual(result, expected)

    def test_returns_true_when_comparing_two_non_empty_lists_of_dictionaries(self):
        result = deep_compare([{1: 2, 3: 4}, {5: 6}], [{5: 6}, {1: 2, 3: 4}])
        expected = True

        self.assertEqual(result, expected)

    def test_returns_false_when_comparing_two_non_empty_tuples_of_dictionaries(self):
        result = deep_compare(({1: 2, 3: 4}, {5: 6}), ({5: 6}, {1: 2, 3: 4}))
        expected = False

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
