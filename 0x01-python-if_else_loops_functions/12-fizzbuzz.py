#!/usr/bin/python3
def fizzbuzz():
    for num in range(1, 101):
        if num % 3 == 0:
            print('{}'.format('Fizz'), end=' ')
        elif num % 5 == 0:
            print('{}'.format('Buzz'), end=' ')
        elif num % 3 == 0 and num % 5 == 0:
            print('{}'.format('FizzBuzz'), end=' ')
        else:
            print('{}'.format(num), end=' ')
