import sys
from random import randint

def generate_numbers(filename, numbers):
    with open(filename,"w") as f:
       for i in range(0,numbers):
          f.write(str(randint(1,1000)))
          f.write(" ")
    f.close()


def main():
    args = sys.argv
    generate_numbers(args[1],int(args[2]))

if __name__ == '__main__':
    main()