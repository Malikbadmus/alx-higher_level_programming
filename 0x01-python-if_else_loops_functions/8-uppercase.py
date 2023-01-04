#!/usr/bin/python3
def uppercase(str):
    x = ""
    z= " "
    for i in str:
        if(ord(i) >= 97 and ord(i) <= 122):
            x = ord(i) - 32
            i = chr(x)
        print("{}".format(i), end="")
        print("{}".format(z), end="")
