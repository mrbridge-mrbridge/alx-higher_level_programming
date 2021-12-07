#!/usr/bin/python3
"""module that inherits from list
prints the list, but sorted (ascending sort)
"""


class MyList(list):
    """class 'MyList' inherits from class 'list'"""
    def print_sorted(self):
        """prints the list, but sorted (ascending sort)"""
        print(sorted(self))
