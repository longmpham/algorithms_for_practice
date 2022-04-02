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
	 __|__|__| == n-1 + n-2 == 3
    |__|__|__|
	   __
	__|__|
   |__|__| == n-1 + n-2 = 2 --> n = 2

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
		return 1
	elif n >= 2: 
		return (stair_climb(n-1) + stair_climb(n-2))


def stair_climb_memo(n, memo):
	"""
	stype: int, n-stairs
	rtype: int, different ways of climbing n stairs
	
	"""

	if n in memo:
		return memo[n]

	if n == 0:
		return 1

	if n == 1:
		return 1
	elif n >= 2: 
		memo[n] = (stair_climb(n-1) + stair_climb(n-2))
		return memo[n]




def stair_climb_bottom_up(n,memo):

	# initialize base conditions as first elements in memo
	memo[0] = 1
	memo[1] = 1

	for i in range(2,n+1):
		memo[i] = memo[i-1] + memo[i-2]

	return memo[n]


n = 5
memo = {}
print(stair_climb_bottom_up(n, memo))


