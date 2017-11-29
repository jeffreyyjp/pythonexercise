"""date_interval

This program is used to get the duration between two dates. User should input two dates, and the program will output the duration.
"""

from datetime import datetime

print('The date format is MM/DD/YY, for example: 11/29/2017')

first_date = raw_input('Please input first date: ') # get user's first date input
second_date = raw_input('Please input second date: ') # get user's second date input

def check_date(datestr):
    date_list = datestr.split('/')
    monthstr, daystr, yearstr = date_list[0], date_list[1], date_list[2]
    try:
        date_obj = datetime.datetime(int(yearstr), int(monthstr), int(daystr))
    except:
        check_date(raw_input("Invalid date, please input again: "))
    else:
        return date_obj

print(check_date(first_date) - check_date(second_date))
duration_time = (check_date(first_date) - check_date(second_date)).days
print("The duration time is: {}".format(abs(duration_time)))
