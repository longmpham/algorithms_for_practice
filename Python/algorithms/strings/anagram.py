"""
	Anagrams!
"""


from collections import Counter

# short way
def isAnagram_v1(str1, str2):
	return Counter(str1) == Counter(str2)

# long thoughtful way.
def isAnagram_v2(str1, str2):


	seen = {}
	for i in str1:
		if i not in seen:
			seen[i] = 1
		else:
			seen[i] += 1

	for i in str2:
		if i not in seen:
			return False
		else:
			seen[i] -= 1

	print(seen)

	# if keys are equal to zero!
	check = all(value == 0 for value in seen.values())

	return check


string1 = 'fefefe21'
string2 = '21fefefe'

print(isAnagram_v2(string1,string2))