
def shuffle(arr):
    """
    we will only consider the elements around the middle point in case of odd len of array
    """
    # n ranges from 1 to n as in statement
    # Starting point of an
    an = 0
    if len(arr)%2:
        # Starting point of bn for odd lengths
        bn = len(arr)//2 + 1
        mid_element = arr[bn - 1]
    else:
        # Starting point of bn
        # for even lengths
        bn = len(arr)//2
    next_an = None
    while bn < len(arr) and an < len(arr) - 1:
        if next_an is None:
            next_an = arr[an + 1]
        else:
            temp = arr[an + 1]
            arr[an + 1] = next_an
            next_an = temp
            an += 1
            bn += 1
            if bn == len(arr):
                # Only occurs in case of odd elements
                arr[bn - 1] = mid_element
                break
        arr[an + 1] = arr[bn]
        an += 1
    return arr

arr = [1, 2, 9, 15]
print(shuffle(arr))

arr = [1, 2, 3, 4, 5, 6]
print(shuffle(arr))