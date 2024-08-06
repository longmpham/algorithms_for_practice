class Node: 
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None
        
class BTreeWhile:
    def __init__(self, value=None):
        self.root = value
        
    def add_node(self, value):
        # check if root is none and add if so
        new_node = Node(value)
        if self.root == None:
            self.root = new_node
            return
        
        current_node = self.root
        while True:
            if value < current_node.value:
                if current_node.left == None:
                    current_node.left = new_node
                    return
                else:
                    current_node = current_node.left
            elif value > current_node.value:
                if current_node.right == None:
                    current_node.right = new_node
                    return
                else:
                    current_node = current_node.right      
            else:
                print("value already exists")
                return
            
    def print_in_order(self, node):
        if node != None:
            self.print_in_order(node.left)
            print(node.value, end=" ")
            self.print_in_order(node.right)
    def print_post_order(self, node):
        if node != None:
            self.print_post_order(node.left)
            self.print_post_order(node.right)
            print(node.value, end=" ")
    def print_pre_order(self, node):
        if node != None:
            print(node.value, end=" ")
            self.print_pre_order(node.left)
            self.print_pre_order(node.right)
            
    def print_tree(self):
    
        if self.root == None:
            print("empty tree")
            return
        user_input = input("i=inorder, p=postorder, pp=preorder: ")
        if user_input == "i":
            self.print_in_order(self.root)
        elif user_input == "p":
            self.print_post_order(self.root)
        elif user_input == "pp":
            self.print_pre_order(self.root)
        else:
            print("not a correct input")
            
mytree = BTreeWhile()
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

In-order: 0, 1, 2, 4, 6, 7, 9
Pre-order: 4, 1, 0, 2, 7, 6, 9
Post-order: 0, 2, 1, 6, 9, 7, 4
"""



mytree.print_tree()