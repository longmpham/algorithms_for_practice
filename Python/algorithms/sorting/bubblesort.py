"""
    learn bubble sort on simple array
"""



def bubbleSort(arr):

    # return if empty
    if not arr:
        return False

    n = len(arr)
    # traverse through the array (O(n)) time.
    for i in range(n):

        # traverse each number in the array n times until it sets in its proper position
        for j in range(0, n-i-1):
            # compare if left is less than right, if not swap!
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

    # return arr
    return ', '.join(str(num) for num in arr)


array = [5,4,3,2,1]
print(array)

print(bubbleSort(array))