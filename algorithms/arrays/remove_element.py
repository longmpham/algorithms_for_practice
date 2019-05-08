"""
	remove all elements found from an array. ie. [1,2,3,3,4,5] ==> [1,2,4,5] by removing 3
"""


def remove_element(nums, value):
    
    index = 0

    for element in nums:
        if element == value:
            del nums[index]
        index+=1

    print(nums)





    # print new list!
    # new_list = []
    # i = 0
    # while i < index:
    #     new_list.append(nums[i])
    #     i += 1
    # print(new_list)

                


array = [1,3,2,3,4,5,3,7]
print(remove_element(array, 3))