import unittest
from my_sort_program import my_sort,validate_values,sort_list,sort_tuple,sort_dict

class TestValidateValues(unittest.TestCase):
    def test_validation_of_first_argument(self):
        exc = None

        try:
            validate_values(None,3,"")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'First argument not passed')
    def test_validation_of_second_argument(self):
        exc = None
        try:
            validate_values((1,2,3),'zdr',"")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Second argument is not bool')

    def test_validation_of_third_argument(self):
        exc = None
        try:
            validate_values([1,2,3,3],True,1)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Third argument is not string')

class TestSortingOfList(unittest.TestCase):
    def test_sorting_of_list_in_ascending_order(self):
        
        myList = [4,2,5,5,8,100,1]
        expectedList = [1,2,4,5,5,8,100]
        
        sort_list(myList,True)

        self.assertEqual(expectedList,myList)

    def test_sorting_of_list_in_descending_order(self):

        myList = [4,2,5,5,8,100,1]
        expectedList = [100,8,5,5,4,2,1]

        sort_list(myList,False)

        self.assertEqual(expectedList,myList)


class TestSortingOfTuple(unittest.TestCase):
    def test_sorting_of_tuple_in_ascending_order(self):

        myTuple = (4,2,5,5,8,100,1)
        expectedTuple = (1,2,4,5,5,8,100)
        
        result=sort_tuple(myTuple,True)

        self.assertEqual(expectedTuple,result)

    def test_sorting_of_tuple_in_descending_order(self):

        myTuple = (4,2,5,5,8,100,1)
        expectedTuple = (100,8,5,5,4,2,1)

        result=sort_tuple(myTuple,False)

        self.assertEqual(expectedTuple,result)


class TestSortingOfDictionary(unittest.TestCase):
    def test_sorting_of_dictionary_in_ascending_order(self):

        myListOfDictionaries = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]
        expectedListOfDictionaries = [{'name': 'Marto', 'age': 24}, {'name': 'Sashko', 'age': 25}, {'name': 'Ivo', 'age': 27}]

        sort_dict(myListOfDictionaries,True,'age')

        self.assertEqual(myListOfDictionaries,expectedListOfDictionaries)

    def test_sorting_of_dictionary_in_descending_order(self):
        myListOfDictionaries = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]
        expectedListOfDictionaries = [{'name': 'Ivo', 'age': 27},{'name': 'Sashko', 'age': 25}, {'name': 'Marto', 'age': 24} ]

        sort_dict(myListOfDictionaries,False,'age')

        self.assertEqual(myListOfDictionaries,expectedListOfDictionaries)


class TestMySort(unittest.TestCase):
    def test_my_sort_if_it_is_list_in_ascending_order(self):

        myList = [4,2,5,5,8,100,1]
        expectedList = [1,2,4,5,5,8,100]

        my_sort(myList,True)

        self.assertEqual(myList,expectedList)

    def test_my_sort_if_it_is_list_in_descending_order(self):

        myList = [4,2,5,5,8,100,1]
        expectedList = [100,8,5,5,4,2,1]

        my_sort(myList,False)

        self.assertEqual(myList,expectedList)

    def test_my_sort_if_it_is_tuple_in_ascending_order(self):

        myTuple = (4,2,5,5,8,100,1)
        expectedTuple = (1,2,4,5,5,8,100)

        result = my_sort(myTuple,True)

        self.assertEqual(result,expectedTuple)

    def test_my_sort_if_it_is_tuple_in_descending_order(self):

        myTuple = (4,2,5,5,8,100,1)
        expectedTuple = (100,8,5,5,4,2,1)

        result = my_sort(myTuple,False)

        self.assertEqual(result,expectedTuple)

    def test_my_sort_if_it_is_dictionary_in_ascending_order(self):

        myListOfDictionaries = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]
        expectedListOfDictionaries = [{'name': 'Marto', 'age': 24}, {'name': 'Sashko', 'age': 25}, {'name': 'Ivo', 'age': 27}]

        my_sort(myListOfDictionaries,True,'age')

        self.assertEqual(myListOfDictionaries,expectedListOfDictionaries)

    def test_my_sort_if_it_is_dictionary_in_descending_order(self):

        myListOfDictionaries = [{'name': 'Marto', 'age': 24}, {'name': 'Ivo', 'age': 27}, {'name': 'Sashko', 'age': 25}]
        expectedListOfDictionaries = [{'name': 'Ivo', 'age': 27},{'name': 'Sashko', 'age': 25}, {'name': 'Marto', 'age': 24} ]

        my_sort(myListOfDictionaries,False,'age')

        self.assertEqual(myListOfDictionaries,expectedListOfDictionaries)


if __name__ == '__main__':
    unittest.main()