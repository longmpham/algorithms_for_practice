"""
	Sorted array to BST
"""

class Tree_Node:
	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

class My_Failed_Solution:

	def sorted_array_to_BST(self, array):

		# base if empty!
		if not array:
			print('empty array')
			return

		if len(array) == 1:
			return array

		# check if even or odd
		if len(array) % 2 == 0:
			# even array
			print('even array!')
		else:
			# odd array
			print('odd array')

		half_point = len(array)//2
		root_key = array.pop(half_point)

		bot_array = array[0:half_point]
		top_array = array[half_point:len(array)]

		print(bot_array)
		print(top_array)
		print(root_key)


		# start inserting !
		print('inserting now!')
		root = Tree_Node(root_key)

		while bot_array:
			print(bot_array)
			self._insert(root, bot_array.pop())

		while top_array:
			print(top_array)
			self._insert(root, top_array.pop())

		print(bot_array)
		print(top_array)


		print('printing tree...')
		print(self.in_order_tree_traversal(root))

	def _insert(self, root, key):

		# first check the value of the current root to decide where to go.
		if key < root.value:
			# we go left
			if root.left is None:
				root.left = Tree_Node(key)
			else:
				return self._insert(root.left, key)

		if key > root.value:
			# we're greater!

			if root.right is None:
				root.right = Tree_Node(key)
			else:
				return self._insert(root.right, key)

	def in_order_tree_traversal(self, root):

		if root is None:
			return

		if root is not None:
			
			if root.left is not None:
				self.in_order_tree_traversal(root.left)

			print(root.value)

			if root.right is not None:
				self.in_order_tree_traversal(root.right)


class Right_Solution:
	def sortedArrayToBST(self, num):
		if not num:
			return None

		mid = len(num) // 2

		root = Tree_Node(num[mid])
		root.left = self.sortedArrayToBST(num[:mid])
		root.right = self.sortedArrayToBST(num[mid+1:])

		return root

	def in_order_tree_traversal(self, root):

		if root is None:
			return

		if root is not None:
			
			if root.left is not None:
				self.in_order_tree_traversal(root.left)

			print(root.value)

			if root.right is not None:
				self.in_order_tree_traversal(root.right)


if __name__ == '__main__':

	array = [-10,-3,0,5,9]
	fail = My_Failed_Solution()
	print(fail.sorted_array_to_BST(array))


	solution = Right_Solution()
	root = solution.sortedArrayToBST(array)

	print(solution.in_order_tree_traversal(root))
