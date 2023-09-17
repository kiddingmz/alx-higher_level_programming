#!/usr/bin/python3
"""Define the class Rectangle"""
from models.base import Base


class Rectangle(Base):
    """The Class Rectangle inheritance of class Base"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """construtor"""
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        """Return a width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the with"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Return height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
