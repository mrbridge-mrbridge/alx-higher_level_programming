#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            str2[i] = str[i] - chr(32)
            print('{}'.format(str2))
        else:
            print('{}'.format(chr(i)))
