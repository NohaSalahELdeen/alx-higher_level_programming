#!/usr/bin/python3
""" defines a class """


class Square:
    """ defines a square class """

    def __init__(self, size=0, position=(0, 0)):
        """ Instantiation with size

            Args:
                size: Private instance attribute
                position: position of space
        """

        self.__size = size
        self.__position = position

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

    @property
    def position(self):
        """ use by using space
            Return: the position
        """
        return self.__position

    @position.setter
    def position(self, value):
        """ set value to position """
        if not isinstance(value, tuple) and len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """ Public instance method
            Return: the current square area
        """

        return self.__size ** 2

    def my_print(self):
        """ prints in stdout the square with the character # """

        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__position[0]):
                    print(" ", end="")
                print("#" * self.__size)
