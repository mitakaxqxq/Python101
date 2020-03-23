import sys
from cat import cat 

def cat2(arguments):
    for arg in arguments:
       cat(arg)
       print("")

def main():
    args = sys.argv
    cat2(args[1::])

if __name__ == '__main__':
    main()