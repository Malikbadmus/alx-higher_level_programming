#!/usr/bin/python3
"""Converting python to JSON."""


import json


def from_json_string(my_str):
    """JSON to OBJECT."""

    newobj = json.loads(my_str)
    return newobj
