"""
	find triplets (3 numbers) in a list that sum to a given value.
	ie. list = [1,2,3,4,5,6,7,8,9,10]       sum = 6   ans = [1,2,3]
"""

def triplet_sum(numbers, sum):
	
	# helper variables
	seen = {}
	index = 0
	# count_loop1 = 0
	# count_loop2 = 0

	# traverse through list!
	while index < len(numbers):
		compliment = sum - numbers[index]

		j = 0
		
		# find compliments of the compliments that sum to our target
		while j < compliment:
			# count_loop2 += 1
			if j in seen:
				if compliment - j in seen:
					# print('i found one')
					# return True
					# print('loop1:', count_loop1, 'loop2:', count_loop2)
					return sorted([index, seen[j], seen[compliment-j]]) # take out sorted, just for viewing purpose
				else:
					j += 1
			else:
				j += 1

		# count_loop1 += 1
		seen[numbers[index]] = index
		index += 1

	# print('loop1:', count_loop1, 'loop2:', count_loop2)

	return False



numbers = [
			[1,2,3,4,5,6,7,8,9,10],
			[6,7,8,9,10],
			[1,2,3,4],
			[2,1,3],
			[4,7,2,1,7,0,3,9],
			[4,5,6,7,8,9,1,2,3],
			[3,4,5,6,7,8,9,1,2]
		]

for nums in numbers:
	print(triplet_sum(nums, 6))