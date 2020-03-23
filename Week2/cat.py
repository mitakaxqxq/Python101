import sys

def cat(arguments):
    with open(arguments,"r") as f:
       content = f.read()
       print(content)
    f.close()


def main():
    cat("file.txt")

if __name__ == '__main__':
    main()