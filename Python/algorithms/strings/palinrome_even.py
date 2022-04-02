"""
	Create a palindrome checker.
	ie. string = Dog  palindrome = God
"""


def is_palindrome(string):

	# return if no string is provided.
	if not string:
		return print('empty string')

	# if string length = 1, it's to some degree a palindrome in itself.
	if len(string) == 1:
		return True
	
	odd = False
	# check if the string length is odd or even.
	if len(string) % 2 == 0:
		halfpoint = len(string)//2
	else:
		halfpoint = len(string)//2
		odd = True
	# print('halfpoint: {}'.format(halfpoint)) #works!


	checker = []

	letter = 0

	# go up until half point.
	while letter < halfpoint:
		checker.append(string[letter])
		letter += 1

	# print(checker)
	if odd:
		letter = halfpoint + 1
	else:
		letter = halfpoint
	# print ('first letter length: ', letter, len(string))
	# check dictionairy if it matches the second half of word
	while letter < len(string):
		if checker.pop() == string[letter]:
			# print(checker)
			letter += 1
		else:
			return False

	if not checker:
		return True



string = ['pooop', 'poop', 'dog', 'cat', 'me', 'ordro', '', 'i', 'halblah', 'juiiuj']

for s in string:
	print(is_palindrome(s))