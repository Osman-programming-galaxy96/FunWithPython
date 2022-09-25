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
    print('test long solution', timeit.timeit(lambda : caught_speeding_long_v(a,b)))
    print('test short solution', timeit.timeit(lambda : caught_speeding_short_v(a,b)))
    print('test ultra solution', timeit.timeit(lambda : caught_speeding_ultra_v(a,b)))

testing_cought_speeding()

