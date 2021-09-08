#!/usr/bin/python3
def uppercase(str):
    if ord(str) >= 97 and ord(str) <= 122:
        str2 = ord(str) - 32
        print("{str2}")
    else:
        print("{str}")
