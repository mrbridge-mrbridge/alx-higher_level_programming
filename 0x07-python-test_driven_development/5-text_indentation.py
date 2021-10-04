#!/usr/bin/python3
"""
This module prints a text with 2 new lines after each of these characters: ., ? and :
"""
def text_indentation(text):
    """fuction accepts string and print indented string"""

    if type(text) is not str:
        raise TypeError('text must be a string')

    flag = 0
    for elm in text:
        if flag == 0:
            if elm == ' ':
                continue
            flag = 1
        if flag == 1:
            if elm in list(':.?'):
                print(elm + '\n')
                flag = 0
            else:
                print(elm, end='')
