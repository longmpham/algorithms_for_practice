"""
	Look and say sequence

	wiki:
	sequence = [1, 11, 21, 1211, 111221, 312211, 13112221, 1113213211, ...]

	ie. look_and_say(4) = 1211 <--- index 3

	To generate a member of the sequence from the previous member,
	read off the digits of the previous member, 
	counting the number of digits in groups of the same digit. 

	For example:

	1 is read off as "one 1" or 11.
	11 is read off as "two 1s" or 21.
	21 is read off as "one 2, then one 1" or 1211.
	1211 is read off as "one 1, one 2, then two 1s" or 111221.
	111221 is read off as "three 1s, two 2s, then one 1" or 312211.


"""


def look_and_say(n):
	# find the number to the nth number.

	if n <= 0 or n > 30: return '0'
	if n == 1:
		return '1'


	s = '1'
	count = 1

	while count < n:

		looking_at_index = 0
		counter = 1
		temp = ''
		# print('lenstr', len(s))
		for index in range(1, len(s)):
			# print('str =', s)
			# keep track of how many times you see the looking_at_index
			# print('looking at', s[looking_at_index])
			# print('comparing to index value,', s[index])
			if s[looking_at_index] == s[index]:
				counter += 1
				# print('counter:', counter)
				continue
			
			# the index values are now different! 
			# first add the new count + value
			# then iterate to the next one and reset counter
			temp += str(counter) + s[looking_at_index]
			looking_at_index = index
			counter = 1

			# print('counter:', counter)
		temp += str(counter) + str(s[looking_at_index])
		# we finished the string and counted occurrences. now append them all!
		s = temp
		count += 1
	return str(s)



print(look_and_say(4))



