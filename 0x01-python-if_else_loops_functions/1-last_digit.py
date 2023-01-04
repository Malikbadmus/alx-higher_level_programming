#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
n_digit = int(str(number)[-1])
L_digit = 0
if number < 0:
    L_digit = -(n_digit)
else :
    L_digit = n_digit
if L_digit > 5:
    print("Last digit of {} is {} and is greater than 5".format(number, L_digit)
    )
elif L_digit == 0:
    print("Last digit of {} is {} and is 0".format(number, L_digit))
elif L_digit < 6 and L_digit != 0:
    print("Last digit of {} is {} and is less than 6 and not 0".format(number,
                                                                       L_digit))
