def validate_value(fraction):
    if not isinstance(fraction,tuple):
        raise ValueError('Passed fraction is not in the form of a tuple')
    elif len(fraction) > 2:
        raise ValueError('Passed tuple has more than two elements')
    elif len(fraction) < 2:
        raise ValueError('Passed tuple has less than two elements')
    elif fraction[1] == 0:
        raise ValueError('Second element is zero - cannot divide by zero!!!')

def GCD(x,y):
    if(y==0): 
        return x 
    else:
        return GCD(y,x%y) 

def simplify_fraction(fraction):
    x,y = fraction
    result = GCD(x,y)
    x//=result
    y//=result

    newTuple = (x,y)

    return newTuple

def main():
    print(simplify_fraction((1,7)))
    print(simplify_fraction((3,9)))
    print(simplify_fraction((4,10)))
    print(simplify_fraction((462,63)))

if __name__ == '__main__':
    main()