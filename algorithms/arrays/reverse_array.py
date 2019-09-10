"""
	Reversal!
"""




# the best way to do it in python: use the built in slicing operator
def reverse_array(arr):
	return arr[::-1]


# the naive way
def reverse_array_naive(arr):

	new_arr = [0]*len(arr)

	ptr = len(arr) - 1

	for i in range(len(arr)):
		new_arr[i] = arr[ptr]
		ptr -= 1

	return new_arr

ar = [1,2,3,4,5]
print(reverse_array_naive(ar))