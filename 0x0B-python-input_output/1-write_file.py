#!/usr/bin/python3
"""Write string to a test File."""


def write_file(filename="", text=""):

    """writing file"""

    with open(filename, "w", encoding="utf-8") as f:
        f.write(text)
        y = 0
        for x in text:
            y += 1
        return y
