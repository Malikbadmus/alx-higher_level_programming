#!/usr/bin/python3
def uppercase(str):
    x = ""
    for i in str:
        if(ord(i) >= 65 and ord(i) <= 90):
            x = ord(i) + 32
            i = chr(x)
    print("{}".format(i), end="")
