from polynomial import Term,Polynomial

def validate_values(string):
    if not isinstance(string,str):
        raise TypeError('Input has to be string!')

    if '-' in list(string):
        raise TypeError('Wrong input - all coefficients and powers must be positive integers')

    if '/' in list(string):
        raise TypeError('Wrong input - you can not have fractions for coefficients in the polynomial')

    quickCheckList = list(string)

    for element in quickCheckList:
        if element not in ['0','1','2','3','4','5','6','7','8','9','+','*','^','x']:
            raise TypeError('Wrong input - you have entered a symbol which is unrecognizable in the polynomial')

    prev = quickCheckList[0]
    for i in range(1,len(quickCheckList)):
        if quickCheckList[i] == '*' and prev == 'x':
            raise TypeError('Coefficient must be multiplied before the value x')

        if prev == '^' and quickCheckList[i] =='x':
            raise TypeError('Wrong input - variable is after a power sign')

        if (quickCheckList[i] == '+' and prev == '+') or (quickCheckList[i] == '*' and prev == '*') or (quickCheckList[i] == '^' and prev == '^'):
            raise TypeError('Incorrect string - you have misspelled a sign in the string')
        prev = quickCheckList[i]

    if '*' in quickCheckList and '^' in quickCheckList and 'x' not in quickCheckList:
        raise TypeError('Wrong input - calcualtion signs in input string but no variable')


def break_down_into_list_of_strings(string):

    listOfTerms = []
    n = len(string)
    
    helpingString = ''

    i = 0

    while i <= n:
        while string[i] != '+':
            helpingString += string[i]
            i += 1
            if i>= n:
                break
        listOfTerms.append(helpingString)
        helpingString = ''
        i += 1
        if i>= n:
            break
    return listOfTerms

def convert_string_to_term(string):

    flagForX = False

    for i in range(0,len(string)):
        if string[i] == 'x':
            flagForX = True

    listOfCoefficientAndPower = string.split('x')

    if len(listOfCoefficientAndPower) == 1:
        listOfCoefficientAndPower.append('')

    myCoefficient = listOfCoefficientAndPower[0]
    myPower = listOfCoefficientAndPower[1]

    if myCoefficient != '':    
        if myCoefficient[-1:] == '*':
            myCoefficient = myCoefficient[:-1]
    else:
        if flagForX == True:
            myCoefficient = 1
        else:
            myCoefficient = 0
    
    if myPower != '':
        if myPower[0] == '^':
            myPower = myPower[1:]
    else:
        if flagForX == True:
            myPower = 1
        else:
            myPower = 0

    print(myCoefficient)
    print(myPower)
    
    return Term(int(myCoefficient),int(myPower))

def convert_string_into_polynomial(string):
    validate_values(string)    
    listOfStrings = break_down_into_list_of_strings(string)
    listOfTerms = []
    for elem in listOfStrings:
        listOfTerms.append(convert_string_to_term(elem))
    myPolynomial = Polynomial(listOfTerms)
    return myPolynomial

def find_derivative_of_polynomial(polynomial):

    oldListOfTerms = polynomial.terms
    newListOfTerms = []
    
    for term in oldListOfTerms:
        newCoefficient = term.coefficient * term.power
        newPower = term.power - 1
        if newPower < 0:
            newListOfTerms.append(Term(0,0))
        else:
            newListOfTerms.append(Term(newCoefficient,newPower))

    newListOfTerms = [elem for elem in newListOfTerms if elem.power >= 0]

    return Polynomial(newListOfTerms)

def main():
    print(convert_string_to_term('123*x'))
    print(convert_string_to_term('x^56'))
    print(convert_string_to_term('123'))
    print(convert_string_to_term('123*x^56'))
    print(convert_string_to_term('3*x^7'))

if __name__ == '__main__':
    main()