"""
	Rotate array to the left by k times

	ie.

	[1,2,3,4,5], k = 3 ---> [4,5,1,2,3]


	rotate to the right by k times

	ie. 

	[1,2,3,4,5], k = 3 ---> [3,4,5,1,2]

"""


def rotate_array_left(array, rotation_count):

	print('original array:', array)

	while rotation_count > 0:
		# save the first element as it will be overwritten!
		temp_first_pos = array[0]

		for i in range(1,len(array)):
			array[i-1] = array[i]

		rotation_count -= 1
		array[len(array)-1] = temp_first_pos

		print(array)

	return 'final arrray: ' + str(array)


def rotate_array_right(array, rotation_count):

	print('original array:', array)

	while rotation_count > 0:
		# save the last element as it will be overwritten!
		temp_last_pos = array[-1]

		# work backwards!
		index = len(array) - 1
		while index > 0:
			array[index] = array[index-1]
			index -= 1

		rotation_count -= 1
		array[0] = temp_last_pos

		print(array)

	return 'final arrray: ' + str(array)


def rotate_array_right_optimized_ish(array, rotation_count):


	def reverse(sub_array, start, end):
		# keep swapping till the middle
		while start < end:
			temp = sub_array[start]
			sub_array[start] = sub_array[end]
			sub_array[end] = temp

			start += 1
			end -= 1


	# for leet code test cases...
	rotation_count = rotation_count % len(nums)

	# 1. start the initial reverse
	reverse(array, 0, len(array)-1)
	print(array)

	# 2. then reverse the 0 to k sub array
	reverse(array, 0, rotation_count-1)
	print(array)

	# 3. then reverse the k to n sub array
	reverse(array, rotation_count, len(array)-1)
	print(array)
	




if __name__ == '__main__':


	# array = [1,2,3,4,5]
	# rotation_count = 3

	# print(rotate_array_left(array, rotation_count))

	# array = [1,2,3,4,5]
	# rotation_count = 3

	# print(rotate_array_right(array, rotation_count))

	array = [1,2,3,4,5,6,7,8]
	rotation_count = 3

	print(array)
	print(rotate_array_right_optimized_ish(array, rotation_count))