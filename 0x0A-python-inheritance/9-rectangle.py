#!/usr/bin/python3
"""module inherits from 7-base_geometry.BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""import parent class"""


class Rectangle(BaseGeometry):
    """declare class Rectangle as inheriting from class BaseGeometry"""
    def __init__(self, width, height):
        """class constructor"""
        self.__width = width
        self.__height = height
        super().integer_validator('width', width)
        super().integer_validator('height', height)

    def area(self):
        """return the area of the Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """return string representation of Rectangle"""
        return ("[{}] {}/{}".format(Rectangle.__name__, self.__width, self.__height))
