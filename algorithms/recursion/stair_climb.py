"""
	climb n stairs with 1 or 2 steps
	
	ex.
			  __
		   __|__|
		__|__|__| =
	 __|__|__|__|
	|__|__|__|__|
		   __
		__|__|
	 __|__|__| == n - 1 + n == 5
    |__|__|__|
	   __
	__|__|
   |__|__| == n - 1 + n = 2 -1 + 2 = 3 --> n = 2

   	 __
	|__| == 1 --> n = 1

	 __ == 1  --> n = 0

"""
# solve with recursion
def stair_climb(n):
	"""
	stype: int, n-stairs
	rtype: int, different ways of climbing n stairs
	"""

	if n == 0:
		return 1

	if n == 1:
		return 1:
	elif n < 2: 
		helper_function(n + (n-1))


def helper_funtion


