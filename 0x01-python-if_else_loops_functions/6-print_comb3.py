#!/usr/bin/python3

for i in range(0, 8):
    for x in range(i+1, 10):
        if i == x:
            continue
        print("{}{}".format(i, x), end=", ")
print("{:d}".format(89))
