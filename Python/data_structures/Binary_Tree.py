"""
	Create your first Binary Tree!
"""


# Create a Node class to have data + 2 children
class Node: 

	def __init__(self, value=None):

		self.value=value
		self.left_node=None
		self.right_node=None


# Create your Binary Tree!
class Binary_Tree:

	def __init__(self, root=None):
		self.root = None

	def add_node(self, value):

		# if no root add the root.
		if self.root is None:
			self.root = Node(value)
		else:
			self._add_node(value, self.root)

	def _add_node(self, value, current_node):

		# first we check left. if no value, we insert there.
		# else we go further.
		if value < current_node.value:

			if current_node.left_node is None:
				current_node.left_node = Node(value)
			else:
				self._add_node(value, current_node.left_node)

		# the current value is greater
		elif value > current_node.value:

			if current_node.right_node is None:
				current_node.right_node = Node(value)
			else:
				self._add_node(value, current_node.right_node)

		# the current node is equal
		else:
			print('value already in tree')


	def print_tree(self):
		if self.root is not None:
			self._print_tree(self.root)
		else:
			print('empty tree')

	def _print_tree(self, current_node):
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

	def tree_height(self):
		if self.root is not None:
			height = 0
			self._tree_height(self.root, height)
		else:
			print('empty tree')

	def _tree_height(self, current_node, height):
		if current_node is not None:
			height += 1
			self._tree_height(current_node.left_node, height)
			self._tree_height(current_node.right_node, height)





def main():


	Tree = Binary_Tree()
	Tree.print_tree()

	Tree.add_node(4)
	Tree.add_node(7)
	Tree.add_node(1)
	Tree.add_node(1)

	Tree.print_tree()


if __name__ == '__main__':
	main()