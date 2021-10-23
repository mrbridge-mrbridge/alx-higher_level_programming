#!/usr/bin/python3
"""Module contains the Base class"""
import json
import csv
import turtle


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

    @staticmethod
    def from_json_string(json_string):
        """
        returns the pyhton dict of json string
        """
        if json_string is None or len(json_string == 0):
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation 
        of list_objs to a file
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, 'w') as f:
            if list_objs is None:
                f.write("[]")
            else:
                list_objs = [elm.to_dictionary() for elm in list_objs]
                f.write(Base.to_json_string(list_objs))
