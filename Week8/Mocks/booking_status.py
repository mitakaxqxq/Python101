from datetime import datetime


class Booking:
    def __init__(self, date, cancelled, fully_paid):
        self.start = date
        self.cancelled = cancelled
        self.fully_paid = fully_paid

    def is_fully_paid(self):
        return self.fully_paid


def get_booking_status(booking):
    now = datetime.now()

    if booking.cancelled:
        return 'Cancelled'

    if booking.is_fully_paid():
        return 'Paid'

    if now < booking.start:
        return 'Upcoming'

    return 'Waiting taxes'
