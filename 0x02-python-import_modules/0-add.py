#!/usr/bin/python3
if __name__ == "__main__":
    from add_0 import add
    """
        import add function from py file
        print the result of the addition 1 + 2 = 3
    """

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
