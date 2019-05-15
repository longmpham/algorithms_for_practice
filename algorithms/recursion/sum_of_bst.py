"""
	sum of a BST
"""

class Tree_Node:
	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = None
		self.right = None



def sum_of_bst(root, new_sum):

	# check for empty root
	if root is None:
		return new_sum


	# not an empty root! begin search

	if root is not None:
		new_sum += root.value
		print(new_sum)
		if root.left is not None:
			# add the left
			new_sum = sum_of_bst(root.left, new_sum)
			# print(new_sum)

		if root.right is not None:
			# add the right
			new_sum = sum_of_bst(root.right, new_sum)
			# print(new_sum)

	return new_sum



if __name__ == '__main__': 
	"""
				1
			2		3	
		4	5		

	"""


	root1 = Tree_Node(1)  
	root1.left = Tree_Node(2)  
	root1.right = Tree_Node(3)  
	root1.left.left = Tree_Node(4)  
	root1.left.right = Tree_Node(5)  
  
	root2 = Tree_Node(1)  
	root2.left = Tree_Node(2)  
	root2.right = Tree_Node(3)  
	root2.left.left = Tree_Node(4)  
	root2.left.right = Tree_Node(5)  
  
	new_sum = 0

	sum_of_bst(root1, new_sum)
