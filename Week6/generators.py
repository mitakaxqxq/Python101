from collections import Iterable


def accepts_iterables(*types):
    def inner(func):
        def check_arguments(*argv):
            for i in range(0, len(types)):
                if not isinstance(argv[i], types[i]):
                    raise TypeError('Argument ' + str(i + 1) + ' not of type ' + str(types[i].__name__))
            return func(*argv)
        return check_arguments
    return inner


@accepts_iterables(Iterable, Iterable)
def chain(iterable_one, iterable_two):
    if not isinstance(iterable_one, Iterable):
        raise AttributeError('First object is not iterable!')

    if not isinstance(iterable_two, Iterable):
        raise AttributeError('Second object is not iterable!')
    print(type(iterable_one))
    print(type(iterable_two))
    if type(iterable_two) != type(iterable_one):
        raise ValueError('Objects types must be equal!')

    for elem in iterable_one:
        yield elem

    for elem in iterable_two:
        yield elem


def compress(iterable, mask):
    list_of_values = []

    for i in range(iterable, mask):
        value = (yield iterable[i])

        if mask[i] is True:
            list_of_values.append(value)

    return list_of_values


def main():
    print(list(chain(range(0, 4), range(4, 8))))
    print(list(compress(["Ivo", "Rado", "Panda"], [False, False, True])))
    print(list(chain([1, 2], {1: 2})))

if __name__ == '__main__':
    main()
