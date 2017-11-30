# encoding: UTF-8

"""date_interval

This program is used to get the duration between two dates. User should input two dates, and the program will output the duration.
"""

import re, os
from datetime import date

def check_date_format(datestr):
    """ check the date format input. """
    while re.search('\d\d/\d\d/\d\d\d\d', datestr) == None:
        datestr = raw_input('Invalid date format, try again: ')
    return datestr

def get_date(datestr, dateflag):
    """ Get date object. """
    date_list = datestr.split('/')
    monthstr, daystr, yearstr = date_list[0], date_list[1], date_list[2]
    print("{0} date: year = {1}, month = {2}, day = {3}".format(dateflag, yearstr, monthstr, daystr))
    try:
        date_obj = date(int(yearstr), int(monthstr), int(daystr))
    except:
        # date_obj = raw_input("Invalid date, please input again: ")
        return get_date(raw_input("Invalid {} date, please input again: ".format(dateflag)), dateflag)
    else:
        return date_obj

def get_date_diff(firstdate, seconddate):
    """ Get duration between two dates. """
    return abs((get_date(firstdate, "First") - get_date(seconddate, "Second")).days)

print('The date format is MM/DD/YY, for example: 11/29/2017')

# Get user input and check date format
first_date = check_date_format(raw_input('Please input first date: '))
second_date = check_date_format(raw_input('Please input second date: '))

print("The duration time is: {}".format(get_date_diff(first_date, second_date)))

os.system('pause')