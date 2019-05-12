"""
	return if strings are the same

	Case 1: strings are the same
	"ABC"
	"ABC"

	Case 2: strings are off by 1
	"ABC"
	"AB" OR "AC"

	Case 3: strings are off by N


"""




def compare_strings(str1, str2, my_tolerance):

	# see if strings are empty.
	if len(str1) == 0 or len(str2) == 0:
		return False

	# arrange such that str1 is always greater than str2  !
	if len(str1) < len(str2):
		temp = str1
		str1 = str2
		str2 = temp


	index_str1 = 0
	index_str2 = 0
	unmatches = 0
	tolerance = my_tolerance

	while index_str2 < len(str2):
		# comapre each letter
		if str1[index_str1] == str2[index_str2]:
			index_str1 += 1
			index_str2 += 1
			print("hello! im the same!")
		else:
			# check if str1[index +1] is the same 
			index_str2 += 1
			if str1[index_str1] == str2[index_str2]:
				index_str1 += 1
			else:
				# they are more than off by 1
				return False
			unmatches += 1

		if unmatches >= tolerance:
			return False

	return True


def compare_strings_v2(str1, str2, my_tolerance):

	# see if strings are empty.
	if len(str1) == 0 or len(str2) == 0:
		return False

	higher = str1
	lower = str2

	# arrange such that str1 is always greater than str2
	if len(str1) < len(str2):
		temp = higher
		higher = lower
		lower = temp

	index_higher = 0
	index_lower = 0
	unmatches = 0
	tolerance = my_tolerance
	match = True

	print(higher, lower)

	while index_lower < len(lower):

		# comapre each letter
		if lower[index_lower] == higher[index_higher]:
			print("hello! im the same!")
			index_higher += 1
			index_lower += 1

		else:


			# check if next letter in str1 is the same
			tol_count = 1
			while tol_count <= tolerance and tol_count <= len(higher) - len(lower):
				print('tol_count', tol_count)
				if len(lower) != len(higher):
					print('lowerindexval:', lower[index_lower], 'higherval', higher[index_higher])
					if lower[index_lower] == higher[index_higher + tol_count]:
						# there was a match in the search
						unmatches -= 1
						break
					else:
						unmatches += 1
					
				else:
					unmatches += 1
					# print('unmatches:', unmatches)

				print('unmatches:', unmatches)
				tol_count += 1

			# end of comparison, increment and go next!
			index_higher += 1
			index_lower += 1
			unmatches += 1

		# if we have too many unmatches return false.
		if unmatches > tolerance:
			return False


	# case: the shorter array ended very early, the longer array still has comparisons, BUT
	# the shorter array matched.

	if len(higher) - len(lower) <= tolerance:
		if unmatches <= tolerance:
			return True
		else:
			return False
	else:
		return False


str1 = 'AB'
str2 = 'AC'
tolerance = 1


print(compare_strings_v2(str1, str2, tolerance))
		