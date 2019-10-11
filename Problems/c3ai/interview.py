def max_sub_product_array(arr):

    # O(n^2) time complexity.
    max = 0
    for i in range(len(arr)):
        product = arr[i]
        for j in range(i+1, len(arr)):
            product =+ product * arr[j]
            if product > max:
                max = product