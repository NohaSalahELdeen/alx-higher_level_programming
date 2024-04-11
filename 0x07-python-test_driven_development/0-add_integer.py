#!/usr/bin/python3
""" adds 2 integers."""


def add_integer(a, b=98):
    """ add_integer a function that adds 2 integers.

        Args:
        a: the first int or float number.
        b: the secand int or float number.

        Return: an integer the addition of a and b
    """

    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    elif type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")

    return int(a) + int(b)
