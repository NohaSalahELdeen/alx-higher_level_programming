#!/usr/bin/python3
""" Rectangle module """


class Rectangle:
    """ Rectangle class """
    def __init__(self, width=0, height=0):
        """ init method
            Args:
                width: the width of rectangle.
                height: the height of rectangle.
        """

        self.width = width
        self.height = height

    @property
    def height(self):
        """ height method
            Return: height
        """
        return self.__height

    @height.setter
    def height(self, value):
        """ set value to height """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    @property
    def width(self):
        """ width method
            Return: width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """ set value to width """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    def area(self):
        """ the rectangle area method
            Return:  the rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """ the rectangle perimeter method
            Return: the rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return 2 * (self.__height + self.__width)

    def __str__(self):
        """ str method that print the rectangle with the character #
            Return: string
        """
        string = ""
        if self.__width == 0 or self.__height == 0:
            return string
        else:
            string += "\n".join("#" * self.__width
                                for i in range(self.__height))
            return string

    def __repr__(self):
        """ return a string representation of the rectangle """
        return ("Rectangle({}, {})".format(self.__width, self.__height))
