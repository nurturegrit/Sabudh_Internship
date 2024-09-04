def find_maximum_product_triplets(arr, get_other_results=False):
    max_3 = [0, 0, 0]
    neg_2 = [0, 0]
    product = 1
    # Iterating through the array, get the values of max_3 positive values, min_2 negative values
    for j in range(len(arr)):
        num = arr[j]
        if num < 0:
            for i in range(1, -1, -1):
                if num < neg_2[i]:
                    while i >= 0:
                        temp = neg_2[i]
                        neg_2[i] = num
                        num = temp
                        i -= 1
        else:
            for i in range(2, -1, -1):
                if num > max_3[i]:
                    while i >= 0:
                        temp  = max_3[i]
                        max_3[i] = num
                        num = temp
                        i -= 1
    neg_2_product = neg_2[1] * neg_2[0]
    if neg_2_product:
        if neg_2_product > max_3[0] * max_3[1]:
            max_product_triplets = neg_2 + max_3[-1:]
            for num in max_product_triplets: product *= num
    else:
        for num in max_3: product *= num
        max_product_triplets = max_3
    if get_other_results:
        return max_3, neg_2, product, max_product_triplets
    else:
        return max_product_triplets
    
print(find_maximum_product_triplets([-4, 1, -8, 9, 6]))
print(find_maximum_product_triplets([1, 7, 2, -2, 5]))