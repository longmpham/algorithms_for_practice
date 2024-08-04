# assumes unique values only!

class Node:

    def __init__(self, value=None) -> None:
        self.value = value
        self.left = None
        self.right = None
        
class BTree:
    
    def __init__(self, root=None) -> None:
        self.root = None
        
    def add_node(self, value):
        # check if there is a root and if not add node
        if self.root == None:
            self.root = Node(value)
            return
        # Call recursive function to check the next node
        self._add_node(value, self.root)
        
    def _add_node(self, value, current_node):
        
        # check left if less, add it
        if value < current_node.value:
            if current_node.left == None:
                current_node.left = Node(value)
            else:
                self._add_node(value, current_node.left)
        # check if value is greater and if so, keep going
        elif value > current_node.value:
            if current_node.right == None:
                current_node.right = Node(value)
            else:
                self._add_node(value, current_node.right)
        else:
            print("the item is already in the tree")
            
    def print_tree(self):
        if self.root != None:
            self._print_tree(self.root)
        else:
            print('empty tree')
    
    def _print_tree(self, current_node):
        if current_node != None:
            # user can develop separate functions or just comment out
            # print in order
            self._print_tree(current_node.left)
            print(current_node.value)
            self._print_tree(current_node.right)
        
            # print post order(left, right, print)
            # self._print_tree(current_node.left)
            # self._print_tree(current_node.right)
            # print(current_node.value)
            
            # print pre order(print, left, right)
            # print(current_node.value)
            # self._print_tree(current_node.left)
            # self._print_tree(current_node.right)


mytree = BTree()
mytree.print_tree()

mytree.add_node(4)
mytree.add_node(7)
mytree.add_node(1)
mytree.add_node(1)
mytree.add_node(2)
mytree.add_node(6)
mytree.add_node(0)
mytree.add_node(9)
"""
        4
      /   \
     1     7
    / \   / \
   0   2 6   9

"""



mytree.print_tree()