#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string != str or roman_string is None:
        return 0
    number = 0
    roman_list = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100,
                  "D": 500, "M": 1000}
    for i in range(len(roman_string)):
        result = roman_list[roman_string[i]]
        if i + 1 < len(roman_string) and roman_list[roman_string
                                                    [i + 1]] > result:
            number -= result
        else:
            number += result

    return number
