import unittest
from sort_fractions import validate_values,sort_fractions

class TestValidateValues(unittest.TestCase):
    def test_validation_of_first_argument(self):
        exc = None

        try:
            validate_values(((1,2),(3,4)),1)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'First argument is not list')

    def test_validation_of_second_argument(self):
        exc = None

        try:
            validate_values([(1,2),(3,4)],[])
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Second argument is not boolean')

class TestSortingOfFractions(unittest.TestCase):
    def test_sorting_in_ascending_order(self):
        myList = [(2, 3), (1, 2), (5, 6), (1, 3)]
        expectedList = [(1, 3), (1, 2), (2, 3), (5, 6)]

        result = sort_fractions(myList)
        
        self.assertEqual(result,expectedList)

    def test_sorting_in_descending_order(self):
        myList = [(2, 3), (1, 2), (5, 6), (1, 3)]
        expectedList = [(5, 6), (2, 3), (1, 2), (1, 3)]

        result = sort_fractions(myList,False)
        
        self.assertEqual(result,expectedList)


if __name__ == '__main__':
    unittest.main()