#!/usr/bin/python3
"""Define the class to json function"""


def class_to_json(obj):
    """Return the dictionary"""
    return obj.__dict__
