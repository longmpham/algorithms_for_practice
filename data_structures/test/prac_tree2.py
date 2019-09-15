"""
	another round of b trees
"""

class Node:
	def __init__ (self, value=None):
		self.value = value
		self.left = None
		self.right = None

class BTree: 
	def __init__(self, root=None):
		self.root = None

	def add(self, value):

		# check if node has a value
		if (self.root is None):
			self.root = Node(value)
		# else go to next node
		else:
			self._add(self.root, value)

	def _add(self, cur_node, value):

		# check values to go left or right
		if (value < cur_node.value):
			# check if left is none or not

			if(cur_node.left is None):
				cur_node.left = Node(value)
			else:
				self._add(cur_node.left, value)

		elif (value > cur_node.value):

			if(cur_node.right is None):
				cur_node.right = Node(value)
			else:
				self._add(cur_node.right, value)

		else:
			print(value, 'is already in tree')


	def print(self):

		if (self.root is not None):
			# go left until it is!
			self._print(self.root)
		else:
			print('no tree')

	def _print(self, root):

		if(root is not None):
			self._print(root.left)
			print(root.value)
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