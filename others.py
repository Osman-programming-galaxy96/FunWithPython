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
