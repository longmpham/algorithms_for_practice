"""
	list from bottom of of a binary tree
	
	For example:
	Given binary tree [3,9,20,null,null,15,7],
	    3
	   / \
	  9  20
	    /  \
	   15   7

	answer:
   	[
  		[15,7],
  		[9,20],
  		[3]
	]
"""

class Tree_Node:

	def __init__(self, value=None, left=None, right=None):
		self.value = value
		self.left = left
		self.right = right


def bottom_up_tree_traversal(root: Tree_Node):
	"""
	rtype: List of lists
	"""

	dfs_array = []

	if root is None:
		return dfs_array
	else:
		# call a helper to help with our bfs

		_bottom_up_tree_traversal(root, 0, dfs_array)
		return dfs_array

def _bottom_up_tree_traversal(root: Tree_Node, level, dfs_array):

	if root is None: return

	if root is not None:
		
		# if we're at a new level, add a list (within the list!)
		if len(dfs_array) < level + 1:
			dfs_array.insert(0, [])
		
		# add the value to the list in the level
		dfs_array[-(level + 1)].append(root.value)

		# call for the next layer
		_bottom_up_tree_traversal(root.left, level + 1, dfs_array)
		_bottom_up_tree_traversal(root.right, level + 1, dfs_array)






if __name__ == '__main__': 


	# should print [ [10], [4,9], [3,5,7,8], [2,6], [1] ]
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
  


 

	print(bottom_up_tree_traversal(root1))