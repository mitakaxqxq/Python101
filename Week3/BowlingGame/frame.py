class Frame:

    def __init__(self,first_try,second_try):
        self.validate_values(first_try,second_try)

        self.first_try = first_try
        self.second_try = second_try

    def __str__(self):
        if self.first_try == 10:
            return 'Strike'
        elif self.first_try + self.second_try < 10:
            return 'Open Frame'
        elif self.first_try + self.second_try == 10:
            return 'Spare'

    def __repr__(self):
        return f'Frame ({self.first_try},{self.second_try})'

    def __eq__(self,other):
        return self.first_try == other.first_try and self.second_try == other.second_try

    @staticmethod
    def validate_values(first_try,second_try):
        if not isinstance(first_try,int):
            raise TypeError('Invalid type of pins for your first try - it must be integer!')
        if not isinstance(second_try,int):
            raise TypeError('Invalid type of pins for your second try - it must be integer!')
        if first_try < 0 or first_try > 10:
            raise TypeError('Invalid number of pins for your first try - it must be between 0 and 10!')
        if second_try < 0 or second_try > 10:
            raise TypeError('Invalid number of pins for your second try - it must be between 0 and 10!')
        if first_try + second_try > 10:
            raise TypeError('Invalid score - you can not score more than 10 pins in a single frame')
    