#!/usr/bin/python3
"""this module is about a square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Square class"""
    def __init__(self, size, x=0, y=0, id=None):
        """initalisation of class square"""
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """get the size"""
        return self.width

    @size.setter
    def size(self, value):
        """set the size"""
        self.width = value
        self.height = value

    def __str__(self):
        """str() representation of square"""
        return "[{}] ({}) {}/{} - {}".format(self.__class__.__name__,
                                             self.id, self.x, self.y,
                                             self.width)

    def update(self, *args, **kwargs):
        """using *args and **kwargs to update class
        attributes
        """
        if len(args):
            for k, v in enumerate(args):
                if k == 0:
                    self.id = v
                if k == 1:
                    self.size = v
                if k == 2:
                    self.x = v
                if k == 3:
                    self.y = v
        else:
            if "id" in kwargs:
                self.id = kwargs["id"]
            if "size" in kwargs:
                self.size = kwargs["size"]
            if "x" in kwargs:
                self.x = kwargs["x"]
            if "y" in kwargs:
                self.y = kwargs["y"]
