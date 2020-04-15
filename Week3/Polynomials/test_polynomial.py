import unittest

from polynomial import Term, Polynomial

class TestTerm(unittest.TestCase):
    
    def test_term_with_negative_coefficient(self):
        
        exc = None
        try:
            term = Term(-1,1)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Term coefficient cannot be negative number!')

    def test_term_with_negative_power(self):
        
        exc = None
        try:
            term = Term(1,-1)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Term power cannot be negative number!')

    def test_if_term_representation_is_correct_when_coefficient_is_bigger_than_one(self):
        
        term = Term(2,3)
        expected = 'Term 2*x^3'

        self.assertEqual(repr(term),expected)

    def test_if_term_is_correct_when_coefficient_and_power_are_greater_than_one(self):

        term = Term(2,3)

        expected = '2*x^3'

        self.assertTrue(str(term) == expected)
    
    def test_if_term_is_correct_when_coefficient_is_one(self):

        term = Term(1,3)
        expected = 'x^3'

        self.assertTrue(str(term) == expected)

    def test_if_term_is_correct_when_coefficient_and_power_are_one(self):

        term = Term(1,1)
        expected = 'x'

        self.assertTrue(str(term) == expected)

    def test_if_term_is_correct_when_power_is_one(self):

        term = Term(1212,1)
        expected = '1212*x'

        self.assertTrue(str(term) == expected)

    def test_if_term_is_correct_when_it_is_zero(self):

        term = Term(0,0)
        expected = '0'

        self.assertTrue(str(term) == expected)

    def test_if_term_is_correct_when_it_is_constant(self):

        term = Term(123,0)
        expected = '123'

        self.assertTrue(str(term) == expected)

    def test_if_two_terms_are_equal(self):
        
        term1 = Term(2,3)
        term2 = Term(2,3)

        self.assertTrue(term1 == term2)


class TestPolynomial(unittest.TestCase):

    def test_if_two_polynomials_are_equal_when_they_have_equal_number_of_terms_in_different_order(self):

        polynomial1 = Polynomial([Term(1,20),Term(1,2),Term(10,2)])
        polynomial2 = Polynomial([Term(1,2),Term(10,2),Term(1,20)])

        self.assertTrue(polynomial1 == polynomial2)

    def test_if_two_polynomials_are_equal_when_they_have_different_number_of_terms(self):

        polynomial1 = Polynomial([Term(1,20),Term(1,2),Term(10,2)])
        polynomial2 = Polynomial([Term(1,2),Term(10,2),Term(1,20),Term(10,2)])

        self.assertFalse(polynomial1 == polynomial2)

    def test_if_two_polynomials_are_different(self):

        polynomial1 = Polynomial([Term(1,20),Term(3,5)])
        polynomial2 = Polynomial([Term(4,6),Term(7,8)])

        self.assertFalse(polynomial1 == polynomial2)

    def test_if_polynomial_is_sorted_in_descending_order(self):

        expected = Polynomial([Term(1,20),Term(7,8),Term(4,6),Term(3,5)])

        result = Polynomial(sorted([Term(4,6),Term(1,20),Term(3,5),Term(7,8)]))

        self.assertTrue(result == expected)

class TestFindingDerivativeOfPolynomial(unittest.TestCase):
    def test_when_there_are_only_terms_with_both_coefficient_and_power(self):

        expected = Polynomial([Term(240,19),Term(7820,781),Term(6888,55)])

        test_polynomial = Polynomial([Term(12,20),Term(123,56),Term(10,782)])
        result = test_polynomial.derivative()
        self.assertTrue(str(expected) == result)

    def test_when_there_are_only_terms_with_coefficients_and_power_one(self):

        expected = Polynomial([Term(12,0),Term(123,0),Term(10,0)])

        test_polynomial = Polynomial([Term(12,1),Term(123,1),Term(10,1)])
        result = test_polynomial.derivative()
        self.assertTrue(str(expected) == result)

    def test_when_there_are_only_terms_with_powers_and_coefficient_one(self):

        expected = Polynomial([Term(20,19),Term(782,781),Term(2,1)])

        test_polynomial = Polynomial([Term(1,20),Term(1,782),Term(1,2)])
        result = test_polynomial.derivative()
        self.assertTrue(str(expected) == result)

    def test_when_there_are_only_terms_with_power_zero(self):

        expected = Polynomial([Term(0,0),Term(0,0),Term(0,0)])

        test_polynomial = Polynomial([Term(121212,0),Term(11111,0),Term(999,0)])
        result = test_polynomial.derivative()
        self.assertTrue(str(expected) == result)

    def test_with_a_polynomial_of_random_types_of_terms(self):

        expected = Polynomial([Term(240,19),Term(0,0),Term(782,781),Term(123,0)])

        test_polynomial = Polynomial([Term(12,20),Term(123,1),Term(1,782),Term(12211,0)])
        result = test_polynomial.derivative()

        self.assertTrue(str(expected) == result)

if __name__ == '__main__':
    unittest.main()