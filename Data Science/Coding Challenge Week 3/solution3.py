def find_median(arr1, arr2):
    """
    Takes 2 sorted arrays as inputs and find the median of their joint
    """
    # Let's take two pointer for starting element of each arr and join the lists
    a = 0
    b = 0
    joined = []
    while a != len(arr1) - 1 or b != len(arr2) - 1:
        if a == len(arr1):
            joined += arr2[b:]
            break
        elif b == len(arr2):
            joined += arr1[a:]
            break
        if arr1[a] > arr2[b]:
            joined.append(arr2[b])
            b += 1
        elif arr1[a] == arr2[b]:
            joined.append(arr1[a])
            joined.append(arr2[b])
            a += 1
            b += 1
        else:
            joined.append(arr1[a])
            a += 1
    if len(joined)%2:
        return joined[len(joined)//2]
    else:
        return (joined[len(joined)//2 - 1] + joined[len(joined)//2])/2
    
print(find_median([2, 3, 5, 8], [10, 12, 14, 16, 18, 20]))
print(find_median([1,2,3,4,5,6], [6,7,8,9,10]))
print(find_median([-5, 3, 6, 12, 15],[-12, -10, -6, -3, 4, 10]))