'''base functions to practice string operations'''
'''Most of them are solution to CodingBat problems from https://codingbat.com/python'''

# Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
def pos_neg(a, b, negative):
  if(negative):
    return (a < 0 and b < 0)
  else:
    return ((a < 0 and b >0) or (b < 0 and a >0))

# Given a non-empty string and an int n, return a new string where the char at index n has been removed. \n The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
def missing_char(str, n):
    return (str[0:n] + str[n+1:len(str)])

# Given a string, return a new string where the first and last chars have been exchanged.
def front_back(str):
    if(len(str) <= 1):
        return str
    else:
        new_str = str[len(str)-1] + str[1:len(str)-1] + str[0]
    return new_str

# Just spelling words backwards
def spell_backwards(str):
    return str[::-1]

# Given a string, return a new string made of every other char starting with the first, so "Hello" yields "Hlo".
def string_bits(str):
  if(len(str) <= 1):
    return str
  else:
    new_str = str[0]
    for i in range(1,len(str)):
      if(i%2 == 0):
        new_str+=str[i]
    return new_str

def string_splosion(str):
  new_str = ''
  for i in range(len(str)):
    if(len(str) == 1):
      return str
    if(i == 0):
        new_str += str[i]*2
    elif (i == 1):
        new_str += str[i]
    else:
        new_str += str[0:i+1]
  return new_str

'''Given a string, return the count of the number of times that a substring length 2 appears in the string and also as the last 2 chars of the string, so "hixxxhi" yields 1 (we won't count the end substring).'''
def last2(str):
    substring = str[len(str) - 2: len(str) ]
    firststring = str[:len(str)-2]
    count = 0
    for i in range (len(firststring)):
        new_substr = str[i: i+2]
        if(new_substr == substring):
            count += 1
    return count

'''Given an array of ints, return the number of 9's in the array.'''

def array_count9(nums):
  count9 = 0
  for i in range(len(nums)):
    if(nums[i] == 9):
      count9 += 1
  return count9

'''Given an array of ints, return True if one of the first 4 elements in the array is a 9. The array length may be less than 4.'''

def array_front9(nums):
  bool = False
  for i in range(len(nums[:4])):
    if(nums[i] == 9):
      bool = True
  return bool

'''Given an array of ints, return True if the sequence of numbers 1, 2, 3 appears in the array somewhere.
'''

def array123(nums):
  bool = None
  if(len(nums)<3):
      return False
  for i in range(len(nums)-1):
    if(nums[i] == 1):
        if(nums[i+1] == 2):
            if(nums[i+2] == 3):
                bool = True
  if bool is None:
      bool = False
  return bool

'''Given 2 strings, a and b, return the number of the positions where they contain the same length 2 substring. So "xxcaazz" and "xxbaaz" yields 3, since the "xx", "aa", and "az" substrings appear in the same place in both strings.
'''
def string_match(a, b):
    matches = 0
    for i in range(len(a) - 1):
        substr_a = a[i] + a[i+1]
        if i == len(b)-1:
            break
        else:
            substr_b = b[i] + b[i+1]
        if substr_a == substr_b:
            matches += 1
    return matches
