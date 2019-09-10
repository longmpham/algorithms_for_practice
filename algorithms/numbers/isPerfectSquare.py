# is number a perfect square








def isPerfectSquare(num):

	# base condition if 0 or negetive
	if (num <= 0): return False


	for i in range(1, num):
		test = i*i
		print(test)
		if test == num:
			return True
		if test > num: 
			return False

	return False





num = 32
print(isPerfectSquare(num))