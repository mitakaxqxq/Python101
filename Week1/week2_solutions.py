def closest_to_gas_station(travelled_distance,stations):
   prev = stations[0]
   for i in stations:
      if i >= travelled_distance:
         return prev
      else:
         prev = i
   return prev

   

def gas_stations(distance, tank_size, stations):
   listOfStationsToStop = []
   helperTankSize = tank_size
   while helperTankSize - tank_size <= distance:
      listOfStationsToStop.append(closest_to_gas_station(helperTankSize,stations))
      helperTankSize += tank_size
   return listOfStationsToStop
'''
print(gas_stations(320, 90, [50, 80, 140, 180, 220, 290]))
print(gas_stations(390, 80, [70, 90, 140, 210, 240, 280, 350]))
'''

def to_digits(n):
    res=[int(d) for d in str(n)]
    return res

def is_number_balanced(number):
   numberToList = to_digits(number)
   length = len(numberToList)
   if length == 1:
      return True
   left = length // 2
   if left % 2 == 0:
    right = length // 2
   else:
    right = length // 2 + 1
   print(left)
   print(right)
   sum1 = 0
   sum2 = 0
   for i in range(left):
      sum1 += numberToList[i]
   for i in range(length-right):
      sum2 += numberToList[i]
   if sum1 == sum2:
      return True
   return False
'''
print(is_number_balanced(9))
print(is_number_balanced(4518))
print(is_number_balanced(28471))
print(is_number_balanced(1238033))
'''
def increasing_or_decreasing(seq):
   increasing = all(x<y for x,y in zip(seq,seq[1:]))
   decreasing = all(x>y for x,y in zip(seq,seq[1:]))
   if increasing == True:
      if decreasing == False:
         return 'Up!'
      else:
         return 'False'
   else:
      if decreasing == True:
         return 'Down!'
      else:
         return 'False'
'''
print(increasing_or_decreasing([1,2,3,4,5]))
print(increasing_or_decreasing([5,6,-10]))
print(increasing_or_decreasing([1,1,1,1]))
print(increasing_or_decreasing([9,8,7,6]))
'''
def get_length_of_number(n):
   count = 0
   while n != 0:
      count+=1
      n = n // 10
   return count

def get_first_digit_of_number(n):
   length = get_length_of_number(n)
   i = 0
   while i < length-1:
      i+=1
      n = n // 10
   return n

def get_largest_palindrome(n):
   listOfPalindromes = []
   lengthOfNumber = get_length_of_number(n)
   firstDigitOfNumber = get_first_digit_of_number(n)-1
   x=pow(10,lengthOfNumber-1)
   for i in range(firstDigitOfNumber*x,n-1):
      if str(i) == str(i)[::-1]:
         listOfPalindromes.append(i)
   return max(listOfPalindromes)
'''
print(get_largest_palindrome(99))
print(get_largest_palindrome(252))
print(get_largest_palindrome(994687))
print(get_largest_palindrome(754649))'''

def sum_of_numbers(input_string):
   listOfNumbers = []
   num = 0
   for x in list(input_string):
      if x.isdigit():
         num = num*10+int(x)
      else:
         listOfNumbers.append(num)
         num = 0
   return sum(listOfNumbers)+num
'''
print(sum_of_numbers("ab125cd3"))
print(sum_of_numbers("ab12"))
print(sum_of_numbers("ab"))
print(sum_of_numbers("1101"))
print(sum_of_numbers("1111O"))
print(sum_of_numbers("1abc33xyz22"))
print(sum_of_numbers("0hfabnek"))
'''

def birthday_ranges(birthdays, ranges):
   myDict = {}
   birthdays.sort()
   for i in birthdays:
      if i in myDict.keys():
         myDict[i]+=1
      else:
         myDict[i]=1
   print(myDict)

   listOfPeopleBorn = []

   for elem in ranges:
      sum = 0
      for i in range(elem[0],elem[1]+1):
         if i in myDict.keys():
            sum += myDict[i]
      listOfPeopleBorn.append(sum)
   return listOfPeopleBorn
'''
print(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))
print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (2,301), (8,301), (200, 225), (300, 365)]))
'''
def myGroup(myList):
   index = 0
   length = len(myList)
   groups = []
   curr = []
   for elem in range(0,length):
      if myList[elem] in curr:
         curr.append(myList[elem])
      elif len(curr) != 0:
         groups.append(curr)
         curr = []
         curr.append(myList[elem])
      elif len(curr) == 0:
         curr.append(myList[elem])
      if elem == length - 1:
         groups.append(curr)
   return groups

def numbers_to_message(pressed_sequence):
   listOfNums = myGroup(list(pressed_sequence))
   message = ''
   helper = ''
   capital = False
   hashmap = { 0:' ', 2:'abc', 3:'def',
                4:'ghi', 5:'jkl', 6:'mno',
                7:'pqrs', 8:'tuv', 9:'wxyz'}

   for elem in listOfNums:
      if elem[0] == 1:
         capital = True
         continue
      if elem[0] == -1:
         continue

      index = len(elem)
      helper = hashmap[elem[0]]

      if index > len(helper):
         index //= len(helper)

      if(not capital):
         message += helper[index-1]
      else:
         helper = helper.upper()
         message += helper[index-1]
         capital = False
   return message

print(numbers_to_message([2, -1, 2, 2, -1, 2, 2, 2]))
print(numbers_to_message([2, 2, 2, 2]))
print(numbers_to_message([1, 4, 4, 4, 8, 8, 8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))