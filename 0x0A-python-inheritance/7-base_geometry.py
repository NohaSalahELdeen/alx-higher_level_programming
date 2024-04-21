#!/usr/bin/python3
""" 7-base_geometry module """


class BaseGeometry:
    """ BaseGeometry class """

    def area(self):
        """ Public instance method area """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ Public instance method that validates value """
        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")
