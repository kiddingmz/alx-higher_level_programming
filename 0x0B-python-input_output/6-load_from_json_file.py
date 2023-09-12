#!/usr/bin/python3
"""Define the load/read json file function"""
import json


def load_from_json_file(filename):
    """Create an object python from JSON file"""
    with open(filename) as f:
        return json.load(f)
