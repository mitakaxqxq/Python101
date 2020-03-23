from simplify_fractions import GCD,simplify_fraction

def LCM(a,b): 
    return (a*b) / GCD(a,b) 

def check_zero_denominator(fractions):
    for elem in fractions:
        if elem[1] == 0:
            return True
    return False

def check_fraction_length_bigger_than_required(fractions):
    for elem in fractions:
        if len(elem) > 2:
            return True
    return False

def check_fraction_length_lower_than_required(fractions):
    for elem in fractions:
        if len(elem) < 2:
            return True
    return False

def validate_values(fractions):
    if not isinstance(fractions,list):
        raise ValueError('Passed fractions are not in the form of a list of tuples')
    elif len(fractions) > 2:
        raise ValueError('More than 2 fractions are being passed for the program to collect')
    elif check_fraction_length_bigger_than_required(fractions):
        raise ValueError('There is a fraction with more than two elements')
    elif check_fraction_length_lower_than_required(fractions):
        raise ValueError('There is a fraction with less than two elements')
    elif check_zero_denominator(fractions):
        raise ValueError('Second element of one of the fractions is zero - cannot divide by zero!!!')

def collect_fractions(fractions):
    firstFraction = simplify_fraction(fractions[0])
    secondFraction = simplify_fraction(fractions[1])

    newDenom = LCM(firstFraction[1],secondFraction[1])

    firstNumerator = newDenom / firstFraction[1]
    secondNumerator = newDenom / secondFraction[1]

    newNumer = firstNumerator + secondNumerator

    return simplify_fraction((int(newNumer),int(newDenom)))


def main():
    print(collect_fractions([(1, 4), (1, 2)]))
    print(collect_fractions([(1, 7), (2, 6)]))

if __name__ == '__main__':
    main()