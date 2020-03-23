def sum_of_digits(n):
    s = 0
    if n < 0:
      n=-n
    while n != 0:
       s+=n%10
       n=n//10
    return s

"""
print(sum_of_digits(1325132435356))
print(sum_of_digits(123))
print(sum_of_digits(6))
print(sum_of_digits(-10))
"""

def to_digits(n):
    res=[int(d) for d in str(n)]
    return res
"""
print(to_digits(123))
print(to_digits(99999))
print(to_digits(123023))
"""

def to_number(digits):
	res = "".join([str(i) for i in digits])
	return int(res)

"""
to_number([1,2,3])
to_number([9,9,9,9,9])
to_number([1,2,3,0,2,3])
to_number([21,2,33])
"""
def fact(n):
   s=1
   while n != 1:
      s=s*n
      n=n-1
   return s

def fact_digits(n):
	s = 0
	while n != 0:
		s+=fact(n%10)
		n=n//10
	return s

"""
print(fact_digits(111))
print(fact_digits(145))
print(fact_digits(999))
"""

def palindrome(n):
    newstr = str(n)[::-1]
    if newstr == str(n):
        return True
    else:
        return False

"""
print(palindrome(121))
print(palindrome("kapak"))
print(palindrome("baba"))
"""

def count_vowels(str):
    s = 0
    for i in str:
      s+=check_is_vowel(i)
    return s

"""
print(count_vowels("Python"))
print(count_vowels("Theistareykjarbunga")) #It's a volcano name!
print(count_vowels("grrrrgh!"))
print(count_vowels("Github is the second best thing that happend to programmers, after the keyboard!"))
print(count_vowels("A nice day to code!"))
"""

def check_is_symbol(a):
	return a in ['.',',','!','?',':',';',' ']

def check_is_vowel(a):
    return a in ['a','e','i','o','u','y','A','E','I','O','U','Y']

def count_consonants(str):
   s = 0
   for i in str:
     s+=not(check_is_vowel(i)+check_is_symbol(i))
   return s

"""
print(count_consonants("Python"))
print(count_consonants("Theistareykjarbunga")) #It's a volcano name!
print(count_consonants("grrrrgh!"))
print(count_consonants("Github is the second best thing that happend to programmers, after the keyboard!"))
print(count_consonants("A nice day to code!"))

"""

def char_histogram(string):
   dictionary = {}
   for a in string:
      if a in dictionary:
        dictionary[a] += 1
      else:
        dictionary[a] = 1
   return dictionary

"""
print(char_histogram("Python!"))
print(char_histogram("AAAAaaa!!!"))
"""

def sum_matrix(m):
   s = 0
   for mas in m:
      for elem in mas:
         s=s+elem
   return s

"""
m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(sum_matrix(m))
m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
print(sum_matrix(m))
m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
print(sum_matrix(m))

"""

def nan_expand(times):
    beg = times
    while times > 0:
       print("Not a ",end="")
       times=times-1
    if beg == 0:
       print("")
    else:
       print("NaN")

"""
nan_expand(0)
nan_expand(1)
nan_expand(2)
nan_expand(3)
"""

def prime_factorization(n):
   mylist=[]
   i = 2
   while i <= n:
      counter = 0
      if n % i == 0:
        while n % i == 0:
           counter+=1
           n//=i
      if counter > 0:
        mytuple=(i,counter)
        mylist.append(mytuple)
      i+=1
   return mylist
"""
print(prime_factorization(10))
print(prime_factorization(14))
print(prime_factorization(356))
print(prime_factorization(89))
print(prime_factorization(1000))
"""

def group(list):
   listOfLists =[]
   helperList = []
   for elem in list:
      if not helperList:
         helperList.append(elem)
      else:
         if elem in helperList:
            helperList.append(elem)
         else:
            listOfLists.append(helperList)
            helperList = [elem]
   listOfLists.append(helperList)
   return listOfLists

"""
print(group([1, 1, 1, 2, 3, 1, 2]))
print(group([1, 2, 1, 2, 3, 3]))
"""

def max_consecutive(items):
   newList = [len(i) for i in group(items)]
   return max(newList)

"""
print(max_consecutive([1, 2, 3, 3, 3, 3, 4, 3, 3]))
print(max_consecutive([1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 5]))
"""

def contains_word(word,text):
   return text.count(word) + text[::-1].count(word)


def word_counter():
    word = input()
    size = input()
    n , m = [int(x) for x in size.split(' ')]
    print(n,m)
    if len(word) > min(n,m):
       return "Invalid number of rows or columns!"
    matrix = []
    rows_inputted = 0
    print("Enter matrix: ")
    while rows_inputted < n:
       row_input = input()
       row = row_input.strip().split(' ')
       if len(row) != m:
          return "Wrong input!"
       matrix.append(row)
       rows_inputted+=1

    word_occurances = 0
    for row in matrix:
           word_occurances+=contains_word(word,row)

    for i in range(m):
       column = []
       for row in matrix:
          column.append(row[i])
       word_occurances+=contains_word(word,column)
    return word_occurances

print(word_counter())

'''alternativa na vhoda
n = int(size.split(' ')[0])
m = int(size.split(' ')[1])'''