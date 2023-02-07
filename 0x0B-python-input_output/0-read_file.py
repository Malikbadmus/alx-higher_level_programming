#!/usr/bin/python3

def read_file(filename=""):
    with open(filename, encoding = 'utf8') as one:
        contents = one.read()
        print(contents)
