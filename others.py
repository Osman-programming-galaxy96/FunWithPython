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
