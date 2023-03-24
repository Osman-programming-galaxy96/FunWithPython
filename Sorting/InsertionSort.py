import random
def InsertionSort(tab):
    for step in range(1, len(tab)):
        key = tab[step]
        j = step - 1
        while j >= 0 and key < tab[j]:
            tab[j + 1] = tab[j]
            j = j - 1
        tab[j + 1] = key

    print(tab)


def randomInt(size):
    intArray = []
    for i in range(size):
        a = random.randint(1,99)
        intArray.append(a)
    return intArray

# InsertionSort(randomInt(7))
InsertionSort([1,5,7,8,4,3])
# randomInt(7)

