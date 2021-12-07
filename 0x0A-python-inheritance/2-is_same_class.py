#!/usr/bin/python3
"""module returns True if the object is exactly an instance 
    of the specified class ; otherwise False"""


def is_same_class(obj, a_class):
    """checks if obj is an instance of a_class"""
    if type(obj) == a_class:
        return True
    else:
        return False
