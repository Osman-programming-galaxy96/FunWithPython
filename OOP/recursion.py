# # !/usr/bin/env python

import sys

print(sys.argv[0])

def countElem(array, pos):
    if pos == len(array)-1:
        return pos+1
        print("Suma elementów to: ", pos)
    else:
        return countElem(array, pos+1)
