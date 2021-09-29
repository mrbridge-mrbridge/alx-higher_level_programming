#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
        """
        self.__size = size

    @property
    def size(self):
        """Property getter to get size"""
        return self.__size

    @size.setter
    def size(self, value):
        """Property setter to set size"""
        if type(value) is not int:
            raise TypeError('size must be an integer')
        elif value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """Return area of square"""
        return (self.__size * self.__size)
