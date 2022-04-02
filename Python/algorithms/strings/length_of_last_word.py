"""
	Length of last word

	ex. "" = 0
		" " = 0
		"a " = 1
		" a" = 1
		"a a" = 1
		"hello world" = 5
"""

# this is time complexity O(n) Space complexity O(n)
def length_of_last_word(string):

	if string == '':
		return 0

	if string == ' ':
		return 0

	split_string = string.split(' ')
	size_of_splits = len(split_string)
	count = 0

	while count < size_of_splits:
		if split_string[size_of_splits-1] == '':
			size_of_splits -= 1
		else:
			return len(split_string[size_of_splits-1])

	return 0


# this is time complexity O(n) Space complexity O(1)
def length_of_last_word_v2(string):
	if string == '':
		return 0

	if string == ' ':
		return 0

	counter = 0
	size = len(string)
	while 0 < size:
		if string[size-1] == ' ':
			if counter > 0:
				return counter
			continue
		else:
			counter += 1
			size -= 1
	return 0


string = 'a a'
print(length_of_last_word_v2(string))