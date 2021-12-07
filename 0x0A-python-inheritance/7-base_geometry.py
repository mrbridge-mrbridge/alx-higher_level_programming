#!/usr/bin/python3
"""module 7-base_geometry raising exceptions"""


class BaseGeometry:
    """BaseGeometry class declared"""
    def area(self):
        """raises an exception only"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates value"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
