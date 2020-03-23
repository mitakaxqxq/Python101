import unittest
from utils import validate_values,break_down_into_list_of_strings,convert_string_to_term,convert_string_into_polynomial,find_derivative_of_polynomial
from polynomial import Term,Polynomial

class TestValidationOfString(unittest.TestCase):
    
    def test_when_input_is_not_string(self):

        exc = None

        try:
            validate_values([1,2,3])
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Input has to be string!')

    def test_when_there_is_negative_sign_in_string(self):

        exc = None

        try:
            validate_values('-2x^5')
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Wrong input - all coefficients and powers must be positive integers')

    def test_when_there_is_division_sign_in_string(self):

        exc = None

        try:
            validate_values('2/3*x^6')
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Wrong input - you can not have fractions for coefficients in the polynomial')

    def test_when_there_is_unrecognizable_symbol_in_string(self):

        exc = None

        try:
            validate_values('2*x%7')
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Wrong input - you have entered a symbol which is unrecognizable in the polynomial')

    def test_when_the_value_is_in_front_of_the_coefficient(self):

        exc = None

        try:
            validate_values('x*2^7')
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Coefficient must be multiplied before the value x')

    def test_when_there_is_a_double_plus_sign_in_the_input_string(self):

        exc = None

        try:
            validate_values('2*x^7++2')
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect string - you have misspelled a sign in the string')

    def test_when_there_is_a_double_multiply_sign_in_the_input_string(self):

        exc = None

        try:
            validate_values('2**x^7+2')
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect string - you have misspelled a sign in the string')

    def test_when_there_is_a_double_power_sign_in_the_input_string(self):

        exc = None

        try:
            validate_values('2*x^^7+2x')
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect string - you have misspelled a sign in the string')

    def test_when_the_variable_is_missing_but_there_are_multiply_and_power_signs(self):

        exc = None

        try:
            validate_values('2*^4')
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Wrong input - calcualtion signs in input string but no variable')


    def test_when_the_variable_is_after_a_power_sign(self):

        exc = None

        try:
            validate_values('2*x^x4')
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Wrong input - variable is after a power sign')


class TestBreakingDownStringIntoListOfStrings(unittest.TestCase):

    def test_if_input_is_correctly_broken_into_strings(self):

        expected = ['123*x^56','12*x^20','x^782','123*x','1873223']

        result = break_down_into_list_of_strings('123*x^56+12*x^20+x^782+123*x+1873223')

        self.assertTrue(expected == result)

class TestConvertingStringIntoTerm(unittest.TestCase):

    def test_converting_when_there_are_both_coefficient_and_power(self):

        expected = Term(123,56)

        result = convert_string_to_term('123*x^56')

        self.assertTrue(expected == result)


    def test_converting_when_there_are_both_coefficient_and_power_but_no_multiply_sign(self):

        expected = Term(123,56)

        result = convert_string_to_term('123x^56')

        self.assertTrue(expected == result)

    def test_converting_when_there_is_only_coefficient_and_power_is_one(self):

        expected = Term(123,1)
        
        result = convert_string_to_term('123*x')
        
        self.assertTrue(expected == result)

    def test_converting_when_there_is_only_power_and_coefficient_is_one(self):

        expected = Term(1,56)

        result = convert_string_to_term('x^56')

        self.assertTrue(expected == result)

    def test_converting_when_there_is_only_constant(self):

        expected = Term(12121,0)

        result = convert_string_to_term('12121')

        self.assertTrue(expected == result)

class TestConvertingListOfTermsInPolynomial(unittest.TestCase):

    def test_converting_of_list_of_terms_in_polynomial(self):

        expected = Polynomial([Term(12,20),Term(123,56),Term(1,782),Term(123,1),Term(1873223,0)])

        result = convert_string_into_polynomial('123*x^56+12*x^20+x^782+123*x+1873223')

        self.assertTrue(expected == result)

class TestFindingTheDerivativeOfAPolynomial(unittest.TestCase):

    def test_when_there_are_only_terms_with_both_coefficient_and_power(self):

        expected = Polynomial([Term(240,19),Term(7820,781),Term(6888,55)])

        result = find_derivative_of_polynomial(Polynomial([Term(12,20),Term(123,56),Term(10,782)]))

        self.assertTrue(expected == result)

    def test_when_there_are_only_terms_with_coefficients_and_power_one(self):

        expected = Polynomial([Term(12,0),Term(123,0),Term(10,0)])

        result = find_derivative_of_polynomial(Polynomial([Term(12,1),Term(123,1),Term(10,1)]))
        print(result)
        self.assertTrue(expected == result)

    def test_when_there_are_only_terms_with_powers_and_coefficient_one(self):

        expected = Polynomial([Term(20,19),Term(782,781),Term(2,1)])

        result = find_derivative_of_polynomial(Polynomial([Term(1,20),Term(1,782),Term(1,2)]))

        self.assertTrue(expected == result)

    def test_when_there_are_only_terms_with_power_zero(self):

        expected = Polynomial([Term(0,0),Term(0,0),Term(0,0)])

        result = find_derivative_of_polynomial(Polynomial([Term(121212,0),Term(11111,0),Term(999,0)]))

        self.assertTrue(expected == result)

    def test_with_a_polynomial_of_random_types_of_terms(self):

        expected = Polynomial([Term(240,19),Term(0,0),Term(782,781),Term(123,0)])

        result = find_derivative_of_polynomial(Polynomial([Term(12,20),Term(123,1),Term(1,782),Term(12211,0)]))

        self.assertTrue(expected == result)


if __name__ == '__main__':
    unittest.main()