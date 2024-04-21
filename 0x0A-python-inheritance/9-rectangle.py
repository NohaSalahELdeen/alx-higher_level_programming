#!/usr/bin/python3
""" 9-rectangle module """


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ subclass inherits from BaseGeometry """

    def __init__(self, width, height):
        """ init method """

        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Public instance method area """
        return self.__width * self.__height

    def __str__(self):
        """ return  rectangle description """
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
