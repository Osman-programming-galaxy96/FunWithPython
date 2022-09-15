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

