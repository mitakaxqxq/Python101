from math import gcd


class Fraction:
    def __init__(self,numerator,denominator):
        if denominator <= 1:
            raise AssertionError('Zero or negative denominator')
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return f'{self.numerator}/{self.denominator}'

    def __repr__(self):
        return f'Fraction {self}'

    def __eq__(self,other):
        return self.numerator / self.denominator == other.numerator / other.denominator

    def simplify(self):
        myGCD=gcd(self.numerator,self.denominator)
        return Fraction(self.numerator // myGCD,self.denominator // myGCD)

    def __add__(self,other):
        return Fraction(self.numerator*other.denominator+self.denominator*other.numerator,self.denominator*other.denominator)

    def __lt__(self,other):
        return self.numerator/self.denominator < other.numerator/other.denominator
