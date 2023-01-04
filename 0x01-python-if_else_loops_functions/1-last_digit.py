#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n_digit = abs(number) % 10
if number < 0:
    L_d = -(n_digit)
else:
    L_d = n_digit
if L_d > 5:
    print(f"Last digit of {number:d} is {L_d:d} and is greater than 5")
elif L_d == 0:
    print("Last digit of {} is {} and is 0".format(number, L_d))
elif L_d < 6 and L_d != 0:
    print(f"Last digit of {number:d} is {L_d:d} and is less than 6 and not 0")
