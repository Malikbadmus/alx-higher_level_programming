#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    try:
        p_list = my_list[:x]
        print(*p_list, sep = "")
        print("nb_print: {:d}".format(x))
    except:
        print("Error in your program")
