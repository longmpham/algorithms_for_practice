"""
	Given an array, find all pairs that sums to a given value
	ie. array = [1,2,3,4,5]    sum = 5    ans = [1,4], [2,3]
"""

def find_all_sum_of_pairs(array, sum):

	i = 0
	seen_list = {}
	ans = []

	while i < len(array):

		# find the compliment
		compliment = sum - array[i]

		if compliment not in seen_list:
			# add element of array in if not seen!
			seen_list[array[i]] = i
		else:
			# we did see a pair match! Yippee!
			ans.append((min(i, seen_list[compliment]), max(i, seen_list[compliment])))
		i += 1

	# sort our return list by the first index in ascending order! Need more time to understand lambdas.
	ans = sorted(ans, key=lambda x: x[0])
	return ans


# test cases
arrays = [
			[1,2,3,4,5,6,7,8],
			[3,5,2,6,7,9,2,1]
		]
for array in arrays:
	print(find_all_sum_of_pairs(array,5))