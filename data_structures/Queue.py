"""
	Create a Queue data structure
"""


class Queue:

	def __init__(self, q=[]):
		self.q = []

	def isEmpty(self):
		if not self.q: return True
		return False

	def enqueue(self, item):
		self.q.insert(0, item)

	def dequeue(self):
		if self.q:
			return self.q.pop()
		else:
			print('empty queue')
			return

	def peek(self):
		return self.q[-1]

	def dequeueAll(self):
		print('deleting all q')
		while self.q:
			self.q.pop()

	def getQueue(self):
		if self.isEmpty():
			return 'empty queue'
		return self.q

	def size(self):
		return len(self.q)


def main():
	My_Q = Queue()

	if My_Q.isEmpty():
		print('empty!')

	# make some stuff
	My_Q.enqueue(4)
	My_Q.enqueue(5)

	print(My_Q.size())

	print(My_Q.getQueue())

	# now pop all
	print(My_Q.peek())
	My_Q.dequeue()
	My_Q.dequeue()
	My_Q.dequeue()

	My_Q.enqueue(4)
	My_Q.enqueue(5)	
	My_Q.enqueue(4)
	My_Q.enqueue(5)	
	My_Q.enqueue(4)
	My_Q.enqueue(5)

	print(My_Q.getQueue())

	My_Q.dequeueAll()

	print(My_Q.getQueue())



if __name__ == '__main__':
	main()