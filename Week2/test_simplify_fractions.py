import unittest
from simplify_fractions import validate_value,simplify_fraction,GCD

class TestValidateValues(unittest.TestCase):
    def test_validation_if_list_is_passed(self):
        exc = None
        try:
            validate_value([1,2])
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Passed fraction is not in the form of a tuple')

    def test_validation_if_dictionary_is_passed(self):
        exc = None
        try:
            validate_value({1:2})
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Passed fraction is not in the form of a tuple')

    def test_validation_if_tuple_with_more_than_two_elements_is_passed(self):
        exc = None
        try:
            validate_value((1,2,3,4))
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Passed tuple has more than two elements')

    def test_validation_if_tuple_with_less_than_two_elements_is_passed(self):
        exc = None
        try:
            validate_value((1,))
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Passed tuple has less than two elements')
    def test_validation_if_second_element_of_tuple_is_zero(self):
        exc = None
        try:
            validate_value((1,0))
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Second element is zero - cannot divide by zero!!!')

class TestGCD(unittest.TestCase):
    def test_gcd_method_with_numerator_greater_than_denominator(self):
        fraction = (72,60)

        x,y = fraction
        
        result = GCD(x,y)
        
        self.assertEqual(12,result)

    def test_gcd_method_with_numerator_lower_than_denominator(self):
        fraction = (12,60)
        
        x,y = fraction        
        
        result = GCD(x,y)
        
        self.assertEqual(12,result)

    def test_gcd_method_with_numerator_and_denominator_being_coprime(self):
        fraction = (12,23)

        x,y = fraction

        result = GCD(x,y)

        self.assertEqual(1,result)

class TestSimplifyFraction(unittest.TestCase):
    def test_simplify_fraction(self):
        result = simplify_fraction((333,27))
        self.assertEqual(result,(37,3))


if __name__ == '__main__':
    unittest.main()