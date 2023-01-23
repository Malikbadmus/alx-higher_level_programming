#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
        p_list = my_list[:x]
        try:
            print(*p_list, sep = "")
            print("nb_print: {:d}".format(x))
        except IndexError:
            print("Error in your program")
