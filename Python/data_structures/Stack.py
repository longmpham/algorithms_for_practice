"""
	Create a stack data structure
"""


class Stack:

	def __init__(self, items=[]):
		self.items = []

	def add(self, item):
		self.items.append(item)

	def pop(self):
		if self.items:
			return self.items.pop()
		else:
			print('empty stack')
			return

	def peek(self):
		return self.items[-1]

	def deleteAll(self):
		while not self.items:
			self.items.pop()

	def getStack(self):
		return self.items

	# def sort




def main():
	My_Stack = Stack()

	My_Stack.add(4)
	My_Stack.add(5)

	print(My_Stack.getStack())

	# now pop all
	My_Stack.pop()
	My_Stack.pop()
	My_Stack.pop()


if __name__ == '__main__':
	main()