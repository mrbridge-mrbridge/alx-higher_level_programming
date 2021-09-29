#!/usr/bin/python3
"""Defining a class Node"""

class Node:
    """A class Node"""
    def __init__(self, data, next_node=None):
        """Intsantiation of data and next_node

        Args:
            data: data in a list
            next_node: next node in list
        """

        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """To get data"""
        return self.__data

    @data.setter
    def data(self, value):
        """To set data"""
        if type(value) is not int:
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """To get next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """To set next_node"""
        
        if value != None or type(value) is not Node:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value

class SinglyLinkedList:
    """A class that defines singly linked list"""

    def __init__(self):
        """Initialize singly linked lists"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node"""
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > value:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < value):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        values = []
        tmp = self.__head
        while tmp is not None:
            values.append(str(tmp.data))
            tmp = tmp.next_node
        return ('\n'.join(values))
