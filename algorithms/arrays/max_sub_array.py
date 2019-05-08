"""
	Find the largest continguous sub-array with a sum of target, given an array.

	ex.

	Input: [-2,1,-3,4,-1,2,1,-5,4],
	Output: 6
	Explanation: [4,-1,2,1] has the largest sum = 6.

"""


def max_sub_array_iterative(nums):

	global_max = nums[0]
	local_max = nums[0]
	index = 0
	while index < len(nums):

		# set up inner loop to have a running local max counter
		inner_index = index
		local_max = 0

		while inner_index < len(nums):
			local_max += nums[inner_index]
			inner_index += 1

			# if the local max is less than the global max -> update
			if local_max > global_max:
				global_max = local_max

		index += 1
	return global_max



def max_sub_array(nums):
	"""
	:type nums: List[int]
	:rtype: int
	"""
	global_max = [0] * len(nums)
	current_max = nums[0]
	global_max[0] = current_max

	for i in range(1, len(nums)):

		# compare with local max
		if current_max > 0:
			current_max = nums[i] + current_max
		else:
			current_max = nums[i]

		# compare with global max
		global_max[i] = max(global_max[i], current_max)

	# print(global_max)

	return max(global_max)

"""
	compare max = -2 with 0 -> False
	max = 1
	next loop
	compare max = 1 with 0 -> True
	max = -3 + 1 = -2
	next loop
	compare max = -2  with 0 -> False
	max = 4
	next loop
	comapre max = 4 with 0 -> True
	max = -1 + 4 = 3
	next loop
	compare max = 3 with 0 -> True
	max = 2 + 3 = 5
	next loop
	comapre max = 5 with 0 -> True
	max = 1 + 5 = 6
	next loop
	compare max = 6 with 0 -> True
	max = 6 + -5 = 1
"""

array = [-2,1,-3,4,-1,2,1,-5,4]

# print(max_sub_array(array))
print(max_sub_array_iterative(array))
