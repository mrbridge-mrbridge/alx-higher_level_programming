#!/usr/bin/python3
"""module with class Square that inherits from Rectangle (9-rectangle.py)"""


Rectangle = __import__('9-rectangle').Rectangle
"""class Rectangle imported"""


class Square(Rectangle):
    """class Square declared"""

    def __init__(self, size):
        """class constructor"""
        self.__size = size
        super().integer_validator("size", size)

    def area(self):
        """return the area of the Square"""
        return self.__size * self.__size

    def __str__(self):
        """return string representation of Rectangle"""
        return ("[Square] {}/{}".format(self.__size, self.__size))
