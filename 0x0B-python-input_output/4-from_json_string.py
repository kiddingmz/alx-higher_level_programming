#!/usr/bin/python3
"""Define the json to strong function"""
import json


def from_json_string(my_str):
    """Return the Python object representation of a JSON string"""
    return json.loads(my_str)
