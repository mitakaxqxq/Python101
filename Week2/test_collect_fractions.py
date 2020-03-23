import unittest
from collect_fractions import validate_values,collect_fractions,LCM,check_zero_denominator,check_fraction_length_bigger_than_required,check_fraction_length_lower_than_required

class TestValidateValues(unittest.TestCase):
    def test_input_if_it_is_given_as_tuple_of_tuples(self):
        exc = None
        try:
            validate_values(((1,2),(3,4)))
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Passed fractions are not in the form of a list of tuples')

    def test_input_if_it_is_given_as_dictionary_of_tuples(self):
        exc = None
        try:
            validate_values({1:2,3:4})
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Passed fractions are not in the form of a list of tuples')

    def test_input_if_there_are_more_than_two_fractions(self):
        exc = None
        try:
            validate_values([(1,2),(3,4),(5,6)])
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'More than 2 fractions are being passed for the program to collect')

    def test_input_if_there_is_fraction_with_more_than_two_elements(self):
        exc = None
        try:
            validate_values([(1,2),(3,4,5)])
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'There is a fraction with more than two elements')

    def test_input_if_there_is_fraction_with_less_than_two_elements(self):
        exc = None
        try:
            validate_values([(1,2),(3,)])
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'There is a fraction with less than two elements')


    def test_input_if_there_is_a_fraction_whose_denominator_is_zero(self):
        exc = None
        try:
            validate_values([(1,0),(2,3)])
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Second element of one of the fractions is zero - cannot divide by zero!!!')

class TestLCM(unittest.TestCase):
    def test_LCM_with_zero(self):
        fract = (0,99)
        first,second = fract
        self.assertEqual(0,LCM(first,second))
    
    def test_LCM_with_negative_number(self):
        fract = (-12,28)
        first,second = fract
        self.assertEqual(-84,LCM(first,second))

class TestCollectFractions(unittest.TestCase):
    def test_collecting_of_fractions_when_no_need_of_simplifying(self):
        result = collect_fractions([(1,2),(1,3)])
        self.assertEqual(result,(5,6))

    def test_collecting_of_fractions_when_there_is_need_of_simplifying(self):
        result = collect_fractions([(1,2),(2,10)])
        self.assertEqual(result,(7,10))

if __name__ == '__main__':
    unittest.main()