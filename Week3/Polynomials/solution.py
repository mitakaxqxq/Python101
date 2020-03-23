import sys
from utils import break_down_into_list_of_strings,convert_string_to_term,convert_string_into_polynomial,find_derivative_of_polynomial

def main():
    args = sys.argv[1]
    
    myPolynomial = convert_string_into_polynomial(args)

    print('The derivative of f(x) = '+args+' is:')

    print('f`(x) = ' + str(find_derivative_of_polynomial(myPolynomial)))


if __name__ == '__main__':
    main()