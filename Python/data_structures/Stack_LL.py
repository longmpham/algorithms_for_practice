
class Node:
    
    def __init__(self, data):
        self.data = data
        self.next = None
        
class StackLL:
    
    def __init__(self):
        self.head = None
        
    def add(self, value):
        new_node = Node(value)
        # check if head empty
        if self.head == None:
            self.head = new_node
            return
        
        else:
            new_node.next = self.head
            self.head = new_node
            
    def pop(self):
        """Return the first element on the stack

        Returns:
            _type_: _description_
        """
        
        if self.head == None:
            print("nothing in stack")
            return
        # return first value and self.head.next points to the next node
        popped_node = self.head
        self.head = self.head.next
        # extra: the node we pop has nothing to point at
        popped_node.next = None
        
        return popped_node
    
    def display(self):
        
        if self.head == None:
            print("stack is empty")
            return
        
        current_node = self.head
        while current_node != None:
            print(f"{current_node.data}", end=">")
            current_node = current_node.next
        print("None")
        
    def peak(self):
        """returns the value at the top without removing it from stack
        """
        if self.head == None:
            print("nothing in the stack")
            return
        return self.head.data
        
        
my_stack = StackLL()
my_stack.display()
my_stack.add(1)
my_stack.add(2)
my_stack.display()
print(f"the top of the stack is {my_stack.peak()}")
my_stack.add(3)
my_stack.display()
my_stack.pop()
my_stack.display()
my_stack.pop()
my_stack.display()
my_stack.pop()
my_stack.display()