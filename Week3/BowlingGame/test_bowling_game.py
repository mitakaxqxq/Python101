import unittest

from frame import Frame
from bowling_game import BowlingGame

class TestValidationOfBowlingGame(unittest.TestCase):

    def test_raises_exception_when_input_is_not_a_list(self):
        exc = None

        try:
            b = BowlingGame((1,2,3,4,5))
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Wrong input - you have to enter list of positive integers')

    def test_raises_exception_when_less_than_ten_tries(self):
        exc = None

        try:
            b = BowlingGame([1,2,3,4,5,6,7,8,1])
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Wrong input - can not have less than 10 tries')

    def test_raises_exception_when_more_than_twenty_tries(self):
        exc = None

        try:
            b = BowlingGame([1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8,1,2,3,4,5,6,7,8])
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Wrong input - can not have more than 20 tries')

    def test_when_a_value_in_the_rolls_is_not_integer(self):

        exc = None

        try:
            b = BowlingGame([1,2,3,'4',5,6,7,8,9,1])        
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Wrong input - you must enter integers for knocked pins')

class TestBowlingGameInitialization(unittest.TestCase):

    def test_passes_with_correct_values_for_bowling_game(self):

        test_frames = [1,2,3,4,5,4,3,2,1,2,8]

        bowling_game = BowlingGame(test_frames)

    def test_initializes_values_of_bowling_game_as_expected(self):

        test_frames = [1,2,3,4,5,4,3,2,1,2,8]

        bowling_game = BowlingGame(test_frames)
        self.assertEqual(getattr(bowling_game,'frames'),[Frame(1,2),Frame(3,4),Frame(5,4),Frame(3,2),Frame(1,2),Frame(8,0)])

class TestBowlingGameScore(unittest.TestCase):
    def test_bowling_game_calculate_score_when_all_frames_are_zero(self): 
        
        bowling_game = BowlingGame([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]) 

        self.assertEqual(bowling_game.calculate_score(), 0)

    def test_bowling_game_calculate_score_when_all_frames_are_open_frames(self):
        
        bowling_game = BowlingGame([1, 4, 4, 5, 6, 3, 5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6, 2])

        self.assertEqual(bowling_game.calculate_score(),65)

    def test_bowling_game_calculate_score_when_all_frames_are_strikes(self):
        
        bowling_game = BowlingGame([10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10])

        self.assertEqual(bowling_game.calculate_score(), 300)

    def test_bowling_game_with_invalid_number_of_frames(self):
        
        bowling_game = BowlingGame([5, 1, 1, 0, 1, 7, 3, 6, 4, 3, 2, 1, 6])

        self.assertEqual(bowling_game.calculate_score(), 'Invalid number of frames.')

    def test_bowling_game_with_spare_in_tenth_frame_preceeded_by_spare(self):

        bowling_game = BowlingGame([1, 6, 7, 2, 3, 4, 5, 5, 6, 2, 1, 6, 7, 2, 3, 4, 5, 5, 6, 4, 5])
        #print(str(bowling_game))
        self.assertEqual(bowling_game.calculate_score(), 101)

    def test_bowling_game_with_strike_and_open_frame_in_tenth_frame(self):

        bowling_game = BowlingGame([1, 6, 7, 2, 3, 4, 5, 5, 6, 2, 1, 6, 7, 2, 3, 4, 5, 5, 10, 4, 5])

        self.assertEqual(bowling_game.calculate_score(), 109)

    def test_bowling_game_with_strikes_and_only_one_open_frame_in_tenth_frame(self):

        bowling_game = BowlingGame([10, 10, 10, 10, 10, 10, 10, 10, 10, 3, 4])

        self.assertEqual(bowling_game.calculate_score(), 257)

    def test_bowling_game_with_open_frame_in_tenth_frame_preceeded_by_strike(self):

        bowling_game = BowlingGame([10,10,10,10,10,10,10,10,5,5,10,5,4])

        self.assertEqual(bowling_game.calculate_score(), 264)

    def test_bowling_game_with_strike_in_tenth_frame_preceeded_by_spare(self):

        bowling_game = BowlingGame([6,4,4,4,4,4,4,4,10,10,10,5,5,10,9,1,10])

        self.assertEqual(bowling_game.calculate_score(), 173)

    def test_bowling_game_with_open_frame_in_tenth_frame_preceeded_by_spare(self):

        bowling_game = BowlingGame([10,10,10,10,10,10,10,10,5,5,4,6,5])

        self.assertEqual(bowling_game.calculate_score(), 254)

    def test_bowling_game_with_three_strikes_in_tenth_frame(self):

        bowling_game = BowlingGame([10,10,10,10,10,10,10,5,5,6,4,10,10,10])

        self.assertEqual(bowling_game.calculate_score(),261)


if __name__ == '__main__':
    unittest.main()