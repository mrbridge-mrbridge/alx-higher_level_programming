#!/usr/bin/python3
"""module returns the list of available attributes and methods of an object"""


def lookup(obj):
    """function accepts obj as input and list all
    available attributes and methods of an obj"""
    return (dir(obj))
