#!/usr/bin/python3
"""Module contains the Base class"""


class Base:
    """The class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """initialises the class base"""
        if id != None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
