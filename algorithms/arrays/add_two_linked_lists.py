"""
	add 2 linked lists together like old fashion math. they are non negative and stored backwards
	assume they are the same size
	ie. L1 = 2 -> 4 -> 3
		L2 = 5 -> 6 -> 4

		342
	+	465
		===
		807	



		NOT WORKING. SKIP. LLs dont work.

"""

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
        # print(x)

def add_two_numbers_linked_list(l1,l2):
	
	# pointers to linked_lists
	start1 = list1_pointer = l1
	start2 = list2_pointer = l2

	# new linked_list
	start3 = new_linked_list = ListNode(0)


	# 	1s = l1 + l2 + c
	# 	10s= l1 + l2 + c
	#	100s = l1 + l2 + c
	#	...
	temp_total = 0
	carry = 0

	while list1_pointer != None or list2_pointer != None:
		print('not none!')
		if list1_pointer != None and list2_pointer != None:
			temp_total += list1_pointer.val + list2_pointer.val + carry
			print('total:', temp_total)
			if temp_total % 10 == 0:
				carry = 1
			else:
				carry = 0

			print('adding sum')
			# add our sum to the new list
			new_linked_list.val = temp_total
			new_linked_list.next = ListNode(0)
			new_linked_list = new_linked_list.next

		# if not none -> go next until the last one!
		list1_pointer = list1_pointer.next
		list2_pointer = list2_pointer.next

	# skip the 0 and print the array
	start3 = start3.next
	while start3 != None:
		print('new list val:', start3.val)
		start3 = start3.next


cur1 = l1 = ListNode(2)
l1 = l1.next
l1 = ListNode(4)
l1 = l1.next
l1 = ListNode(3)
l1 = l1.next

cur2 = l2 = ListNode(5)
l2 = l2.next
l2 = ListNode(6)
l2 = l2.next
l2 = ListNode(4)
l2 = l2.next

while cur2 != None:
	print(cur2.val)
	cur2 = cur2.next

print(add_two_numbers_linked_list(cur1,cur2))