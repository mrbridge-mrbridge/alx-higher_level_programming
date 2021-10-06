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
        """Get width of Rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of Rectangle"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """Get height of Rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of Rectangle"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value
