#!/usr/bin/python3
"""Function for add two integer"""


def add_integer(a, b=98):
    """Add two integer

    Return:
        sum

    Raises:
        TypeError: non number
    """
    if type(a) not in [int, float]:
        raise TypeError('a must be an integer')
    if type(b) not in [int, float]:
        raise TypeError('b must be an integer')
    return (int(a) + int(b))
