#!/usr/bin/python3
"""module 7-base_geometry raising exceptions"""


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
