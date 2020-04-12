import unittest
from frame import Frame

class TestValidationOfFrame(unittest.TestCase):

    def test_raises_exception_when_first_try_is_not_int(self):

        exc = None

        try:
            frame = Frame((1,),2)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Invalid type of pins for your first try - it must be integer!')

    def test_raises_exception_when_second_try_is_not_int(self):

        exc = None

        try:
            frame = Frame(1,(2,))
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Invalid type of pins for your second try - it must be integer!')

    def test_raises_exception_when_first_try_is_greater_than_ten(self):

        exc = None

        try:
            frame = Frame(11,2)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Invalid number of pins for your first try - it must be between 0 and 10!')


    def test_raises_exception_when_first_try_is_negative(self):
        
        exc = None

        try:
            frame = Frame(-1,2)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Invalid number of pins for your first try - it must be between 0 and 10!')

    def test_raises_exception_when_second_try_is_greater_than_ten(self):

        exc = None

        try:
            frame = Frame(1,11)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Invalid number of pins for your second try - it must be between 0 and 10!')


    def test_raises_exception_when_second_try_is_negative(self):
        
        exc = None

        try:
            frame = Frame(1,-2)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Invalid number of pins for your second try - it must be between 0 and 10!')

    def test_raises_exception_when_two_tries_score_more_than_ten(self):

        exc = None

        try:
            frame = Frame(5,6)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'Invalid score - you can not score more than 10 pins in a single frame')

class TestFrameInitialization(unittest.TestCase):

    def test_frame_initalization_as_expected_when_first_try_is_not_ten(self):
        
        frame = Frame(1,9)

        self.assertEqual(getattr(frame,'first_try'),1)
        self.assertEqual(getattr(frame,'second_try'),9)

    def test_frame_initalization_as_expected_when_first_try_is_ten(self):
        
        frame = Frame(10,0)
        self.assertEqual(getattr(frame,'first_try'),10)
        self.assertEqual(getattr(frame,'second_try'),0)

class TestFrameStrMethod(unittest.TestCase):

    def test_frame_str_method_as_expected_when_frame_is_open(self):
        
        frame = Frame(3,3)

        self.assertEqual(str(frame),'Open Frame')

    def test_frame_str_method_as_expected_when_frame_is_spare(self):
        
        frame = Frame(3,7)

        self.assertEqual(str(frame),'Spare')

    def test_frame_str_method_as_expected_when_frame_is_strike(self):

        frame = Frame(10,0)

        self.assertEqual(str(frame),'Strike')

class TestFrameEqMethod(unittest.TestCase):

    def test_frame_eq_method_as_expected(self):
        
        frame1 = Frame(2,7)
        frame2 = Frame(2,7)

        self.assertTrue(frame1 == frame2, 'Frames are equal')

if __name__ == '__main__':
    unittest.main()