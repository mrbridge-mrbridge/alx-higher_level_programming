#!/usr/bin/python3
def no_c(my_string):
    cp = ""
    for i in my_string:
        if i != 'c' and i != 'C':
            cp += i
    return cp
