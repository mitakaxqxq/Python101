import sys
import os

def duhs(pathname):
   sum = 0
   allFiles = os.listdir(pathname)
   for arg in allFiles:
      itemPath = os.path.join(pathname,arg)
      if os.path.isfile(itemPath):         
         sum += os.path.getsize(itemPath)
      elif os.path.isdir(itemPath):
         sum += duhs(itemPath)
   return sum

def main():
   print(sys.argv[1],"size is:",round(duhs(sys.argv[1])/(1024*1024*1024),1),"GB")

if __name__ == '__main__':
	main()