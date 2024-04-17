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

    @property
    def size(self):
        """ to retrieve the size

            Return: size
        """

        return self.__size

    @size.setter
    def size(self, value):
        """ set value to size
            Args:
                value: new value to set
        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ Public instance method
            Return: the current square area
        """

        return self.__size ** 2
