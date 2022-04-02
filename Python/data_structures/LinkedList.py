"""
	Create a Linked List
	-add a node
	-delete a node
	-sort a node
	-print node
"""

class Node:

	def __init__(self, value, next=None):
		self.value = value
		self.next = None


class LinkedList:

	def __init__(self):
		self.head = None

	def addNode(self, value):
		
		# create the new node		
		New_Node = Node(value)	

		# print(value)
		# base case: first value
		if self.head is None:
			self.head = New_Node
			return
		
		# we have to traverse the linkedlist and find the last element
		current_pointer = self.head
		while current_pointer.next is not None:
			current_pointer = current_pointer.next

		# once its at the end when it reaches none, we add the element!
		current_pointer.next = New_Node

	def pop(self):

		# create a temp variable to hold the position of head
		current_pointer = self.head
		previous_pointer = None

		# base case, no linked list exists.
		if current_pointer.next is None:
			if current_pointer.value is not None:
				print('List is empty because pop')
				self.head = None
				current_pointer.value = None
				return
			print('List is empty')
			return
		

		# find last element
		while current_pointer.next is not None:
			previous_pointer = current_pointer
			current_pointer = current_pointer.next
			popped = current_pointer.value

		# we found the last element...
		current_pointer = previous_pointer
		current_pointer.next = None

		return popped

	def deleteNode(self, key):

		# [ 1 ] -> [ 2 ] -x-> [ X3X ] -x-> [ 4 ] -> None
		#				 ---------->

		current_pointer = self.head
		previous_pointer = None

		# base condition if no list.
		if current_pointer.next is None:
			if current_pointer.value == key:
				current_pointer.value = None
				self.head = None
				print('deleted')

			print('No list found')
			return

		while current_pointer.next is not None:
			print('looking at:', current_pointer.value)
			if current_pointer.value == key:
				# we found the value.
				if previous_pointer is None:
					# this means that its the head (0th position in the list)
					print('key is first index. deleting...')
					self.head = current_pointer.next
					return
				else:
					# it was found mid list / end
					previous_pointer.next = current_pointer.next
					print('found key:', key, 'deleting...')
					return

			else:
				previous_pointer = current_pointer
				current_pointer = current_pointer.next

				# if last element...
				if current_pointer.next is None:
					if current_pointer.value == key:
						previous_pointer.next = current_pointer.next
						print('found key:', key, 'deleting...')
						return


		print('no key:', str(key), 'found')
		return 

	def printList(self):

		current_pointer = self.head
		string = 'List is empty'


		# if empty...
		if self.head is None:
			print(string)
			return
		elif current_pointer.value == None:
			print(string)
			return
		else:
			string = ''

		# else we print the list
		while current_pointer is not None:
			string += str(current_pointer.value) + ', '
			current_pointer = current_pointer.next

		print(string)

	def get(self, key):

		current_pointer = self.head

		while current_pointer.next is not None:
			if current_pointer.value == key:
				print('Found:', key)
				return True
			else:
				current_pointer = current_pointer.next
				if current_pointer.next == None:
					if current_pointer.value == key:
						print('Found:', key)
						return True

		print('Could not find:', key)
		return False

	def size(self):

		current_pointer = self.head
		size = 0

		# check base case (0th index)
		if current_pointer.next is None:
			if current_pointer.value is None:
				size = 0
				return size

		size = 1
		# otherwise, numbers do exist.
		while current_pointer.next is not None:
			size += 1
			current_pointer = current_pointer.next

		print('size:', size)
		return size



def main():

	# create a linked list!
	My_Linked_List = LinkedList()
	
	# add some elements
	My_Linked_List.addNode(1)
	My_Linked_List.addNode(2)
	My_Linked_List.addNode(3)
	My_Linked_List.addNode(4)
	My_Linked_List.printList()

	My_Linked_List.get(4)
	My_Linked_List.get(6)

	My_Linked_List.size()

	# #Try Deleting!
	# print('\ndeleting now')
	# My_Linked_List.deleteNode(1)
	# My_Linked_List.printList()
	# My_Linked_List.deleteNode(6)
	# My_Linked_List.printList()
	# My_Linked_List.deleteNode(3)
	# My_Linked_List.printList()
	# My_Linked_List.deleteNode(4)
	# My_Linked_List.printList()
	# My_Linked_List.deleteNode(2)
	# My_Linked_List.printList()
	# print('\nim done')

	# My_Linked_List.printList()
	# My_Linked_List.addNode(1)
	# My_Linked_List.addNode(2)
	# My_Linked_List.addNode(3)
	# My_Linked_List.addNode(4)
	# My_Linked_List.printList()

	# # pop it now.

	# My_Linked_List.pop()
	# My_Linked_List.printList()

	# My_Linked_List.pop()
	# My_Linked_List.printList()

	# My_Linked_List.pop()
	# My_Linked_List.printList()

	# My_Linked_List.pop()
	# My_Linked_List.printList()



if __name__ == '__main__':
	main()