import unittest
from generators import *


class TestChainGenerator(unittest.TestCase):

    def test_raises_exception_when_first_object_in_chain_is_not_iterable(self):
        exc = None
        try:
            chain(1, [1, 2, 3])
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Argument 1 not of type Iterable')

    def test_raises_exception_when_second_object_in_chain_is_not_iterable(self):
        exc = None
        try:
            chain([1, 2], 3)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Argument 2 not of type Iterable')

    def test_raises_exception_when_objects_types_are_not_equal(self):
        exc = None
        try:
            chain([1, 2], {1: 2})
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Objects types must be equal!')

    def test_passes_with_correct_types_of_two_iterable_objects(self):
        result = list(chain(range(0, 4), range(4, 8)))
        expected = [x for x in range(0, 8)]

        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main()
