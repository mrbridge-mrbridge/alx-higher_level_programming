#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent a square."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square.
        Args:
            size (int): The size of the new square.
            position (int, int): Position of square
        """
        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """To get position"""
        return self.__position

    @position.setter
    def position(self, value):
        """To set position"""
        if type(value) is not tuple or \
                len(value) != 2 or \
                type(value[0]) is not int or value[0] < 0 or \
                type(value[1]) is not int or value[1] < 0:
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value

    def area(self):
        """Return area of square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with # character"""

        if self.__size != 0:
            for i in range(self.__position[1]):
                print()

            for i in range(self.__size):
                print(' ' * self.position[0], end='')
                [print('#', end='') for j in range(self.__size)]
                print('')
        else:
            print()
