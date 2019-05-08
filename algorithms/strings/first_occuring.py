"""
	return the first occuring character's index or letter in a string
	
"""


def first_occuring(str):

	# if needed, use all uppers. otherwise, if caps is necessary, take out.
	str = str.upper()

	# create a letter map that we have seen while we go through the string
	letter_map = {}

	for letter in str:
		if letter not in letter_map:
			# add the letter in the map.
			letter_map[letter] = 1
		else:
			# we found one!
			# letter_map[letter] += 1
			# print(letter_map)
			return letter

	return 'None found in the string'


string = 'ABCDA'

print(first_occuring(string))

