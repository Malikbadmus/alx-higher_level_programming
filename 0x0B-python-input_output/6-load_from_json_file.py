#!/usr/bin/python3
"""Working with JSON"""

import json


def load_from_json_file(filename):
    """Creating an Object fron A JSON file."""

    with open(filename, "r") as f:
        new = f.read()
        newobj = json.loads(new)
    return newobj
