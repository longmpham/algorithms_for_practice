"""
    convert a string to integer
    "123" => 123
    "900" => 900
"""

def naive_reverse(array):

    # create a last iterator
    last = len(array)-1

    for i in range(len(array)):
        if(i == last):
            break
        # swap and increment the last iterator
        array[i], array[last] = array[last], array[i]
        last -= 1
    return array


def my_atoi(str):

    if not str:
        return False

    # another case is if the string is not a number....
    
    # metric converter!
    n = 1

    # first I reverse the string
    # python does this very nicely or i can use a built in.

    # rev_str = reversed(str)
    rev_str = str[::-1]
    print('reversed string:', rev_str)

    # ones, tens, 100s, ... n x 10 every iteration for n characters(numbers) in the string
    final_int = 0
    
    # begin the cycle to convert our string by addings the ones, tens, hundreds... etc.
    for num in rev_str:
        final_int += int(num) * n
        n = n*10

    return final_int




my_string = '123'
array = [5,4,3,2,1]
print(naive_reverse(array))
print(my_atoi(my_string))