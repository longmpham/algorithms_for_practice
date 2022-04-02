"""
	delete an item(s) from an unsorted linked list

"""



def delete_duplicates(linked_list):
    if head is None:
        return None
    
    current_node = head
    
    # curr 				curr.next
    # curr.val = 1		curr.val = 2
    # [1] 		->		 [2] 		->		 [None]
    # 
    # if current == the next node, they are the same. move the pointer to the next and skip the same node
    # if current not the same -> iterate next! current = current.next
    
    while current_node.next:
        
        if current_node.val == current_node.next.val:
            # skip 
            current_node.next = current_node.next.next
        else:
            # dont skip, check the next one
            current_node = current_node.next

    return head