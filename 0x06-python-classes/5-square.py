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

    def area(self) -> int:
        """Define the area for the square.

        Return:
            area
        """
        return (self.__size * self.__size)

    @property
    def size(self):
        """Get size the square

        Return:
            size
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """Set the size square."""
        if not isinstance(value, int):
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def my_print(self):
        """Print the square #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size, end="")
                print()
