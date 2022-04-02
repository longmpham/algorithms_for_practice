"""
	Given an array, find a pair that sums to a given value
	ie. array = [1,2,3,4,5]    sum = 3    ans = [1,2]
"""

def sum_of_pairs(array, sum):

	seen = {}
	i = 0

	while i < len(array):

		# calculate the compliment of your index value
		compliment = sum - array[i]

		# if the compliment is not seen, add the index value in the seen numbers list
		if compliment not in seen:
			print('compliment: ', compliment, 'number: ', array[i], 'i: ', i)
			seen[array[i]] = i
			i +=1
		else:
			# return the index of the pairs ([low num, high num])
			return [min(i, seen[compliment]), max(i, seen[compliment])]

	return False

# test cases
array1 = [1,2,3,4,5]
array2 = [2,3,1,6,7]
array3 = [1,5,2,9,10]
array4 = [5,4,3,2,1]

print(sum_of_pairs(array4, 3))