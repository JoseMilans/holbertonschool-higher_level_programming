#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0      
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    sum = 0
    str_len = len(roman_string)  
    for i in range(str_len):
        if i + 1 < str_len and roman[roman_string[i]] < roman[roman_string[i + 1]]:
            sum -= roman[roman_string[i]]
        else:
            sum += roman[roman_string[i]]   
    return sum
