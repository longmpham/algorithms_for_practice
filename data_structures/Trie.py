"""
	Implement a basic Trie (Tree that holds chars to search for words)
"""


class TrieNode:
	def __init__(self):
		self.children = {}


class TrieWithNodes:
	def __init__(self):
		self.root = TrieNode()


	def add(self, word):
		current_pointer = self.root

		for character in word:
			if character not in current_pointer.children:
				current_pointer.children[character] = TrieNode()
				print('adding', character)
			current_pointer = current_pointer.children[character]

		current_pointer.children['*'] = True


	def search(self, word):
		current_pointer = self.root

		for character in word:
			print(character)
			if character not in current_pointer.children:
				return False
			current_pointer = current_pointer.children[character]

		if '*' in current_pointer.children:	
			return True
		else:
			return False


	def contains(self, sub_word):
		current_pointer = self.root

		for character in sub_word:
			print(character)
			if character not in current_pointer.children:
				return False
			current_pointer = current_pointer.children[character]
		return True





# contains no TrieNode class
class Trie:
	def __init__(self):
		self.root = {}


	def add(self, word):
		current_pointer = self.root

		for character in word:
			# if the character doesn't exist, place an empty dict
			if character not in current_pointer:
				current_pointer[character] = {}

			# then fill the dict
			current_pointer = current_pointer[character]

		# finally, add a * at the end to signify the end of a word
		current_pointer['*'] = True

	def search(self, word):
		current_pointer = self.root

		for character in word:
			# if the character doesn't exist, we return false!
			if character not in current_pointer:
				return False
			current_pointer = current_pointer[character]

		if '*' in current_pointer:
			return True
		else:
			return False

	def contains(self, sub_word):
		current_pointer = self.root

		for character in sub_word:
			if character not in current_pointer:
				return False
			# else we go next!
			current_pointer = current_pointer[character]

		return True



if __name__ == '__main__':


	dictionary = TrieWithNodes()

	dictionary.add('hello')
	dictionary.add('hi')
	dictionary.add('hey')

	# TRUE
	print(dictionary.search('hello'))
	print(dictionary.search('hi'))
	print(dictionary.search('hey'))
	print()

	# FALSE
	print(dictionary.search('yo'))
	print(dictionary.search('imbad'))
	print()

	# TRUE
	print(dictionary.contains('h'))
	print(dictionary.contains('hell'))
	print()

	# FALSE
	print(dictionary.contains('ll'))
	print(dictionary.contains('me'))
	print()