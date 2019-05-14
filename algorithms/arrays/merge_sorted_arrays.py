"""
	merge 2 sorted arrays into a sorted array
"""


def merge_sorted_arrays(nums1, m, nums2, n):
	"""
	arr1 = list1
	m = len of list
	nums2 = list2
	n = len of list
	"""

	if m == 0 and n == 0:
		return None
	if m == 0: 
		nums1 = nums2
		return nums1
	if n == 0: return nums1

	# base condition: if nums1 + nums2 = sorted.
	if nums1[-1] < nums2[0]: 
		nums1 = nums1 + nums2 # <- python does this automagically.
		return nums1
	
	# else, create empty spaces for nums1 to extend the array.
	nums1 = nums1 + [0]*n


	# compare nums1 and nums2 last index
	A = m-1		# nums1 (original)
	B = n-1		# nums2 (original)
	C = m+n-1	# nums1 (full length)

	# print(A,B,C)

	while A >= 0 and B >= 0:

		# print('comparing', nums2[B], 'with', nums1[A])

		if nums2[B] > nums1[A]:
			nums1[C] = nums2[B]
			B -= 1
		else:
			nums1[C] = nums1[A]
			A -= 1

		C -= 1

	if A < 0:
		nums1[:B+1] = nums2[:B+1]

	# print(nums1)

	return nums1





arr1 = [1,2,3]
m = len(arr1)
arr2 = [2,5,6]
n = len(arr2)

print(merge_sorted_arrays(arr1,m,arr2,n))