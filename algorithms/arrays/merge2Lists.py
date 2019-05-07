"""
	merge 2 sorted linked lists
	assuming they are both sorted, and have non-zero values, and have elements

	l1 = [1,3,4] , l2 = [1,2,4], ans = [1,1,2,3,4,4]

"""

def mergeTwoLists(l1, l2):

    if not l1: return l2
    if not l2: return l1

    count = 0
    new_list = []

    #reverse second list to pop (maybe bad)
    reversel2 = l2[::-1]

    while(reversel2[-1] < l1[0]):
        new_list.append(reversel2.pop())
        if not reversel2: break

    new_list.append(l1[0])
    count = 1

    while count < len(l1) or count < len(l2):
        
        if not reversel2:
            new_list.append(l1[count])
            count += 1
            if count == len(l1): break
        elif count >= len(l1):
            new_list.append(reversel2.pop())
            count += 1
        # if second list has item same, append that first.
        elif l1[count] >= reversel2[-1]:
            new_list.append(reversel2.pop())
        else:
            new_list.append(l1[count])
            count += 1
    return new_list


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        print(x)

# from leet code, they use overrided ops and stuff...
def mergeTwoLinkedLists(l1, l2):
        # create new linkedlist to merge 2 linkedlists
        new_list = ListNode(0)
        
        # create an iterator node
        current = ListNode(0)

        print('\n')
        
        # set the new list to be the current's first spot location
        new_list = current

        # go until linkedlist of l1 and l2 == none due to linked list nature
        while(l1 and l2):

            if(l1 < l2):
                current.next = l1
                l1 = l1.next
                
            # else l2val > l1 val!
            else:
                current.next = l2
                l2 = l2.next

            # increment the linkedlist
            current = current.next
            
        # if 1 of the lists are empty, append the rest (assuming its sorted!!!)
        current.next = l1 or l2
        
        return new_list.next


l1 = [5,7,8,9,10]
l2 = [1,3,4]
print(mergeTwoLists(l1,l2))



# cur1 = l1 = ListNode(0)
# l1 = l1.next
# l1 = ListNode(2)
# l1 = l1.next
# l1 = ListNode(4)
# l1 = l1.next
# l1 = ListNode(6)
# l1 = l1.next

# cur2 = l2 = ListNode(1)
# l2 = l2.next
# l2 = ListNode(3)
# l2 = l2.next
# l2 = ListNode(5)
# l2 = l2.next
# l2 = ListNode(7)
# l2 = l2.next


# print(mergeTwoLinkedLists(cur1,cur2))
