"""
	Creating my first class (not really...)
"""


class Person:

	# python requires 'self' as the object.
	def __init__(self, name, age, phrase):
		self.name = name
		self.age = age
		self.phrase = phrase

	def print_phrase(self):
		print(self.phrase)


def main():

	Long = Person('long', 25, 'im the best')
	Long.print_phrase()


if __name__ == '__main__':
	main()