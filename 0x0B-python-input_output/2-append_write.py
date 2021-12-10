#!/usr/bin/python3
""" appends a string to a text file (UTF8) and
    returns the number of characters written"""


def append_write(filename="", text=""):
    """
    Appends a string to a text file (UTF8) and returns
    the number of characters written
    Must use the with statement
    Should create the file if doesn’t exist
    """
    with open(filename, 'a', encoding='utf8') as f:
        return f.write(text)
