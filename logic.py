'''When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.

'''

def cigar_party(cigars, is_weekend):
  if(is_weekend):
    return cigars >= 40
  else:
    return cigars >= 40 and cigars <=60


'''You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.

'''
# 0- no ticket
# 1- small ticket
# 2- big ticket
import timeit
def caught_speeding_long_v(speed, is_birthday):
  if(is_birthday):
    if(speed >=81 +5):
      return 2
    elif(speed > 60+5 and speed <= 80+5):
      return 1
    else:
      return 0
  else:
    if(speed >=81):
      return 2
    elif(speed > 60 and speed <= 80):
      return 1
    else:
      return 0

def caught_speeding_short_v(speed, is_birthday):
    birthday_val = 5 if is_birthday else 0
    if speed >= 81 + birthday_val:
        return 2
    elif (speed >= 60 + birthday_val and speed <= 80 + birthday_val):
        return 1
    else:
        return 0

def caught_speeding_ultra_v(speed, is_birthday):
    birthday_val = 5 if is_birthday else 0
    if(speed <= 60 + birthday_val):
        return 0
    if(speed >60 + birthday_val and speed <=80 + birthday_val):
        return 1
    return 2

def testing_cought_speeding():
    a = 82
    b = False
    print('test long solution\t\t', timeit.timeit(lambda : caught_speeding_long_v(a,b)))
    print('test short solution\t\t', timeit.timeit(lambda : caught_speeding_short_v(a,b)))
    print('test ultra solution\t\t', timeit.timeit(lambda : caught_speeding_ultra_v(a,b)))

# testing_cought_speeding()

'''Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".

'''
def alarm_clock(day, vacation):
  weekdays = "10:00" if vacation else "7:00"
  weekends = "off" if vacation else "10:00"
  if day >=1 and day <= 5:
      return weekdays
  else:
      return weekends

'''The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.

'''
def love6(a, b):
  ret = False
  if((a+b == 6 or abs(a-b) == 6) or (a==6 or b==6 )):
    ret = True
  return ret

'''Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.

'''
def in1to10_hard_mode(n, outside_mode):
  not_in_outside_mode = True if n in range (1,11) and not outside_mode else False
  outside_mode_ON = True if n <=1 or n >=10 and outside_mode else False
  if(outside_mode):
    return outside_mode_ON
  return not_in_outside_mode

def in1to10(n, outside_mode):
  if(outside_mode):
    return (n <=1 or n>=10)
  else:
    return (n in range(1,11))

'''
We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks
'''
def make_bricks(small, big, goal):
  leavings = goal - (big*5)
  if(leavings <0):
    leavings = goal%5
  if(leavings == 0):
    return True
  if(leavings >0 ):
    leavings = leavings-(small*1)
  return leavings <= 0

'''Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.

'''
def lone_sum(a, b, c):
  sum = 0
  if a!=b and a!=c:
    sum += a
  if b!=c and b!=a:
    sum += b
  if c!=a and c!=b:
    sum += c
  return sum

'''Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.

'''
def lucky_sum(a, b, c):
  sum = 0
  if a!=13:
    sum += a
  if b!=13 and a!=13:
    sum +=b
  if c!=13 and b!=13 and a!=13:
    sum += c
  return sum

'''Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().

'''

def no_teen_sum(a, b, c):
  sum = 0
  if not fix_teen(a):
    sum += a
  if not fix_teen(b):
    sum += b
  if not fix_teen(c):
    sum += c
  return sum

def fix_teen(n):
  return n >= 13 and n <=19 and n!= 15 and n!=16