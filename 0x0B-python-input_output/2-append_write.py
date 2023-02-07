#!/usr/bin/python3
"""Appending strings to file"""


def append_write(filename="", text=""):
    """Append a string to a UTF8 file"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write('\n'.join(text))
        y = 0
        for x in text:
            y += 1
        return y
