"""
	find a target in an array. if found, return index
	if not found, return index of where it should be found
"""



def searchInsert(array, target):

	index = 0
	for element in array:
		if element == target:
			return index
		else:
			index += 1

def searchInsert_v2(nums, target):
	# we can optimize by cutting work in half.

	# bonus: we can cut work in half multiple times until the value is found!
	# 		if its not found...

	index = 0
	half = int(len(nums)/2)

	if nums[half] == target: return half

	if nums[half] < target:
		# we know its not the lower half, its the upper half
		while half < len(nums):
			if nums[half] == target:
				return half
			elif target < nums[half]:
				return half
			else:		
				half +=1

		return len(nums)

	else:
		# its the lower half
		while index < half:
			if nums[index] == target:
				return index
			elif target < nums[index]:
				return index
			else:
				index += 1

		return half



def searchInsert_v3_recursive(nums, target):
	
	
	index = 0

	# DOES NOT WORK CURRENTLY. Only returns if found.
	half = int(len(nums)/2)
	# print('length of array:', len(nums), 'half:', half)
	print('array:', nums, 'half:', half, 'target:', target)

	# print(nums[half] == target)

	if nums[half] == target:
		print('found target')
		return half
	elif target < nums[half]:
		# print('lower')
		index = searchInsert_v3_recursive(nums[0:half], target)
	elif target > nums[half]:
		# print('higher')
		index = searchInsert_v3_recursive(nums[half:len(nums)], target)




array = [1,3,5,6,7]
target = 7
#print(searchInsert(array, target)) 

# print(searchInsert_v2(array, target)) 

print(searchInsert_v3_recursive(array, target)) 
