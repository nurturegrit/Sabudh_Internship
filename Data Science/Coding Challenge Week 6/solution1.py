def product_except_i(arr):
    '''
    Creates two arrays Prefix, Suffix storing 
    products of all prefix elements and suffix elements
    for all indices of an array
    Outputs An Array that has products of all elements
    in the array except at index  
    '''
    n = len(arr)

    result = [0]* n

    # Prefix
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= arr[i]

    # Suffix
    suffix = 1

    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= arr[i]
    

    return result


print(product_except_i([1,2,3,4]))

print(product_except_i([-1,1,0,-3,3]))
