#!/usr/bin/python3
""" is_same_class module """


def is_same_class(obj, a_class):
    """ check if the object is exactly an instance of the specified class
        Args:
            obj: object
            a_class: class

        Return: true if the object is exactly an instance of the class or False
    """

    return type(obj) == a_class
