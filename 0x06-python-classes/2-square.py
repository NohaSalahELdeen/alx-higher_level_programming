#!/usr/bin/python3
""" Define a square class """


class Square:
    """  a class Square that defines a square """

    def __init__(self, size=0):
        """ defined a method

        Args:
            size: The size of a square
        """

        self.__size = size

        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
