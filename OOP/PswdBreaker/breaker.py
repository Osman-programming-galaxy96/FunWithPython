# Password cracker : assumed every password has one upper letter within and digit at last position
def appendNumber(password, digit, passwordList):
    passwordList.append(password+str(digit))
    if digit < 9:
        return appendNumber(password, digit+1, passwordList)
    else:
        return passwordList

def replaceLetter(password, i , passwordList):
    upper = password[i].upper()
    new_str = password[0:i] + upper + password[i+1:len(password)]
    passwordList.append(new_str)
    while i < len(password)-1:
        return replaceLetter(password, i+1, passwordList)
    return passwordList

def passwordCracker(password):
    replacedLetterList = replaceLetter(password, 0, [])
    passList = []
    for i in range(len(replacedLetterList)):
        passWithDigit = appendNumber(replacedLetterList[i], 0, [])
        passList.append(passWithDigit)
    return passList

def passLister(passList):
    for i in passList:
        print(i)