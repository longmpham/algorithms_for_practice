"""
	is the tree given symmetric?

	ie. 

			1
		2		2			== TRUE
	3	4		4	3   		

"""

class Tree_Node:

	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def is_tree_symmetric(root) -> bool:

	if root is None: return True


	# check if the non-zero root has values
	if root is not None:
		return helper_function(root.left, root.right)




def helper_function(left, right):
	"""
	search from the outside and then search within 
	"""

	# if both are null, its true.
	# if either or null, its false
	if left is None and right is None:
		return True
	if left is None or right is None:
		return False

	print('left:', left.value, 'right:', right.value, ' ==>', (left.value==right.value))

	# if either has values, we check if the values match!
	if left.value == right.value:
		check1 = False
		check2 = False
		# keep checking with pointers point left and pointers pointing right until its exhausted.
		if left.left is not None and right.right is not None:
			check1 = helper_function(left.left, right.right)
		elif left.left is None and right.right is None:
			check1 = True


		# then check with pointers pointing right and pointers pointing left until its exhausted.
		if left.right is not None and right.left is not None:
			check2 = helper_function(left.right, right.left)
		elif left.right is None and right.left is None:
			check2 = True

		return check1 and check2

	else:
		return False






if __name__ == '__main__': 

	"""
			1
		2		2
	3	4		3	4
	"""
	root1 = Tree_Node(1)  
	root1.left = Tree_Node(2)  
	root1.right = Tree_Node(2)  
	root1.left.left = Tree_Node(3)  
	root1.left.right = Tree_Node(4)  
	root1.right.left = Tree_Node(3)  
	root1.right.right = Tree_Node(4)
  


	root2 = Tree_Node(1)  
	root2.left = Tree_Node(2)  
	root2.right = Tree_Node(2)  
	root2.left.left = Tree_Node(3)  
	root2.left.right = Tree_Node(4)  
	root2.right.left = Tree_Node(4)  
	root2.right.right = Tree_Node(3)  
 

	print(is_tree_symmetric(root1))
	print()
	print(is_tree_symmetric(root2))
