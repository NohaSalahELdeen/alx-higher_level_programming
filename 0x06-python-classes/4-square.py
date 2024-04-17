#!/usr/bin/python3
""" defines a class """


class Square:
    """ defines a square class """

    def __init__(self, size=0):
        """ Instantiation with size

            Args:
                size: Private instance attribute
        """

        self.__size = size

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

    def size(self, value):
        """ set value to size
            Args:
                value: new value to set
        """

        self.__size = value

    def size(self):
        """ to retrieve the size

            Return: size
        """

        return self.__size

    def area(self):
        """ Public instance method
            Return: the current square area
        """

        return self.__size ** 2
