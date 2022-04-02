"""
	Find if trees are the same. Exactly.
"""


def is_tree_same_iterative(p: TreeNode, q: TreeNode) -> bool:

	if p is None and q is None:
		return True

	# check iteratively if the tree has values

	if p is not None and q is not None:
		while p.left is not None and q.left is not None:
			if p.val == q.val:
				# keep going
			else:
				return False




def is_tree_same_recursive(p: TreeNode, q: TreeNode) -> bool:
	"""
	stype: p and q are the TreeNodes
	rtype: return True / False if the trees are the same
	"""

	# see if trees are there. if they are empty, return true
	if p is None and q is None:
		return True

	# we then check that the tree has the same elements
	if p is not None and q is not None:
	    
		if p.val == q.val:
			same_left = self.is_tree_same_recursive(p.left, q.left)
			same_right = self.is_tree_same_recursive(p.right, q.right)

			if same_left and same_right:
				return True
			else:
				return False

	return False



def is_tree_same_stack(t1, t2)

	# save as a stack of numbers

	# pop off each pair

	# check if they are the same

	# if the same, move to the next pair

	# if not the same, return False

	# at the end when the stack is empty, return True IFF stacks are empty!