class Term:
    def __init__(self,coefficient,power):
        if coefficient < 0:
            raise TypeError('Term coefficient cannot be negative number!')
        if power < 0:
            raise TypeError('Term power cannot be negative number!')
        self.coefficient = coefficient
        self.power = power

    def __eq__(self,other):
        return self.coefficient == other.coefficient and self.power == other.power

    def __str__(self):
        if self.power == 0:
            if self.coefficient == 0:
                return f'0'
            else:
                return f'{self.coefficient}'
        if self.coefficient == 1:
            if self.power == 1:
                return f'x'
            else:
                return f'x^{self.power}'
        else:
            if self.power == 1:
                return f'{self.coefficient}*x'
            else:
                return f'{self.coefficient}*x^{self.power}'
    def __repr__(self):
        return f'Term {self}'

    def __lt__(self,other):
        return self.power < other.power

class Polynomial:

    def __init__(self,terms):
        self.terms = terms

    def __str__(self):
        string = ''
        reversedList = sorted(self.terms)

        for item in reversedList[::-1]:
            if item == Term(0,0):
                continue
            else:
                string += str(item)
                string += ' + '
        if string == '':
            return '0'
        else:
            return string[:-3]

    def __repr__(self):
        return f'Polynomial {self}'

    def __eq__(self,other):
        selfHelper = self.terms
        otherHelper = other.terms

        for term in selfHelper:
            if term not in otherHelper:
                return False
            else:
                otherHelper.remove(term)
        if otherHelper != []:
            return False
        return True
