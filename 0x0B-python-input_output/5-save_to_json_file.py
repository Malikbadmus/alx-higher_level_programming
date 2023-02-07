#!/usr/bin/python3
"""Write Obj To a File Using JSON."""

import json


def save_to_json_file(my_obj, filename):
    """Write an object to a text file using JSON representation."""
    newobj = json.dumps(my_obj)
    with open(filename, "w") as f:
        f.write(newobj)
