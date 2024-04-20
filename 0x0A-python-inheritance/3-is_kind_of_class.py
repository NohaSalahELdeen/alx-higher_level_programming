#!/usr/bin/python3
""" Same class or inherit from module """


def is_kind_of_class(obj, a_class):
    """ check if the object is an instance of
        Args:
            obj: object
            a_class: class
        Return: True
    """

    return isinstance(obj, a_class)
