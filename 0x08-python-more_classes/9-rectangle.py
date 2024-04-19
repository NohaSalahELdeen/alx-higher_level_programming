#!/usr/bin/python3
""" Rectangle module """


class Rectangle:
    """ Rectangle class """

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """ init method
            Args:
                width: the width of rectangle.
                height: the height of rectangle.
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

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
            string += "\n".join(str(self.print_symbol) * self.__width
                                for i in range(self.__height))
            return string

    def __repr__(self):
        """ return a string representation of the rectangle """
        return ("Rectangle({}, {})".format(self.__width, self.__height))

    def __del__(self):
        """ Print the message """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """ Compare rectangles
            Args:
                rect_1: first rectngle
                rect_2: second erctangle
            Return: rect_1 if both have the same area value
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_2.area() > rect_1.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """ that returns a new Rectangle instance
            Args:
                size: the size of new Rectangle
        """

        return cls(size, size)
