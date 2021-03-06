import unittest
from cancellation_policy import validate_conditions,ensure_conditions


class TestValidateConditions(unittest.TestCase):
    def test_validation_passes_with_valid_conditions(self):
        conditions = [
            {'hours': 10, 'percent': 10},
            {'percent': 100}
        ]

        validate_conditions(conditions)

    def test_raises_exception_if_all_conditions_have_hours(self):
        conditions = [
            {'hours': 10, 'percent': 10}
        ]
        exc = None

        # ACT
        try:
            validate_conditions(conditions)
        except Exception as err:
            exc = err

        # ASSERTS
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Invalid conditions.')

    def test_raises_exception_if_more_than_one_condition_with_no_hours(self):
        conditions = [
            {'hours': 10, 'percent': 10000},
            {'percent': 10},
            {'percent': 100}
        ]
        exc = None

        # ACT
        try:
            validate_conditions(conditions)
        except Exception as err:
            exc = err

        # ASSERTS
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Invalid conditions.')

    def test_raises_exception_if_hours_bigger_than_24(self):
        # ARRANGE
        conditions = [
            {'hours': 72, 'percent': 10000},
            {'percent': 10},
        ]
        exc = None

        # ACT
        try:
            validate_conditions(conditions)
        except Exception as err:
            exc = err

        # ASSERTS
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc), 'Hours cannot be > 24.')

class TestEnsureConditions(unittest.TestCase):
    def test_raises_exception_if_there_is_still_key_null(self):
        #now we ARRANGE
        conditions = [
            {'hours': 10, 'percent': 10},
            {'percent': 10},
            {'percent': 10}
        ]
        exc = None

        #now we ACT
        try:
            ensure_conditions(conditions)
        except Exception as err:
            exc = err

        #and finally we ASSERT
        self.assertIsNotNone(exc)
        self.assertEqual(str(exc),'There is key which is still null.')

class TestGroupConditions(unittest.TestCase):
    def test_group_conditions_with_two_elements(self):
        

if __name__ == '__main__':
    unittest.main()