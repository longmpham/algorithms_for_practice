"""
	check if tree is has identical lefts and rights

			1
		2		2
	3	4		3	4

"""


class Tree_Node:
	def __init__(self, value=None, left=None, right=None):
		self.value = value
		self.left=left
		self.right=right


def is_tree_identical_left_and_right(root) -> bool:

	# base is the root is the only tree
	if root.left is None and root.right is None:
		return True

	return helper_function(root.left, root.right)


def helper_function(left, right):


	if left is None and right is None:
		return True
	if left is None or right is None:
		return False

	print('left:', left.value, 'right:', right.value, ' ==>', (left.value==right.value))

	if left.value == right.value:

		check1 = check2 = False

		# check left children
		if left.left is not None and right.left is not None:
			check1 = helper_function(left.left, right.left)
		elif left.left is None and right.left is None:
			return True

		# check right children
		if left.right is not None and right.right is not None:
			check2 = helper_function(left.right, right.right)
		elif left.right is None and right.right is None:
			return True

		return check1 and check2

	else:
		return False



if __name__ == '__main__': 


	# should be true
	root1 = Tree_Node(1)  
	root1.left = Tree_Node(2)  
	root1.right = Tree_Node(2)  
	root1.left.left = Tree_Node(3)  
	# root1.left.right = Tree_Node(4)  
	root1.right.left = Tree_Node(3)  
	root1.right.right = Tree_Node(4)
  

	# should be false
	root2 = Tree_Node(1)  
	root2.left = Tree_Node(2)  
	root2.right = Tree_Node(2)  
	root2.left.left = Tree_Node(3)  
	root2.left.right = Tree_Node(4)  
	root2.right.left = Tree_Node(4)  
	root2.right.right = Tree_Node(3)  
 

	print(is_tree_identical_left_and_right(root1))
	print('')
	print(is_tree_identical_left_and_right(root2))
