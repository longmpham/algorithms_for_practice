"""
	add 2 binary numbers
"""



def add_binary(a,b):
	# base -> strings are empty
	if len(a) == 0: return b
	if len(b) == 0: return a
	if len(a) == 0 and len(b) == 0: return 0
    
	# figure out which one is longer
	if len(a) < len(b):
		# b is longer, set a such that a is always longer for later.
		temp = a
		a = b
		b = temp
        
	# now make b equal to a in length
	while len(b) is not len(a):
		b = '0' + str(b)

	# need some helper vars
	size = len(a)
	carry = 0
	total = ''

	while 0 < size:
		# add the digits now
		digit_sum = int(a[size-1]) + int(b[size-1]) + int(carry)

		# if there's an overflow, we have to deal with it
		if digit_sum >= 2:
			digit_sum = digit_sum % 2
			carry = 1
		else:
			carry = 0

		# append as first index of new total
		total = str(digit_sum) + total
		size -= 1

	if carry == 1:
		return '1' + total
	else:
		return total





a = '1111'
b = '11'


print(add_binary(a,b))