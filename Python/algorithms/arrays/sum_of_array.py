"""
	Find the sum of an array
	ie. given an array [1,2,3,4,5], sum = 15
"""

def sum_array(array):
	sum = 0
	for i in array:
		sum += i

	return sum

def sum_to_num(num):
	sum = 0
	for i in range(num+1):
		sum += i

	return sum

def sum_of_even_nums_array(array):
	sum = 0
	for i in array:
		if i % 2 == 0:
			# it's an even number!
			sum += i

	return sum

def sum_of_even_nums_num(num):
	sum = 0
	for i in range(num+1):
		if i % 2 == 0:
			sum += i

	return sum



# some dummy arrays
array1 = [1,2,3,4,5]
array2 = [2,3,1,6,7]
array3 = [1,5,2,9,10]

# print test cases
print(sum_array(array1))
print(sum_to_num(4))
print(sum_of_even_nums_array(array3))
print(sum_of_even_nums_num(5))



