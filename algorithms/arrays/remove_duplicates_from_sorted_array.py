"""
	remove duplicates from sorted array
"""

def remove_duplicates(array):

	# given an array that is sorted,
	# i can keep track of the indexes that have duplicates
	# at the end, i remove the indexes , shift array over (or skip the count)


	count = 0
	new_array = []
	seen = {}

	# add to map to show # of occurences
	while count < len(array):
		if(array[count] in seen):
			seen[array[count]] += 1
		else:
			seen[array[count]] = 1
		count += 1

	# only use map where occurrence == 1
	for number in seen:
		if seen[number] == 1: 
			new_array.append(number)

	printer = 'array: ' + str(new_array) + ' length: ' + str(len(new_array))
	return printer

def remove_duplicates_in_place(array):

	count = 0
	size = len(array)
	new_list = []

	while count < size - 1:
		if(array[count] == array[count+1]):
			found_index = count+1
			while found_index < size-1:
				array[found_index] = array[found_index+1]
				found_index += 1
			size -= 1
			print(size)
		else:
			count += 1


	count = 0
	print('last size', size)
	while count < size:
		new_list.append(array[count])
		count += 1

	print(new_list)

def remove_duplicates_in_place_v2(nums):

    if not nums:
        return 0

    index  = 0
    for element in nums:
        if element > nums[index]:
            index += 1
            nums[index] = element
            print('helpme')
    

    return nums[0:index+1]




array = [1,1,2,5,6,7,7,8,9,9]
array1 = [1]
array2 = []

#print(remove_duplicates(array))
print(remove_duplicates_in_place_v2(array))
