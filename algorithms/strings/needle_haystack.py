"""
	find the needle in the haystack with strings and return the first index of the phrase
"""

def needle_haystack(haystack, needle):

    if haystack == '' and needle == '':
        return 0
    elif needle == '':
        return 0
    elif len(needle) > len(haystack):
        return -1
    

    index = 0
    flag = -1
    while index < len(haystack):

        if haystack[index] == needle[0]:
            needle_index = 0
            haystack_index = index

            while needle_index < len(needle):

                if haystack_index == len(haystack):
                    flag = -1
                    break

                elif haystack[haystack_index] == needle[needle_index]:
                    needle_index += 1
                    haystack_index += 1
                    flag = index
                else:
                    flag = -1
                    break
            if flag >= 0:
                return flag
        index += 1
    
    return flag



hay = 'aab'
needle = 'aaa'

print(needle_haystack(hay, needle))