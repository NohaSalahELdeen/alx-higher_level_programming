#!/usr/bin/python3
""" inheritance from """


def inherits_from(obj, a_class):
    """ check if the object is an instance of a class that inherited
        Args:
            obj: object
            a_class: a class
        Return: True if the object is an instance of a class otherwise False
    """
    return isinstance(obj, a_class) and type(obj) != a_class
