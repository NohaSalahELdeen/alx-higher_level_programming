#!/usr/bin/python3
""" 10-square module """


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ Square class inherits  from rectangle """

    def __init__(self, size):
        """ init method """
        if self.integer_validator("size", size):
            self.__size = size
        super().__init__(size, size)

    def area(self):
        """ Public instance method area """
        return super().area()
