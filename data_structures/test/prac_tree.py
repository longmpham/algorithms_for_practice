

class Node:
	def __init__ (self, value=None):
		self.value = value
		self.left = None
		self.right = None


class BTree:
	def __init__ (self, node=None):
		self.node = node

	def add(self, value):

		# check if node has value
		# if not add it

		print('attempting to add: ', value)

		if (self.node is None):
			self.node = Node(value)
		else:
			self._add(self.node, value)


	def _add(self, cur_node, value):

		# compare values to go left or right
		if (value < cur_node.value):

			# if left is empty add it. otherwise search further
			if (cur_node.left is None):
				cur_node.left = Node(value)
			else:
				self._add(cur_node.left, value)

		elif (value > cur_node.value):
			# if right is empty add it. otherwise search further
			if (cur_node.right is None):
				cur_node.right = Node(value)
			else:
				self._add(cur_node.right, value)
		
		else:
			print(value, 'already in tree!')


	def print(self):
		#start checking the node if it has a value!
		if(self.node is not None):
			self._print(self.node)
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