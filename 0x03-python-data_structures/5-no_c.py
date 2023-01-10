#!/usr/bin/python3

def no_c(my_string):
    new_str = ""
    for x in my_string:
        if x == 'c' or x == 'C':
            continue
        new_str = "".join(x)
        return (new_str)
