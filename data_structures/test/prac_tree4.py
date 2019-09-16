"""
	MORE TREEEEEEES

"""

class Node:
	def __init__(self, value=None):
		self.value = value
		self.left = None
		self.right = None


class Binary_Tree:
	def __init__(self):
		self.root = None

	def add(self, value):

		# check if root is not null!
		if (self.root is None):
			self.root = Node(value)

		else:
			self._add(self.root, value)


	def _add(self, cur_node, value):

		# check values and comapre left and right
		if (value < cur_node.value):

			# check if left is empty
			if (cur_node.left is None):
				cur_node.left = Node(value)
			else:
				self._add(cur_node.left, value)

		elif(value > cur_node.value):
			# check if left is empty
			if (cur_node.right is None):
				cur_node.right = Node(value)
			else:
				self._add(cur_node.right, value)
		else:
			print(value, 'in tree already')	

	def print(self):

		# check if node is empty
		if (self.root is not None):
			# call herlper to help check ttreee
			self._print(self.root)
		else:
			print('tree is empty')

	def _print(self, cur_node):

		# check if node has a value. if so get ready to print it. :)
		if (cur_node is not None):

			#inorder (left, print, right)
			self._print(cur_node.left)
			print(cur_node.value)
			self._print(cur_node.right)

			# #postorder (left, right, print)
			# self._print(cur_node.left)
			# self._print(cur_node.right)
			# print(cur_node.value)

			# # preorder
			# print(cur_node.value)
			# self._print(cur_node.left)
			# self._print(cur_node.right)
			

def main():

	BTree = Binary_Tree()

	BTree.print()
	BTree.add(4)
	BTree.add(1)
	BTree.add(7)
	BTree.add(3)
	BTree.add(6)

	BTree.print()

if __name__ == '__main__':
	main()