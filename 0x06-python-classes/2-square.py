#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent the class square."""
    def __init__(self, size=0):
        """Initialization constrution.

        Args:
            size (int): size

        Return:
            nothing
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
