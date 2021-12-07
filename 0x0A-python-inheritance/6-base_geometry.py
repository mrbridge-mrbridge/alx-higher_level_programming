#!/usr/bin/python3
"""raises an Exception with the message area() is not implemented"""


class BaseGeometry:
    """class BaseGeometry"""
    def area(self):
        """raises an exception"""
        raise Exception("area() is not implemented")
