
class Node: 
    def __init__(self, data) -> None:
        self.data = data
        self.next = None
        
class Q_LL:
    
    def __init__(self, data = None) -> None:
        self.data = data
        self.head = None
        
    def q(self, value) -> None:
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            return
        # add new node to the beginning
        new_node.next = self.head
        self.head = new_node
        
    def dq(self) -> Node:
        # 3 scenarios: empty, only the head, or more than just 1

        # empty:
        if self.head == None:
            print("nothing in q")
            return
        
        # just the head:
        if self.head.next == None:
            data = self.head.data
            self.head = None
            return data
        
        # more than 1
        current_node = self.head.next
        previous_node = self.head
        while current_node.next != None:
            previous_node = previous_node.next
            current_node = current_node.next
        data = current_node.data
        previous_node.next = None
        return data
    
    def display(self) -> None:
        if self.head == None:
            print("q is empty")
            return
        current_node = self.head
        while current_node != None:
            print(f"{current_node.data}", end= ">")
            current_node = current_node.next
        print("None")
        
        
        
my_q_ll = Q_LL()
my_q_ll.display()
my_q_ll.q(1)
my_q_ll.q(2)
my_q_ll.q(3)
my_q_ll.display()
print(f"dequeing the first entry in the q: {my_q_ll.dq()}")
my_q_ll.display()
print(f"dequeing the first entry in the q: {my_q_ll.dq()}")
my_q_ll.display()
print(f"dequeing the first entry in the q: {my_q_ll.dq()}")
my_q_ll.display()
