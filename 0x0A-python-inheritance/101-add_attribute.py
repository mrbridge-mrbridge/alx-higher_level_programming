#!/usr/bin/python3
"""this module adds a new attribute to an object if it’s possible"""


def add_attribute(obj, arg1, arg2):
    """adds a new attribute to an object if it’s possible"""

    if hasattr(obj, "__dict__"):
        setattr(obj, arg1, arg2)
    else:
        raise TypeError("can't add new attribute")
