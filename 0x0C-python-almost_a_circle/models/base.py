#!/usr/bin/python3
"""Module contains the Base class"""
import json


class Base:
    """The class Base"""
    __nb_objects = 0

    def __init__(self, id=None):
        """initialises the class base"""
        if id is None:
            Base.__nb_objects += 1
            self.id = self.__nb_objects
        else:
            self.id = id

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        returns json string representation of 
        list_dictionaries
        """
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)
