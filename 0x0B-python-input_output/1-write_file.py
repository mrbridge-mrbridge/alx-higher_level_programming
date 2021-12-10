#!/usr/bin/python3
"""Writes a string to a text file (UTF8) and returns
    the number of characters written
    Must use the with statement
    Should create the file if doesn’t exist
"""


def write_file(filename="", text=""):
"""
    writes a string to a text file (UTF8) and
    returns the number of characters written
"""
    with open(filename, 'w', encoding='utf8') as f:
        return f.write(text)
