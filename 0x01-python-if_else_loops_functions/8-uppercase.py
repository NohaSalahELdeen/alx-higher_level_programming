#!/usr/bin/python3
def uppercase(str):
    for i in str:
        if ord(i) >= 97:
            i = ord(i) - 32
            print("{}".format(chr(i)))
        else:
            print("{}".format(i))
