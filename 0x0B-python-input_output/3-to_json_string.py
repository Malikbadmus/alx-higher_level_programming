#!/usr/bin/python3
"""Working with JSON."""

import json


def to_json_string(my_obj):
    """Return JSON representation of an object."""
    jsonstrings = json.dumps(my_obj)
    return jsonstrings
