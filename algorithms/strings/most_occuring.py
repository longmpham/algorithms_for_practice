"""
	return the most occuring character's index or letter in a string
	
"""



def most_occuring(str):

	seen_letters = {}

	for letter in str:
		if letter not in seen_letters:
			seen_letters[letter] = 1
		else:
			seen_letters[letter] += 1

	print('unsorted:', seen_letters)

	seen_letters = sorted(seen_letters.items(), key=lambda x: x[1])

	print('sorted:', seen_letters)

	return seen_letters[-1]



string = 'ABBBCDA'

print(most_occuring(string))

