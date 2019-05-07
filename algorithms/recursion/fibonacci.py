"""
	Do the Fib! ex. 1, 1, 2, 3, 5, 8, 13, ... 
	index---------->1, 2, 3, 4, 5, 6,  7,  ....


	ex. 	fib(4) = fib(4-1) + fib(4-2) = fib(3) + fib(2)
				fib(3) = fib(3-1) + fib(3-2) = fib(2) + fib(1)
					fib(2) = 1
						fib(1) = 1
				fib(3) = 1 + 1 = 2
			fib(4) = 2 + 1 = 3
	 		return! :)
"""	


def fib(num):

	if num >= 3:
		return fib(num-1) + fib(num-2)
	else:
		return 1


print(fib(4))


