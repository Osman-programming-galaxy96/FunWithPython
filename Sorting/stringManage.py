def front_back(str):
    if(len(str) <= 1):
        return str
    else:
        new_str = str[len(str)-1] + str[1:len(str)-1] + str[0]
    return new_str

def spell_backwards(str):
    return str[::-1]

def string_bits(str):
  if(len(str) <= 1):
    return str
  else:
    new_str = str[0]
    for i in range(1,len(str)):
      if(i%2 == 0):
        new_str+=str[i]
    return new_str