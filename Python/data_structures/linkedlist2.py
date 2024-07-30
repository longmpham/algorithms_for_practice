

# Create a Node class
class Node:
    # define the constructor 
    def __init__(self, value=None):
        self.value = value
        self.next = None # This is your "pointer" to the next node
        
class LinkedList:
    # define the constructor which creates the head of your LL
    def __init__(self):
        self.head = None
        
    # define a way to append to the LL
    def append(self, value):
        new_node = Node(value)
        
        # base case, its the first item in the list
        if (self.head == None):
            self.head = new_node
            return
        
        # if its not the base case, now we have to check until we get to the end of the list.
        # the last item should point to None
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        # finally, the node finds a node's pointer which points to None
        current_node.next = new_node
    
    def prepend(self, value):
        current_node = Node(value)
        
        # set the new node and point to the head
        current_node.next = self.head
        
        # reset the head to the new node
        self.head = current_node
        
        
    def display(self):
        if self.head == None:
            print("nothing to show")
            return
        
        current_node = self.head
        while current_node is not None:
            print(f"{current_node.value}", end="->") # using arrows with "end" so that it shows as an "LL"
            current_node = current_node.next
        # finally print None at the end of the LL
        print("None")
        
    # create a search method to find an element. If none are found, return False. If found, print index and return True
    def search(self, value):
        if self.head == None: return
        index = 0
        current_node = self.head
        
        # base: its just the head and length = 1
        if current_node.value == value:
            print(f"{value} was found at index: {index}")
            return True
        
        # base: its anywhere but the head
        while current_node.value != value and current_node.next is not None:
            current_node = current_node.next
            index += 1
        # if found return, else false
        if current_node.value == value:
            print(f"{value} was found at index: {index}")
            return True
        print(f"{value} was not found")
        return False
        
        
# Test LL
myLL = LinkedList()
myLL.display() 
myLL.append(1) 
myLL.append(3) 
myLL.append(2)
myLL.display() 
myLL.search(2)
myLL.search(3)
myLL.search(8)
myLL.append(4)
myLL.display()
myLL.search(4)