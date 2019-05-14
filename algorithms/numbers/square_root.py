"""
	find the square root of a number, n
"""

# THIS SOLUTION IS TOO LONG TO USE! OPTIMIZSE IT WITH V2
def square_root_slow(n):

	if n <= 0:
		return 'need positive integer'

	# first we need to find a starting place
	count = 1.
	last = 0.
	while count < n: 
		# print(count**2)
		if count**2 == n:
			return count

		if count**2 < n:
			last = count
			count += 1
		else:
			break

	print(last)
	# divide n by last
	temp = n / last

	count_approximation = 0
	tries = 10
	while True:

		# take the average
		temp = (temp + last)/2

		if temp**2 is not n:
			count_approximation += 1
		else:
			return temp

		# stop after n tries
		if count_approximation == tries:
			return temp

def square_root(n):

	# first base solution:

	if n <= 0:
		return 0

	lower = 0
	higher = n

	while lower <= higher:
		middle_num = lower + (higher-lower)//2 # get the mid point value


		if middle_num * middle_num <= n:
			if n < (middle_num+1) * (middle_num+1):
				return middle_num
		elif n < middle_num * middle_num:
			higher = middle_num
		else:
			lower = middle_num + 1



n = 8
print(square_root(n))
