def find_two_uniques(arr):
    """Find 2 Unique Elements in a array that has at least 2 elements that only appear once
    """
    if len(arr) <= 2:
        return arr
    # Exoring all elements
    # will have same result as exoring 2 unique elements
    exor_all = 0
    for num in arr:
        exor_all ^= num
    
    # in exor_all , only the bits that are different in both unique elements are seen as 1
    
    
