#!/usr/bin/python3
def uppercase(str):
    if ord(str) >= 97 and ord(str) <= 122:
        ord(str) = ord(str) - 32
        print('{}'.format(str))
    else:
        print('{}'.format(str))
