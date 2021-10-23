#!/usr/bin/python3
"""this module inherits from class Base"""

from models.base import Base


class Rectangle(Base):
    """the Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initialises the class Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the width"""
        return self.__width

    @property
    def height(slf):
        """get the height"""
        return self.__height

    @property
    def x(self):
        """get the x"""
        return self.__x

    @property
    def y(self):
        """get the y"""
        return self.__y

    @width.setter
    def width(self, value):
        """set the width"""
        self.__width = value

    @height.setter
    def height(self, value):
        """set the height"""
        self.__height = value

    @x.setter
    def x(self, value):
        """set the x"""
        self.__x = value

    @y.setter
    def y(self, value):
        """set the y"""
        self.__y = value
