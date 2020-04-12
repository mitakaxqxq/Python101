import timeit
import time


def accepts(*types):
    def inner(func):
        def check_arguments(*argv):
            for i in range(0, len(types)):
                if not isinstance(argv[i], types[i]):
                    raise TypeError('Argument ' + str(argv[i]) + ' not of type ' + str(types[i].__name__))
            return func(*argv)
        return check_arguments
    return inner


@accepts(str)
def say_hello(name):
    return "Hello, I am {}".format(name)


@accepts(str, int)
def deposit(name, money):
    print("{} sends {} $!".format(name, money))


@accepts(str)
def performance(file_name):
    def inner(func):
        def write_in_file(*argv):
            with open(file_name, 'a') as file:
                file.write('{} was called and took {} seconds to compete\n'.format(func.__name__, timeit.timeit(func, number=1)))
            return func(*argv)
        return write_in_file
    return inner


@performance('log.txt')
def something_heavy():
    time.sleep(2)
    return "I am done!"


@accepts(str)
def silence(file_name):
    def inner(func):
        def check_for_exceptions(*argv):
            exc = None
            try:
                func(*argv)
            except Exception as err:
                exc = err
            if exc is not None:
                with open(file_name, 'a') as file:
                    file.write('Calling "{}" raised an error - {}'.format(func.__name__, type(exc).__name__))
                    file.write(':{} Provided arguments: {}'.format(exc.args, argv))
            return exc
        return check_for_exceptions
    return inner


@silence('errors.txt')
def foo(x):
    if x > 50:
        raise ValueError('Omg.')
    else:
        return x


def main():
#    something_heavy()
    print(say_hello("Ivan"))
    deposit("Marto", 800)
    foo(100)


if __name__ == '__main__':
    main()
