# encoding: UTF-8

"""incremental number

This program needs user to input three integer numbers as start, end and increment. And then it will output a list of numbers. For example: s == 6, e == 26, i == 4, the program will output a list of numbers such as 6, 10, 14, 18, 22, 26.
"""

import os 

def get_increnumbers(start, end, increment):
    list_numbers = [start]
    curr_num = start
    while curr_num + increment <= end:
        curr_num += increment
        list_numbers.append(curr_num)
    return list_numbers

start = int(input('Please input start number: '))

end = int(input('Please input end number(bigger than start): '))
while end < start:
    end = int(input('End number is lower than start, please input again: '))

increment = int(input('Please input increment number: '))
while increment <= 0:
    increment = int(input('Increment number must be positive integer number: '))

print('*' * 50)
print('Your input is: start = {0}, end = {1}, increment = {2}'.format(start, end, increment))
print("The result is {}".format(get_increnumbers(start, end, increment))) 

os.system('pause')