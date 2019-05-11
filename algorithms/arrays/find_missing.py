"""
	Given 2 arrays, find the first missing number: in either array.
	Assume unique numbers in each array
	Assume arr1 > arr2
"""


def find_missing_brute_force(arr1, arr2):

	# my first thought is what if either array has no elements?
	if (len(arr1) == 0 or len(arr2) == 0):
		return '1 array has no elements'

	# force arr1 to be always greater.
	if len(arr1) < len(arr2):
		temp = arr1
		arr1 = arr2
		arr2 = temp

	# case 2: if arr1 = [1,2,3,4]
	# 			 arr2 = [1,2,3,5]


	# now we start doing the comparisons

	# we can do the naive brute force method which is to compare each element in one array
	# to all elements in the other array. if it matches, then we're good. if it doesnt,
	# that would be the missing element!

	# ex. given [1,2,3,4] and 	
	#			[1,2,3]		
	# we get by brute force pairs like so:
	# 11, 12, 13,  	--> count = 1
	# 21, 22, 23	--> count = 2
	# 31, 32, 33	--> count = 3
	# 41, 42, 43	--> count = 3
	#
	# if count is not len of arr1 -> then we know that there are unequal matches. 



	# brute force method.
	# we can see 2 for loops -> O(n^2)
	# space complexity -> O(1)

	last1 = 0
	last2 = 0
	match_found = True
	for num1 in arr1:
		for num2 in arr2:
			if num1 is not num2:
				# if they are not equal, we keep searching arr2.
				last1 =  num1
				last2 = num2
				match_found = False
			else:
				# they are equal... we break searching arr2
				match_found = True
				break
		if not match_found:
			# if the lengths are the same, we have 2 return values.
			if len(arr1) == len(arr2):
				return last1, last2
			else:
				return last1

	return 'They are the same!'


def find_missing_optimal(arr1, arr2):

	seen = {}
	
	for i in arr1:
		if i not in seen:
			seen[i] = 1

		# this else statement should never work if all elements are unique.
		# so essentially we're just counting each unique number once.
		else:
			seen[i] += 1

	# check each element in arr2 such that if it has been seen, then we continue checking.
	# otherwise, if its not seen (in our map), then we return that element.
	for i in arr2:
		if i in seen:
			continue
		else:
			# returns the first value not seen!
			return i

	if len(arr1) <= len(arr2):
		return 'both are the same'
	else: 
		return arr1[len(arr2)]




arr1 = [2,3,4,1,5,6,8]
arr2 = [1,2,6,3,4,5,8,9]

# print(find_missing_brute_force(arr1,arr2))

print(find_missing_optimal(arr1,arr2))



