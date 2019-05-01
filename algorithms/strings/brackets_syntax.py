"""
	Given a string of brackets and only brackets, find whether if the string is correct syntax
	ie. string = [][]{}()       return True
	string = {([])}             return True
	string = ]])()				return False
	string = ]					return False
"""


def correct_bracket_syntax(string):

	# if string is length of 1 or 0, return false! Yay. ez.
	if len(string) <= 1:
		return False
	elif len(string) % 2 != 0:
		return False

	# compare each letter in string and add it to a stack! FIFO data structure!

	stack = []
	open_brackets = '[{('
	# closed_brackets = ']})' # not used!

	for bracket in string:

		if bracket in open_brackets:
			if bracket == '[':
				compliment_bracket = ']'
			elif bracket == '{':
				compliment_bracket = '}'
			else:
				compliment_bracket = ')'
			stack.append(compliment_bracket)
		
		# closed bracket!
		else: 
			# if there is nothing in the stack and we're checking a closed bracket, we know that the string is bad
			if len(stack) < 1: 
				return False
			# check the last item in the stack and see if it matches what we're looking at in the string array.
			# if they are the same, pop out the last item! We start fresh.
			# the deeper the stack, the more deeper we are in the brackets.
			# ie. shallow -> '()[]' deep -> '{[()]}'
			if stack[-1] == bracket:
				stack.pop()
	
	if len(stack) == 0:
		return True
	else:
		return False


string = '[]', '{[]}', '{}[]', '{{', '{', ')', '[', '{[]}{[]}'

for s in string:

	print(correct_bracket_syntax(s))

""" answer should be:
true, 
true, 
true, 
false, 
false,
false, 
false, 
true
"""