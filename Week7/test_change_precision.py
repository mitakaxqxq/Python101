import unittest
from change_precision import change_precision, changePrecision
from decimal import Decimal


class TestChangePrecision(unittest.TestCase):

    def test_raises_exception_when_value_is_not_int(self):
        with self.assertRaises(TypeError):
            with change_precision('12'):
                raise TypeError

    def test_raises_exception_when_value_is_out_of_range(self):
        with self.assertRaises(ValueError):
            with change_precision(-2):
                raise ValueError

    def test_not_raises_exception_wiht_correct_value(self):
        expected = Decimal('3.4')
        with change_precision(2):
            result = Decimal('1.123132132') + Decimal('2.23232')
            self.assertEqual(expected, result)


class TestClassChangePrecsiion(unittest.TestCase):

    def test_raises_exception_when_value_is_not_int(self):
        with self.assertRaises(TypeError):
            with changePrecision('12'):
                raise TypeError('You must assign integer!')

    def test_raises_exception_when_value_is_out_of_range(self):
        with self.assertRaises(ValueError):
            with changePrecision(-2):
                raise ValueError('Integer must be positive!')

    def test_not_raises_exception_wiht_correct_value(self):
        expected = Decimal('3.4')
        with changePrecision(2):
            result = Decimal('1.123132132') + Decimal('2.23232')
            self.assertEqual(expected, result)


if __name__ == '__main__':
    unittest.main()
