#!/usr/bin/python3
"""Define the read file function"""


def read_file(filename=""):
    """Print the read file"""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            print(line, end='')
