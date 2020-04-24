from contextlib import contextmanager
from decimal import getcontext, Decimal


@contextmanager
def change_precision(precision):
    try:
        getcontext().prec = precision
        yield
    except Exception as err:
        raise err
    finally:
        getcontext().prec = 28


with change_precision(2):
    print(Decimal('1.123132132') + Decimal('2.23232'))  # 3.4

print(Decimal('1.123132132') + Decimal('2.23232'))  # 3.355452132


class changePrecision:

    def __init__(self, precision):
        if type(precision) is not int:
            raise TypeError('You must assign integer!')
        elif precision < 0:
            raise ValueError('Integer must be positive!')
        self.precision = precision

    def __enter__(self):
        getcontext().prec = self.precision
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        getcontext().prec = 28


with changePrecision(2):
    print(Decimal('1.123132132') + Decimal('2.23232'))  # 3.4

print(Decimal('1.123132132') + Decimal('2.23232'))  # 3.355452132