#!/usr/bin/python3
def uniq_add(my_list=[]):
    elements = []
    sum_list = 0
    for i in my_list:
        if i not in elements:
            elements.append(i)
            sum_list += i
    return sum_list
