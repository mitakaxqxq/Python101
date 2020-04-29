import unittest
from big_positive_pow import big_possitive_pow
from unittest.mock import patch


class TestBigPositivePow(unittest.TestCase):
    @patch('big_positive_pow.randint')
    def test_returns_correct_value(self, random_mock):
        random_mock.return_value = 3
        self.assertEqual(27, big_possitive_pow())

    @patch('big_positive_pow.randint')
    def test_raises_exception_when_value_is_less_than_one(self, random_mock):
        random_mock.return_value = -2
        with self.assertRaises(ValueError):
            big_possitive_pow()


if __name__ == '__main__':
    unittest.main()
