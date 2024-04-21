#!/usr/bin/python3
""" inheritance from """


def inherits_from(obj, a_class):
    """ check if the object is an instance of a class that inherited
        Return: True if the object is an instance of a class otherwise False
    """

    return isinstance(obj, a_class) and type(obj) is not a_class
