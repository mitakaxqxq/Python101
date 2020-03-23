import unittest

from bowling_game import BowlingGame

class TestValidationOfBowlingGame(unittest.TestCase):

    def test_when_input_is_not_a_list(self):
        exc = None

        try:
            b = BowlingGame((1,2,3,4,5))
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Wrong input - you have to enter list of positive integers')

    def test_when_a_value_in_the_rolls_is_not_integer(self):

        exc = None

        try:
            b = BowlingGame([1,2,3,'4'])        
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Wrong input - a value in the list is not integer')

    def test_when_a_value_in_the_rolls_is_negative_integer(self):

        exc = None

        try:
            b = BowlingGame([1,2,3,-4,5])
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Wrong value - a value in the list is negative - all values must be positive integers')

    def test_when_a_value_in_the_rolls_is_greater_than_ten(self):

        exc = None

        try:
            b = BowlingGame([1,12,3,4,5])
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Wrong value - all values must be positive integers not greater than 10')

class TestCalculationOfScoreOfBowlingGame(unittest.TestCase):

    def test_when_all_rolls_are_zero(self):
        game = BowlingGame([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] )
        expected = 0

        self.assertTrue(game.calculateScore() == expected, 'Scores are equal')

    def test_when_all_rolls_are_one(self):
        game = BowlingGame([1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1] )
        expected = 20

        self.assertTrue(game.calculateScore() == expected, 'Scores are equal')

    def test_when_we_have_one_spare(self):
        game = BowlingGame([5, 5, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] )
        expected = 16

        self.assertTrue(game.calculateScore() == expected, 'Scores are equal')

    def test_when_we_have_all_spares(self):
        i = 0
        game = BowlingGame([5 for i in range(21)])
        expected = 150

        self.assertTrue(game.calculateScore() == expected, 'Scores are equal')

    def test_when_we_have_open_frame(self):

        game = BowlingGame([5, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] )
        expected = 8

        self.assertTrue(game.calculateScore() == expected, 'Scores are equal')

    def test_when_we_have_one_strike(self):
        game = BowlingGame([10, 7, 8, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] )
        expected = 40

        self.assertTrue(game.calculateScore() == expected, 'Scores are equal')

    def test_when_we_have_perfect_score(self):
        game = BowlingGame([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])
        expected = 300

        self.assertTrue(game.calculateScore() == expected, 'Scores are equal')

    def test_one_random_game(self):
        game = BowlingGame([1, 4, 4, 5, 6, 3, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2])
        expected = 65

        self.assertTrue(game.calculateScore() == expected, 'Scores are equal')
        
if __name__ == '__main__':
    unittest.main()