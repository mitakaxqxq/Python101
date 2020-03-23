def check_is_anagram():
   firstInput, secondInput = input().split(' ')
   firstArray = list(firstInput.lower())
   secondArray = list(secondInput.lower())
   for elem in firstArray:
      if elem not in secondArray:
          return 'NOT_ANAGRAMS'
      else:
         secondArray.remove(elem)
   if secondArray != []:
      return 'NOT_ANAGRAMS'
   return 'ANAGRAMS'
'''
print(check_is_anagram())
'''

def to_digits(n):
    res=[int(d) for d in str(n)]
    return res

def sum_of_digits(n):
    s = 0
    if n < 0:
      n=-n
    while n != 0:
       s+=n%10
       n=n//10
    return s

def is_credit_card_valid(number):
   listOfDigits=to_digits(number)
   oddIndexesNumbers = []
   evenIndexesNumbers = []
   for i in range(0,len(listOfDigits)):
      if i % 2 == 0:
         evenIndexesNumbers.append(listOfDigits[i])
      else:
         oddIndexesNumbers.append(listOfDigits[i])

   oddIndexesNumbers = [sum_of_digits(d*2) for d in oddIndexesNumbers]

   sumOfEven = sum(evenIndexesNumbers)
   sumOfOdd = sum(oddIndexesNumbers)

   if (sumOfEven+sumOfOdd) % 10 == 0:
      return 'valid'
   else:
      return 'invalid'
'''
print(is_credit_card_valid(79927398713))
print(is_credit_card_valid(79927398715))
'''

def is_prime(n):
   i = 2
   if n == 0 or n == 1:
      return False
   while i*i<=n:
      if n % i == 0:
         return False
      else:
         i+=1
   return True


def goldbach(n):
   i = 2
   listOfTuples = []
   while i <= n/2:
      remainder = n - i
      if is_prime(i) and is_prime(remainder):
         listOfTuples.append((i,remainder))
      i += 1
   return listOfTuples

'''
print(goldbach(4))
print(goldbach(6))
print(goldbach(8))
print(goldbach(10))
print(goldbach(100))
'''
def checkCoords(col,row,n,m):
   return (col >= 0 and row >= 0) and (col <= n-1 and row <= m-1)

def matrix_bombing_plan(m):
   sumOfAllElements = 0
   for i in range(len(m)):
      for j in range(len(m[0])):
         sumOfAllElements += m[i][j]

   myDict = {}
   remainingSum = sumOfAllElements

   for i in range(len(m)):
      for j in range(len(m[0])):
         if checkCoords(i-1,j-1,len(m),len(m[0])):
            if m[i-1][j-1] - m[i][j] >= 0:
               remainingSum -= m[i][j]
            else:
               remainingSum -= m[i-1][j-1]

         if checkCoords(i-1,j+1,len(m),len(m[0])):
            if m[i-1][j+1] - m[i][j] >= 0:
               remainingSum -= m[i][j]
            else:
               remainingSum -= m[i-1][j+1]

         if checkCoords(i+1,j-1,len(m),len(m[0])):
            if m[i+1][j-1] - m[i][j] >= 0:
               remainingSum -= m[i][j]
            else:
               remainingSum -= m[i+1][j-1]

         if checkCoords(i+1,j+1,len(m),len(m[0])):
            if m[i+1][j+1] - m[i][j] >= 0:
               remainingSum -= m[i][j]
            else:
               remainingSum -= m[i+1][j+1]

         if checkCoords(i,j-1,len(m),len(m[0])):
            if m[i][j-1] - m[i][j] >= 0:
               remainingSum -= m[i][j]
            else:
               remainingSum -= m[i][j-1]

         if checkCoords(i,j+1,len(m),len(m[0])):
            if m[i][j+1] - m[i][j] >= 0:
               remainingSum -= m[i][j]
            else:
               remainingSum -= m[i][j+1]

         if checkCoords(i-1,j,len(m),len(m[0])):
            if m[i-1][j] - m[i][j]  >= 0:
               remainingSum -= m[i][j]
            else:
               remainingSum -= m[i-1][j]

         if checkCoords(i+1,j,len(m),len(m[0])):
            if  m[i+1][j] - m[i][j]  >= 0:
               remainingSum -= m[i][j]
            else:
               remainingSum -= m[i+1][j]

         print(remainingSum)
         myDict[(i,j)] = remainingSum
         remainingSum = sumOfAllElements
   
   return myDict

m = [[1,2,3],[4,5,6],[7,8,9]]
print(matrix_bombing_plan(m))

