def get_next_permutation(arr):
    if len(arr) <= 1:
        return arr
    
    i = len(arr) - 2
    while arr[i] >= arr[i + 1] and i >= 0:
        i -= 1
    
    if i == -1:
        # Array is in descending order
        return arr[::-1]
    
    # find first element larger than arr[i] from right
    j = len(arr) - 1
    while arr[j] <= arr[i]:
        j -= 1

    # Swap arr[i] with arr[j]
    arr[i], arr[j] = arr[j], arr[i]

    # Change direction of elements after i
    arr[i + 1: ] = reversed(arr[i + 1:])

    return arr

print(get_next_permutation([1,2,3]))
print(get_next_permutation([3,2,1]))
print(get_next_permutation([1,1,5]))


