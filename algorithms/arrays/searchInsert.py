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

	index = 0
	half = int(len(nums)/2)
	print(half)
	print(len(nums))

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

array = [1,3,5,6]
target = 5
#print(searchInsert(array, target)) 

print(searchInsert_v2(array, target)) 