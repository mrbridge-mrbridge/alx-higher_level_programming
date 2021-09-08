#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            str2[i] = str[i] - chr(32)
            print('{:c}'.format(str2[i]))
        else:
            print('{:c}'.format(str[i]))
