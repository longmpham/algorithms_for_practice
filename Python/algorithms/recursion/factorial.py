"""
	Do the factorial! N! = N * (N-1) * (N-2) * .... * 1??
	
	case: 	if N = 1 -> N! = 1 * (1 - 1) = 0 -> bad. we leave 0 out and stop at 1.
			if N = 2 -> N! = 2 * (2 - 1) = 2
			if N = 3 -> N! = 3 * (3 - 1) * (2 - 1) = 6 
			if N = 4 -> N! = 4 * (4 - 1) * (3-1) * (2 - 1) = 24
"""


def factorial(num):

	if num <= 1: 
		return 1
	else:
		return num * factorial(num-1)


print(factorial(5))

