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
