#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
if (number % 10) > 5:
    print('Last digit of', number, 'is', number % 10, 'and is greater than 5')
if (number % 10) == 0:
    print('Last digit of', number, 'is', number % 10, 'and is zero')
if (number % 10) < 6 and (number % 10) != 0:
    print('Last digit of', number, 'is', number % 10, 'and is less than 6 and not 0')
