import unittest
from fraction import Fraction

class TestFraction(unittest.TestCase):
    def test_cannot_instantiate_fraction_with_zero_denominator(self):
        exc = None

        try:
            Fraction(1,0)
        except Exception as err:
            exc = err
        self.assertIsNotNone(exc)

    def test_fractions_string_representation_is_as_expected_one(self):
        
        fraction1 = Fraction(1,3)
        fraction2 = Fraction(-1,3)
        fraction3 = Fraction(2,3)

        self.assertEqual(str(fraction1),'1/3')
        self.assertEqual(str(fraction2),'-1/3')
        self.assertEqual(str(fraction3),'2/3')

    def test_simplified_fraction_is_preserved_after_simplification(self):

        fraction1 = Fraction(1,5)
        expected = Fraction(1,5)

        self.assertEqual(fraction1.simplify(),expected)

    def test_simplified_fraction_is_simplified_as_expected(self):

        fraction1 = Fraction(4,10)
        expected = Fraction(2,5)

        self.assertEqual(fraction1.simplify(),expected)

    def test_equalization_if_fractions_when_their_parts_are_equal(self):

        fraction1 = Fraction(1,5)
        fraction2 = Fraction(1,5)

        self.assertTrue(fraction1 == fraction2,'Fractions are equal.')


    def test_equalization_if_fractions_when_their_parts_are_different(self):

        fraction1 = Fraction(1,5)
        fraction2 = Fraction(2,10)

        self.assertTrue(fraction1 == fraction2,'Fractions are equal.')

    def test_collecting_of_fractions_with_non_simplifiable_result(self):

        fraction1 = Fraction(1,7)
        fraction2 = Fraction(2,6)

        expected = Fraction(10,21)
        self.assertEqual(fraction1+fraction2,expected)

    def test_collecting_of_fractions_with_simplifiable_result(self):

        fraction1 = Fraction(1,6)
        fraction2 = Fraction(2,6)

        expected = Fraction(1,2)
        self.assertEqual(fraction1+fraction2,expected)

    def test_sorting_of_fractions_in_ascending_order(self):

        initialFractions = [Fraction(2, 3), Fraction(1, 2), Fraction(5, 6), Fraction(1, 3)]
        expectedFractions = [Fraction(1, 3), Fraction(1, 2), Fraction(2, 3), Fraction(5, 6)]

        result = sorted(initialFractions)

        self.assertEqual(result,expectedFractions)

    def test_sorting_of_fractions_in_descending_order(self):

        initialFractions = [Fraction(2, 3), Fraction(1, 2), Fraction(5, 6), Fraction(1, 3)]
        expectedFractions = [Fraction(5, 6), Fraction(2, 3), Fraction(1, 2), Fraction(1, 3)]

        result = sorted(initialFractions)[::-1]
        self.assertEqual(result,expectedFractions)

if __name__ == '__main__':
    unittest.main()