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
        """Set a with"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Return a height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set a height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Return a x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Set a x"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Return a y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Set a y"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return an area"""
        return self.width * self.height

    def display(self):
        """Print a rectangle"""
        rectangle = self.y * "\n"
        for i in range(self.height):
            rectangle += (" " * self.x)
            rectangle += ("#" * self.width) + "\n"

        print(rectangle, end='')
