import unittest
import itertools
from generators import *


class TestChainGenerator(unittest.TestCase):

    def test_raises_exception_when_objects_types_are_not_equal(self):
        exc = None
        try:
            list(chain([1, 2], {1: 2}))
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Objects types must be equal!')

    def test_passes_with_correct_types_of_two_iterable_objects(self):
        result = list(chain(range(0, 4), range(4, 8)))
        expected = [x for x in range(0, 8)]

        self.assertEqual(result, expected)


class TestCompressGenerator(unittest.TestCase):

    def test_raises_exception_when_value_in_mask_is_not_bool(self):
        exc = None
        try:
            list(compress(["Ivo", "Rado", "Panda"], ['as', False, True]))
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Object in mask is not bool!')

    def test_passes_with_correct_values_in_mask(self):
        result = list(compress(["Ivo", "Rado", "Panda"], [False, False, True]))
        expected = ["Panda"]

        self.assertTrue(expected == result, 'Lists are equal')


class TestCycleGenerator(unittest.TestCase):

    def test_cycle_with_islice(self):
        endless = cycle([1, 2, 3])
        expected = [1, 2, 3, 1, 2, 3]
        result = list(itertools.islice(endless, 6))

        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
