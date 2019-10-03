from collections import defaultdict

class Graph:

	def __init__ (self):
		self.graph = defaultdict(list)

	# connect node A to node B (basically a 2d array!)
	def addEdge(self, u, v):
		self.graph[u].append(v)

	'''	
		the logic is as follows for BFS:
		1. in each graph, whereever you start, you can assume its connected to other nodes
		2. identify nodes as unmarked (or newly found or whatever)
		3. use your first node to begin finding neighbors and enqueue them.
		4. pop the first node in the queue and use that to find neighbors and add them to the queue.
		5. repeat
	'''
	def BFS(self, startNode):

		# identify all nodes to be unmarked/unread
		visitedNodes = [False] * (len(self.graph))
		print(visitedNodes)

		queue = []

		# queue the node
		queue.append(startNode)
		
		# mark the node as visited.
		visitedNodes[startNode] = True

		# start the enqueuing 
		while queue:
			# pop the first element in the queue
			cur_node = queue.pop(0)

			# do things to node that you found
			print('popping off node: ', cur_node)

			# find neighbors
			for i in self.graph[cur_node]:
				# print(queue)

				# if node was unvisited, we queue and mark it as visited.
				if visitedNodes[i] == False:
					print('found node: ', i)
					queue.append(i)
					visitedNodes[i] = True

				else:
					print('node ', i, ' has been visited')


	'''
		the logic for DFS is as follows:
		1. mark all nodes as unvisted (false)
		2. call helper function to begin searching at a node (use call stack)
		3. mark searched node as true
		4. search that node for it's <first> neighbors and search that node (call function/stack)
		5. repeat.

	'''
	def DFS(self, startNode):

		# create an array of unvisited nodes in the graph
		visitedNodes = [False] * (len(self.graph))

		# go down deep as far as you can!
		self._DFS(startNode, visitedNodes)

	def _DFS(self, node, visitedNodes):

		# mark the node as true.
		visitedNodes[node] = True

		# do action with node
		print('popping off:', node)

		# find next node
		for i in self.graph[node]:
			if (visitedNodes[i] == False):
				print('found node: ', i)
				# if its unvisited, go deeper
				self._DFS(i, visitedNodes)
			else:
				print('node ', i, 'has been visited')


	def printGraph(self):
		print(self.graph)




g = Graph() 
g.addEdge(0, 1) 
g.addEdge(0, 2) 
g.addEdge(1, 2)
g.addEdge(1, 5) 
g.addEdge(2, 0) 
g.addEdge(2, 3) 
g.addEdge(3, 3)
g.addEdge(1, 4)
g.addEdge(4, 4)
g.addEdge(5, 5)
# g.addEdge(4, 5)
# g.addEdge(5, 3)
# g.addEdge(0, 5)

g.printGraph()
start = 2
print ('start the graph at: ', start)
g.BFS(start)

print('\n\n ______________________')
g.DFS(start)

# good visual of BFS
# https://www.tutorialspoint.com/data_structures_algorithms/breadth_first_traversal.htm


# good visual of DFS
# https://www.tutorialspoint.com/data_structures_algorithms/depth_first_traversal.htm