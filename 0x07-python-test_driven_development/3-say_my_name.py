#!/usr/bin/python3
"""This module prints 'My name is <first name> <last name>'"""

def say_my_name(first_name, last_name=""):
    """prints first name and last name as strings"""
    if type(first_name) is not str:
        raise TypeError('first_name must be a string')
    if type(last_name) is not str:
        raise TypeError('last_name must be a string')

    return (print('My name is {:s} {:s}'.format(first_name, last_name)))
