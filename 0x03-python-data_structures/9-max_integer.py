#!/usr/bin/bython3
def max_integer(my_list=[]):
    number = my_list[0]
    for biggest in my_list:
        if biggest > number:
            number = biggest
    return number
