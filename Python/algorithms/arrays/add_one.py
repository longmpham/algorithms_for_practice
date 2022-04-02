"""
	given an number indexed into an array, ie. # 345 -> [3,4,5] with the MSB on the left, and the LSB on the right, add 1 to the number.

	Tip: think about edge cases!
"""


def add_one(digits):
    if len(digits) == 0:
        return [0]      
    
    carry = 1
    size = len(digits)
    #new_array = [0] * (size) + 1
    
    while 0 < size:
        # add 1 to the last element of the array.
        digits[size-1] += carry
        if digits[size-1] >= 10:
            digits[size-1] = digits[size-1] % 10
            carry = 1
        else:
            carry = 0
        size -= 1
        
    if carry == 1:
        digits.insert(0,carry)
        return digits
    else:
        return digits


def add_one_early_stop(digits):
    if len(digits) == 0:
        return [0]      
    
    carry = 1
    size = len(digits)
    #new_array = [0] * (size) + 1
    stop = 0
    
    while 0 < size:
        # add 1 to the last element of the array.
        digits[size-1] += carry
        
        # we can stop early if we dont need to add carry anymore!
        if stop == 1 and digits[size-1] < 10:
            return digits
        
        if digits[size-1] >= 10:
            digits[size-1] = digits[size-1] % 10
            carry = 1
            stop = 1
        else:
            carry = 0
        size -= 1
        stop = 1
        
    if carry == 1:
        digits.insert(0,carry)
        return digits
    else:
        return digits




digits1 = [3,4,5]
digits2 = [1,0,0,0,0]
digits3 = [9,9,9]

print(add_one(digits3))