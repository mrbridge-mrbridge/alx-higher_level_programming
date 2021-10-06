#!/usr/bin/python3
"""This module defines an class called Rectangle"""


class Rectangle:
    """A new class classed Rectangle"""
    
    def __init__(self, width=0, height=0):
        """
        Instantiation of class with
        width and height
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """An instance attribute to retrieve width"""
        self.__width__ = width

    @width.setter
    def width(self, value):
        """An instance attribute to set width"""
        if type(value) is not int:
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width__ = value

    @property
    def height(self):
        """An instance attribute to retrieve height"""

        self.__height__ = height

    @height.setter
    def height(self, value):
        """An intance attribute to set height"""
        if type(value) is not int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height__ = value
