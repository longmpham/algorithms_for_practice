

# O(n2)
def max_sub_product_array(arr):

    # O(n^2) time complexity.
    max = 0
    for i in range(len(arr)):
        product = arr[i]
        for j in range(i+1, len(arr)):
            product =+ product * arr[j]
            if product > max:
                max = product
    return max

array = [2,3,4,6]
print(max_sub_product_array(array))