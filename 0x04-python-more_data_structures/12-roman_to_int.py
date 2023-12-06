#!/usr/bin/python3
def roman_to_int(roman_string):
    dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}

    number = 0
    for i in range(len(roman_string)):
        value = dic[roman_string[i]]
        if i + 1 < len(roman_string) and dic[roman_string[i + 1]] > value:
            number -= value
        else:
            number += value
    return number
