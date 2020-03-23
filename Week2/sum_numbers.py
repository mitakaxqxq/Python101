import sys

def sum_numbers(filename):
   with open(filename,"r") as f:
      content = f.read()
      content = [int(d) for d in content.split()]
      return sum(content)
   close(f)

def main():
   args = sys.argv
   print(sum_numbers(args[1]))

if __name__ == '__main__':
	main()