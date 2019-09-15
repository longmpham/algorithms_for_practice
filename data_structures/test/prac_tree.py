"""
	practice rewriting tree
"""


class Node:
	def __init__(self, value=None):
		self.value = value
		self.left = None
		self.right = None

class BTree:
	def __init__(self, root=None):
		self.root = None
		
	def add(self, value):

		print('adding: ', value)
		# check if root node has a value. if not add it.
		if (self.root is None):
			self.root = Node(value)
		# otherwise, check the value in the helper function
		else:
			self._add(self.root, value)


	def _add(self, root, value):
		# we compare values
		if (value < root.value):
			# go left and check left node
			if (root.left is None):
				root.left = Node(value)
			else:
				# recursive function to keep going left.
				self._add(root.left, value)

		# now check right
		elif (value > root.value):
			# check if value there
			if (root.right is None):
				root.right = Node(value)
			else:
				self._add(root.right, value)

		# value already exists
		else:
			print(value, 'in tree already.')


	def print(self):

		if (self.root is not None):
			# go left
			self._print(self.root)


	def _print(self, root):
		if (root is not None):
			# go left
			self._print(root.left)
			print(root.value)
			# go right
			self._print(root.right)



def main():


	Tree = BTree()
	Tree.print()

	Tree.add(4)
	Tree.add(7)
	Tree.add(1)
	Tree.add(1)

	Tree.print()


if __name__ == '__main__':
	main()