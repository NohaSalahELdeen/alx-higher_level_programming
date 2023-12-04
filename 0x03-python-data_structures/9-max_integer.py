#!/usr/bin/bython3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    elif len(my_list) > 0:
        number = my_list[0]
        for biggest in my_list:
            if biggest > number:
                number = biggest
    return number
