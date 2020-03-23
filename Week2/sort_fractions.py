from collect_fractions import LCM


def validate_values(iterable,ascending):
    if not isinstance(iterable,list):
        raise ValueError('First argument is not list')
    if not isinstance(iterable,bool):
        raise ValueError('Second argument is not boolean')


def sort_fractions(iterable,ascending=True):
    if ascending:
        n = len(iterable)
 
        for i in range(n):
            for j in range(0, n-i-1):
                myLCM = LCM(iterable[j][1],iterable[j+1][1])
                firstNumerator = (myLCM/iterable[j][1])*iterable[j][0]
                secondNumerator = (myLCM/iterable[j+1][1])*iterable[j+1][0]

                if firstNumerator > secondNumerator :
                    iterable[j], iterable[j+1] = iterable[j+1], iterable[j]

    elif not ascending:
        n = len(iterable)
 
        for i in range(n):
            for j in range(0, n-i-1):
                myLCM = LCM(iterable[j][1],iterable[j+1][1])
                firstNumerator = (myLCM/iterable[j][1])*iterable[j][0]
                secondNumerator = (myLCM/iterable[j+1][1])*iterable[j+1][0]

                if firstNumerator <= secondNumerator :
                    iterable[j], iterable[j+1] = iterable[j+1], iterable[j]
    return iterable

def main():
    print(sort_fractions([(2, 3), (1, 2)]))
    print(sort_fractions([(2, 3), (1, 2), (1, 3)]))
    print(sort_fractions([(5, 6), (22, 78), (22, 7), (7, 8), (9, 6), (15, 32)]))

if __name__ == '__main__':
    main()