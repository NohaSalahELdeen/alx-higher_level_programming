#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if len(my_list) == 0:
        return None
    new = my_list.copy()
    for i in range(len(my_list)):
        if i % 2 == 0:
            return new.append(True)
        else:
            return new.append(False)
    return new
