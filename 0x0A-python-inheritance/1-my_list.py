#!/usr/bin/python3
""" MyList module """


class MyList(list):
    """ subclass MyList that inherits from list """

    def print_sorted(self):
        """ prints sorted list """
        print(sorted(self))
