import unittest
from booking_status import Booking, get_booking_status
from unittest.mock import patch
import datetime


class TestGetBookingStatus(unittest.TestCase):
    @patch('booking_status.datetime')
    def test_booking_is_cancelled(self, datetime_mock):
        datetime_mock.now.return_value = datetime.datetime(year=2020, month=4, day=22)
        b = Booking(datetime.datetime(year=2020, month=4, day=26), True, True)
        self.assertEqual('Cancelled', get_booking_status(b))

    @patch('booking_status.datetime')
    def test_booking_is_fully_paid(self, datetime_mock):
        datetime_mock.now.return_value = datetime.datetime(year=2020, month=4, day=22)
        b = Booking(datetime.datetime(year=2020, month=4, day=26), False, True)
        self.assertEqual('Paid', get_booking_status(b))

    @patch('booking_status.Booking.is_fully_paid')  # to make sure the method is_fully_paid has passed
    @patch('booking_status.datetime')
    def test_booking_is_upcoming_and_is_not_fully_paid(self, datetime_mock, fully_paid_mock):
        datetime_mock.now.return_value = datetime.datetime(year=2020, month=4, day=22)
        fully_paid_mock.return_value = False
        b = Booking(datetime.datetime(year=2020, month=4, day=26), False, False)
        self.assertEqual('Upcoming', get_booking_status(b))

    @patch('booking_status.datetime')
    def test_booking_is_waiting_taxes(self, datetime_mock):
        datetime_mock.now.return_value = datetime.datetime(year=2020, month=4, day=22)
        b = Booking(datetime.datetime(year=2020, month=4, day=20), False, False)
        self.assertEqual('Waiting taxes', get_booking_status(b))


if __name__ == '__main__':
    unittest.main()
