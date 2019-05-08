"""
	roman numerals
"""

def convert_roman_to_integer(str):
    result = 0
    last = 1001
    numerals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for x in s:

        # find result in our look up table
        num = numerals[x]
        result += num
        if num > last:
            result -= last*2
        last = num
    return result