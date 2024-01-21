#!/usr/bin/python3

def roman_to_int(roman_string):

    if not roman_string or type(roman_string) != str:
        return 0
    roman_map = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    total_value = 0
    for i in range(len(roman_strin))g:
        if i > 0 and roman_map[roman_string[i]] > roman_map[roman_string[i - 1]]:
            total_value += roman_map[roman_string[i]] - 2 * \
                roman_map[roman_string[i - 1]]
        else:
            total_value += roman_map[roman_string[i]]
    return total_value
