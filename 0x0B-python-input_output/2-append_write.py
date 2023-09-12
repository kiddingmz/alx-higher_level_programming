#!/usr/bin/python3
"""Define the append function"""


def append_write(filename="", text=""):
    """The append function"""
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)
