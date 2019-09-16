"""
	another tree practice run

"""


class Node: 
	def __init__(self, value=None):
		self.value = value
		self.left = None
		self.right = None

class Binary_Tree: 
	def __init__(self, root=None):
		self.root = None

	def add(self, value):

		# check if node is empty
		if(self.root is None):
			self.root = Node(value)

		else:
			self._add(self.root, value)



	def _add(self, cur_node, value):

		# check values to go left or right. go left first.
		if (value < cur_node.value):

			# go left! 
			if (cur_node.left is None):

				# add node
				cur_node.left = Node(value)

			else:
				self._add(cur_node.left, value)

		# check right
		elif (value > cur_node.value): 
			if (cur_node.right is None):
				cur_node.right = Node(value)
			else:
				self._add(cur_node.right, value)

		else:
			print(value, 'already in tree')

	def print(self):

		# check if node has value
		if (self.root is not None):

			# go left.
			self._print(self.root)

		else:
			print('no tree')


	def _print(self, cur_node):

		if (cur_node is not None):


			print(cur_node.value)

			# keep going left until it is none.
			self._print(cur_node.left)

			# print out right too.
			self._print(cur_node.right)





def main():


	Tree = Binary_Tree()
	Tree.print()

	Tree.add(4)
	Tree.add(7)
	Tree.add(1)
	Tree.add(2)
	Tree.add(5)
	Tree.add(6)
	Tree.add(8)
	Tree.add(3)
	Tree.add(9)

	Tree.print()


if __name__ == '__main__':
	main()