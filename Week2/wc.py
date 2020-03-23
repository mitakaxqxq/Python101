import sys
import os

def wc(filename,type):
    if type != 'chars' and type != 'words' and type!='lines':
       print('Invalid input!')
       return
    else:
       lineCounter = 0
       wordCounter = 0
       charCounter = 0
       singleLineCounter = 0
       with open(filename,"r") as f:
          for line in f:
             lineCounter += 1
             wordCounter += len(line.split(' '))
             charCounter += len(line)
             if line == '\n':
                singleLineCounter +=1
          if type == 'words':
             return wordCounter - singleLineCounter
          elif type == 'lines':
             return lineCounter
          else:
             return charCounter

def main():
   args = sys.argv
   print(wc(args[2],args[1]))

if __name__ == '__main__':
	main()