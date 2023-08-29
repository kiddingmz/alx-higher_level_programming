#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """Represent the class square."""
    def __init__(self, size=0, position=(0, 0)):
        """Initialization constrution.

        Args:
            size (int): size
            position (int, int)): position

        Return:
            nothing
        """
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
        self.__position = position

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
            [print("") for i in range(0, self.__position[1])]
            for i in range(0, self.__size):
                [print(" ", end="") for j in range(0, self.__position[0])]
                [print("#", end="") for k in range(0, self.__size)]
                print()

    @property
    def position(self):
        """Get the position

        Return:
            position
        """
        return (self.__position)

    @position.setter
    def posiiton(self, value):
        """Set position

        Args:
            value (tuple): tuple
        """
        if ((not isinstance(value, tuple)) or len(value) != 2 or
                (not all(nu >= 0 for nu in value)) or
                (not all(isinstance(nu, int) for nu in value))):
            raise TypeError('position must be a tuple of 2 positive integers')
        self.__position = value
