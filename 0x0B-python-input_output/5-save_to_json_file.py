#!/usr/bin/python3
"""Define the json to file function"""
import json


def save_to_json_file(my_obj, filename):
    """Write an file using JSON content"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
