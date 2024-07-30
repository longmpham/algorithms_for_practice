"""
	Create a palindrome checker.
	ie. string = racecar
"""


def is_palindrome(string):

	# first check if the string length is odd or even. if its even, it can never be a palindrome
	if len(string) % 2 == 0:
		return False

	# if string length = 1, it's to some degree a palindrome in itself.
	if len(string) == 1:
		return True

	# now strings have to be 3 or more and strings are odd number lengths.

	halfpoint = len(string)//2 + 1
	# print('halfpoint: {}'.format(halfpoint)) #works!


	checker = []

	letter = 0

	# go up until half point.
	while letter < halfpoint - 1:
		checker.append(string[letter])
		letter += 1

	# print(checker)
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



string = ['pooop', 'poop', 'dog', 'cat', 'me', 'ordro']

for s in string:
	print(is_palindrome(s))