import unittest
from decorators import *


class TestAcceptsDecorator(unittest.TestCase):

    def test_raises_exception_when_accepts_decorator_takes_wrong_argument(self):
        exc = None

        try:
            say_hello(1)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Argument 1 not of type str')

    def test_accepts_decorator_with_one_correct_argument(self):
        expected = "Hello, I am Marto"
        result = say_hello("Marto")

        self.assertEqual(expected, result)

    def test_accepts_decorator_with_two_correct_argument(self):
        expected = None
        result = deposit("Marto", 800)

        self.assertEqual(expected, result)


class TestPerformanceDecorator(unittest.TestCase):

    def test_raises_exception_when_accepts_decorator_takes_wrong_argument(self):
        exc = None

        try:
            performance(1)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Argument 1 not of type str')

    def test_performance_decorator(self):
        expected = "I am done!"
        result = something_heavy()

        self.assertEqual(expected, result)

    def tearDown(self):
        open('log.txt', 'w').close()


class TestSilenceDecorator(unittest.TestCase):
    def test_raises_exception_when_accepts_decorator_takes_wrong_argument(self):
        exc = None

        try:
            silence(1)
        except Exception as err:
            exc = err

        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Argument 1 not of type str')

    def test_silence_decorator_with_correct_argument_of_function(self):
        expected = None
        result = foo(30)

        self.assertEqual(expected, result)

    def test_silence_decorator_with_incorrect_argument_of_function(self):
        expected = ValueError('Omg.')
        result = foo(100)

        self.assertEqual(type(expected), type(result))
        self.assertEqual(expected.args, result.args)

    def tearDown(self):
        open('errors.txt', 'w').close()


if __name__ == '__main__':
    unittest.main()
