#!/usr/bin/python3
"""Define the write file function"""


def write_file(filename="", text=""):
    """Write the file"""
    with open(filename, 'w', encoding="utf-8") as f:
        nc = f.write(text)

    return (nc)
