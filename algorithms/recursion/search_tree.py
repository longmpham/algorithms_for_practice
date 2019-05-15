"""
	Search for an element in a tree

"""


class Tree_Node:

	def __init__(self, value, left=None, right=None):
		self.value = value
		self.left = None
		self.right = None



def search_tree(root, key) -> bool:

	if root is None:
		return False

	if root.value == key:
		return True

	if root is not None:

		found = False
		# search left
		if root.left is not None:
			found = search_tree(root.left, key)
		# search right
		if root.right is not None:
			found = search_tree(root.right, key)

		return found


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
  
	key = 6

	if search_tree(root1,key):
		print('yay!')
	else:
		print('boo!')