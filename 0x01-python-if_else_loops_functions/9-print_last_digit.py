#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number %= -10
    else:
        number %= 10
    print("{}".format(abs(number)), end="")
    return abs(number)
