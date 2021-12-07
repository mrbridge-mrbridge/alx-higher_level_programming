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


class Rectangle(BaseGeometry):
    """declare class Rectangle as inheriting from class BaseGeometry"""
    def __init__(self, width, height):
        """class constructor"""
        self.__width = width
        self.__height = height
        super().__init__()
