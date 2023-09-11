#!/usr/bin/python3
"""A module for print a list in sorted"""


class MyList(list):
    """A class to customize the list class """

    def print_sorted(self):
        """Prints a list in ascending order"""
        print(sorted(self))
