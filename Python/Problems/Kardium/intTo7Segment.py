def encode(value=0):

	# base condition: non negative and does not exceed 9999
	if (value < 0 or value > 9999):
		return 0x7F7FFD67

	# base condition: no decimals
	if not isinstance(value, int):
		return 0x7F7FFD67


	# encoder for 7-segment display
	intToCode={0:0x02,1:0x67,2:0x48,3:0x60,4:0x25,5:0x30,6:0x10,7:0x66,8:0x00,9:0x24,-1:0x7f}

	# base output: prints 0
	output=0x7f7f7f02

	digit = value % 10
	for i in range(4):

		# add in the number from the left and push numbers out on the right. 
		output= (intToCode[digit] << 24) + (output >> 8)

		# parse the next digit
		value  = value // 10
		if value != 0:
			digit = value % 10
		else:
			digit = -1

	# truncate output to match specification for 4 bytes
	return output & 0xffffffff

print(hex(encode(123)))