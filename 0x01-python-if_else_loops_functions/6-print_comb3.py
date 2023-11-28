#!/usr/bin/python3
for ten_digits in range(0, 10):
    for units in range(ten_digits + 1, 10):
        if ten_digits == 8 and units == 9:
            print("{}{}".format(ten_digits, units))
        else:
            print("{}{}".format(ten_digits, units), end=", ")