#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    if my_list is None:
        return
    new_list = my_list[::-1]
    for x in (new_list):
        print("{:d}".format(x))
