''' Write a Python program to print the calendar of a given month and year.
'''

import calendar
import datetime

def get_calendar_card():
    current_year = datetime.datetime.now().year
    current_month = datetime.datetime.now().month

    Calendar = calendar.TextCalendar()
    calendar_card = Calendar.formatmonth(current_year, current_month)
    print(calendar_card)

'''Write a Python program to calculate number of days between two dates.'''

def get_day_distance():
    t1 = input('Podaj pierwszą datę w formacie RRRR/MM/DD:')
    t2 = input('Podaj drugą datę w formacie RRRR/MM/DD:')

    y1 = t1[0:4]
    m1 = t1[5:7]
    d1 = t1[8:10]


    t1 = datetime.date(int(t1[0:4]),int(t1[5:7]),int(t1[8:10]))
    t2 = datetime.date(int(t2[0:4]),int(t2[5:7]),int(t2[8:10]))

    dt = t1-t2
    print(dt)

'''Int to roman values converter in range  1 <= num <= 3999'''
'''Roman to Int converter'''
''
class RomanOperation(object):
    def intToRoman(self,num):
        M = ["", "M", "MM", "MMM"]
        C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        thousands = M[num//1000]
        houndreds = C[num%1000 // 100]
        tens = X[num%1000 %100 // 10]
        ones = I[num%1000 %100%10]

        print("Roman equivalent ", thousands+houndreds+tens+ones)

    def romanToInt(self,s):
        intSwitcher = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        substractor = ["IV", "IX", "XL", "XC", "CD", "CM"]
        substractorIntSwitcher ={
            "IV": 4,
            "IX": 9,
            "XL": 40,
            "XC": 90,
            "CD": 400,
            "CM": 900,
        }
        substractonPrecedors = ["I", "X", "C"]
        counter = 0
        skip = False
        for i in range(len(s)):
            if s[i] in substractonPrecedors:
                if i < len(s) -1:
                    ab = s[i:i+2]
                    if ab in substractor:
                        val = substractorIntSwitcher[ab]
                        counter += val
                        skip = True
                        continue
                    elif not skip:
                        counter += intSwitcher[s[i]]
                elif not skip:
                    counter += intSwitcher[s[i]]
            elif not skip:
                counter += intSwitcher[s[i]]
            skip = False
        return counter

'''Minimum Index Sum of Two Lists'''
def findRestaurant(self, list1, list2):
    common_string = []
    common_string_dict = {}
    sum_indexes = []

    for i in list1:
        if i in list2:
            common_pos1 = list1.index(i)
            common_pos2 = list2.index(i)
            sum = common_pos1 + common_pos2
            sum_indexes.append(sum)
            common_string_dict[i] = sum
    min_index = min(sum_indexes)
    for j in common_string_dict:
        if common_string_dict[j] == min_index:
            common_string.append(j)
    return common_string

def runningSum(nums):
    running_sum = []
    for i in range(1,len(nums)+1):
        running_sum.append(sum(nums[0:i]))
    return running_sum

'''Find Pivot Index'''
def pivotIndex(nums):
    for i in range(len(nums)):
        sum_front = sum(nums[0:i])
        sum_back = sum(nums[i+1:len(nums)])
        if sum_front == sum_back:
            return i
    return -1
'''Isomorphic Strings'''
'''Given two strings s and t, determine if they are isomorphic.
'''
class StringSolution():
    def isIsomorphic(self,s, t):
        letterMapping = {}
        #Mapping every s[i] letter into t[i] letter
        for i in range(len(s)):
            if i <= len(t):
                letterMapping[s[i]] = t[i]
        #Find duplicates
        resultMapping = StringSolution.findDuplicates(letterMapping)
        new_word = ''
        for i in range(len(s)):
            if s[i] in resultMapping.keys():
                new_word += letterMapping[s[i]]

        return new_word == t
    @staticmethod
    def findDuplicates(dict):
        resultMapping = {}
        for key, value in dict.items():
            if value not in resultMapping.values():
                resultMapping[key] = value
        return resultMapping

'''Return True if s is a subsequence of t'''
'''dinamic programming solution'''
def isSubsequence(s, t):
    i = 0
    j = 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
        j +=1
    return i == len(s)

# Definition for singly-linked list.
# first node -head
# To be done...
class Node:
    def __init__(self, val=None):
        self.val = val
        self.next = None
class Linkedlist:
    def __init__(self):
        self.head = Node()
    def appendNode(self,data):
        new_node = Node(data)
        current_node = self.head
        while current_node.next != None:
            current_node=current_node.next
        current_node.next = new_node
    def display(self):
        elems = []
        current_node = self.head
        while current_node.next != None:
            current_node = current_node.next
            elems.append(current_node.val)
        print(elems)
    def appendListNodes(self,list):
        llist = Linkedlist()
        for i in list:
            llist.appendNode(i)
        return llist


class ListSolution():
    def mergeTwoLists(self, list1, list2):
        list1.Linkedlist = list1
        list2.Linkedlist = list2
        print(list1.Linkedlist.printList())

list1= Linkedlist()
list1.appendListNodes([1,2,3,4])
# list1.appendNode(1)
# list1.appendNode(2)
list1.display()
solution = ListSolution()

