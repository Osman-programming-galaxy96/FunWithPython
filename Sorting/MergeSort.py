def printTab(tab):
    for i in tab:
        print(i, ' | ',end='')
    sortMerge(tab, 0, len(tab)-1)

def merge(tab, l, q, r):
    lSize = q - l + 1
    rSize = r - q

    left = [0] * lSize
    right = [0] * rSize

    for x in range(lSize):
        left[x] = tab[l + x]
    for y in range(rSize):
        right[y] = tab[q + y + 1]

    leftIndex = 0
    rightIndex = 0
    currIndex = n


def sortMerge(tab, l, r):
    # if r > 1:
    q = int((l+r)/2)
    print('Q środek podziału',q)
    sortMerge(tab, l, q)
    sortMerge(tab, q+1, r)
    merge(tab,l,q,r)

printTab([1,5,7,8,4,3])