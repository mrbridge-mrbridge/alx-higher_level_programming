#!/usr/bin/python3
"""module returns True if the object is an instance of,
or if the object is an instance of a class that inherited
from, the specified class ; otherwise False"""


def is_kind_of_class(obj, a_class):
    """returns True for being type of a_class
    or of parentclass of a_class. Else False"""
    if isinstance(obj, a_class):
        return True
    else:
        return False
