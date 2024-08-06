

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        
    def append(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return
        
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
        current_node.next = new_node

    def preppend(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
    
    def search(self, value):
        if self.head == None:
            return
        index = 0
        current_node = self.head
        while current_node is not None:
            if current_node.value == value:
                print(f"found {value} at index: {index}")
                return True
            index+=1
            current_node = current_node.next
        print(f"Could not find {value}")
        return False
    
    
    def display(self):
        if self.head == None:
            print("nothing to print")
            return
        current_node = self.head
        while current_node is not None:
            print(current_node.value, end=">")
            current_node = current_node.next
        print("None")
    
    def insert(self,value,index):
        if self.head == None and index == 0:
            self.head = Node(value)
        if self.head == None:
            return
        
        current_node = self.head
        list_counter = 0
        while current_node is not None and list_counter < index-1: 
            list_counter+=1
            current_node = current_node.next
        print(f"list counter: {list_counter} and index: {index}")
        
        if list_counter == index-1 and current_node is not None:
            new_node = Node(value)
            new_node.next = current_node.next
            current_node.next = new_node
            return
        elif list_counter == index-1 and current_node is None:
            new_node = Node(value)
            current_node = new_node
        else:
            print("unable to insert")
            return False
        
        
myll = LinkedList()
myll.display()
myll.append(2)
myll.append(3)
myll.append(1)
myll.display()
myll.preppend(9)
myll.append(4)
myll.display()
myll.search(3)
myll.search(9)
myll.search(4)
myll.insert(7,2)
myll.display()
myll.insert(6,6)
myll.display()
