#!/usr/bin/python3
"""Define the class Square inheritance of class Rectangle"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """The Class Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor"""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """str"""
        str_square = "[Square] "
        str_id = "({}) ".format(self.id)
        str_xy = "{}/{} - ".format(self.x, self.y)
        str_wh = "{}/{}".format(self.width, self.height)

        return (str_square + str_id + str_xy + str_wh)

    @property
    def size(self):
        """Return a width"""
        return (self.width)

    @size.setter
    def size(self, value):
        """Set the size"""
        self.width = value
        self.height = value

