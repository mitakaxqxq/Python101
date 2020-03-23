import unittest

from song import Song

class TestValidationOfSongArguments(unittest.TestCase):

    def test_when_one_value_is_of_wrong_instance(self):

        exc = None

        try:
            song = Song([12,2,8],"Manowar","The Sons of Odin","3:44")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'All values must be strings!')

    def test_when_more_than_one_value_are_of_wrong_instance(self):

        exc = None

        try:
            song = Song("Odin",[12,2,8],121212,"3:44")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'All values must be strings!')

    def test_when_one_value_is_the_empty_string(self):

        exc = None

        try:
            song = Song("Odin","","The Sons of Odin","3:44")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'None of the values can be the empty string!')

    def test_when_more_than_one_value_are_the_empty_string(self):

        exc = None

        try:
            song = Song("Odin","","The Sons of Odin","")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'None of the values can be the empty string!')

    def test_when_length_is_given_as_a_single_digit(self):

        exc = None

        try:
            song = Song("Odin","Manowar","The Sons of Odin","3")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect length of song - it can not be a single digit!')

    def test_when_length_is_given_as_a_single_digit_with_a_double_dots(self):

        exc = None

        try:
            song = Song("Odin","Manowar","The Sons of Odin","3:")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect input - you have entered a wrong length!')

    def test_when_length_has_two_double_dots_next_to_each_other(self):

        exc = None

        try:
            song = Song("Odin","Manowar","The Sons of Odin","3::44")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect input - you have entered a wrong length!')

    def test_when_there_is_a_wrong_symbol_in_length(self):

        exc = None

        try:
            song = Song("Odin","Manowar","The Sons of Odin","3:4^")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect input - you have entered an unrecognizable symbol in the length!')

    def test_when_there_are_more_numbers_than_needed(self):

        exc = None
        
        try:
            song = Song("Odin","Manowar","The Sons of Odin","1:3:4:4")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect input - you have entered more numbers than just hours, minutes and seconds!')


    def test_when_hours_are_present_in_length_and_minutes_less_than_ten_are_given_as_one_digit(self):

        exc = None
        
        try:
            song = Song("Odin","Manowar","The Sons of Odin","1:3:44")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect input - you have entered an hour but minutes less than ten as a single digit!')

    def test_when_minutes_value_exceeds_maximum_value_with_length_of_hours_minutes_and_seconds(self):

        exc = None
        
        try:
            song = Song("Odin","Manowar","The Sons of Odin","6:67:44")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect input - minutes value is bigger than maximum possible')


    def test_when_seconds_value_exceeds_maximum_value_with_length_of_hours_minutes_and_seconds(self):

        exc = None
        
        try:
            song = Song("Odin","Manowar","The Sons of Odin","6:47:64")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect input - seconds value is bigger than maximum possible')

    def test_when_minutes_value_exceeds_maximum_value_with_length_of_minutes_and_seconds(self):

        exc = None
        
        try:
            song = Song("Odin","Manowar","The Sons of Odin","67:24")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect input - minutes value is bigger than maximum possible')

    def test_when_seconds_value_exceeds_maximum_value_with_length_of_minutes_and_seconds(self):

        exc = None
        
        try:
            song = Song("Odin","Manowar","The Sons of Odin","47:64")
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Incorrect input - seconds value is bigger than maximum possible')

class TestSongMethods(unittest.TestCase):

    def test_if_song_to_string_is_represented_in_right_way(self):

        song = Song("Odin","Manowar","The Sons of Odin","3:44")
        
        string = "Manowar - Odin from The Sons of Odin - 3:44"

        self.assertTrue(str(song) == string,'Strings are equal')


    def test_when_two_songs_are_equal(self):

        song1 = Song("Odin","Manowar","The Sons of Odin","3:44")
        song2 = Song("Odin","Manowar","The Sons of Odin","3:44")

        self.assertTrue(song1 == song2, 'The songs are equal')

    def test_when_a_song_is_added_to_a_dictionary(self):

        song1 = Song("Odin","Manowar","The Sons of Odin","3:44")
        song2 = Song("Odin","Manowar","The Sons of Odin","3:44")

        myDict = {}

        myDict[song1] = 1

        if song2 in myDict:
            myDict[song2] += 1

        self.assertTrue(myDict[song2] == 2, 'Song is hashable')

    def test_when_user_wants_the_length_of_a_song_with_minutes_and_seconds_in_seconds(self):

        song1 = Song("Odin","Manowar","The Sons of Odin","3:44")

        self.assertTrue(224 == song1.length(seconds=True),"Length of song in seconds is right")


    def test_when_user_wants_the_length_of_a_song_with_minutes_and_seconds_in_minutes(self):

        song1 = Song("Odin","Manowar","The Sons of Odin","3:44")

        self.assertTrue(3 == song1.length(minutes=True),"Length of song in minutes is right")


    def test_when_user_wants_the_length_of_a_song_with_minutes_and_seconds_in_hours(self):

        song1 = Song("Odin","Manowar","The Sons of Odin","3:44")

        self.assertTrue(0 == song1.length(hours=True),"Length of song in hours is right")


    def test_when_user_wants_the_length_of_a_song_with_hours_minutes_and_seconds_in_seconds(self):

        song1 = Song("Odin","Manowar","The Sons of Odin","1:03:44")

        self.assertTrue(1664 == song1.length(seconds=True),"Length of song in seconds is right")


    def test_when_user_wants_the_length_of_a_song_with_hours_minutes_and_seconds_in_minutes(self):

        song1 = Song("Odin","Manowar","The Sons of Odin","1:03:44")

        self.assertTrue(63 == song1.length(minutes=True),"Length of song in minutes is right")


    def test_when_user_wants_the_length_of_a_song_with_hours_minutes_and_seconds_in_hours(self):

        song1 = Song("Odin","Manowar","The Sons of Odin","5:03:44")

        self.assertTrue(5 == song1.length(hours=True),"Length of song in hours is right")

    def test_when_user_call_length_method_without_any_attributes(self):

        song1 = Song("Odin","Manowar","The Sons of Odin","5:03:44")

        self.assertTrue("5:03:44" == song1.length(),"String representation of song is right")


if __name__ == '__main__':
    unittest.main()