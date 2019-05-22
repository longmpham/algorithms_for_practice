"""
	find max depth of a tree
"""


class Tree_Node:

	def __init__(self, value=None, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def max_depth(root):


	if root is None:
		return 0

	if root is not None:
		return 1 + max(max_depth(root.left), max_depth(root.right))


if __name__ == '__main__': 



	root1 = Tree_Node(1)  
	root1.left = Tree_Node(2)  
	root1.right = Tree_Node(6)  
	root1.left.left = Tree_Node(3)  
	root1.left.right = Tree_Node(5)  
	root1.right.left = Tree_Node(7)  
	root1.right.right = Tree_Node(8)
	root1.left.left.left = Tree_Node(4)
	root1.right.right.right = Tree_Node(9)
	root1.right.right.right.right = Tree_Node(10)
  

	root2 = Tree_Node(1)  
	root2.left = Tree_Node(2)  
	root2.right = Tree_Node(2)  
	root2.left.left = Tree_Node(3)  
	root2.left.right = Tree_Node(4)  
	root2.right.left = Tree_Node(4)  
	root2.right.right = Tree_Node(3)  
 

	print(max_depth(root1))
	print('')
	print(max_depth(root2))
