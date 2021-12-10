#!/usr/bin/python3
"""module with class MyInt that inherits from int"""


class MyInt(int):
    """class overturns the use of == and != """
    def __eq__(self, value):
        """== becomes !="""
        return int(self) != value

    def __ne__(self, value):
        """!= becomes =="""
        return int(self) == value
