#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            str[i] = str[i] - chr(32)
        print('{}'.format(str[i]), end='')
    print('')
