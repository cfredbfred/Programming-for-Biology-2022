#!/usr/bin/env python3

import sys

'''
var = 20

if bool(var) == True:
    print('Value is True')
else:
    print('Not True')
'''

number = float(sys.argv[1])

if number > 0:
    if number <= 50:
        print('number is less than or equal to 50')
    else:
        print('number is greater than 50')
    print('positive')
elif number == 0:
    print('your number is 0')
else:
    print('negative')

if number % 2 == 0:
    print('number is even')

if number < 50 and number % 2 == 0:
    print('it is an even number that is smaller than 50')

if number > 50 and number % 3 == 0:
    print('it is larger than 50 and divisible by 3')
  
