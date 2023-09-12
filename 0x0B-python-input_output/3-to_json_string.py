#!/usr/bin/python3
"""Define the string-to-JSON function"""
import json


def to_json_string(my_obj):
    """Return the JSON representaio by my_obj"""
    return json.dumps(my_obj)
