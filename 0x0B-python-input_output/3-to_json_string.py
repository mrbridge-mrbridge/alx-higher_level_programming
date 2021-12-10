#!/usr/bin/python3
"""module returns the JSON representation of an object (string)"""
import json


def to_json_string(my_obj):
    """returns the JSON representation of an object (string)"""
    s = json.dumps(my_obj)
    return s
