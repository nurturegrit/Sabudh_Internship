def vol_trapped(arr):
    def find_vol(arr, p1, p2):
        width = p2 - p1 - 1
        length = min(arr[p1], arr[p2])
        diff = sum(arr[p1+1: p2])
        return (length * width) - diff
    def find_if_ends_max(arr):
        first = None
        last = None
        max1 = None
        max2 = None
        vol = 0
        for i, num in enumerate(arr):
            if first is None and num:
                first = i
                last = i
                max1 = i
            elif num:
                last = i
                if num > arr[max1]:
                    max2 = max1
                    max1 = i
                elif max2 is None or num > arr[max2]:
                    max2 = i
        if max2 < max1:
            temp = max1
            max1 = max2
            max2 = temp
        if max1 == first and max2 == last:
            vol += find_vol(arr, first, last)
        elif max1 == first:
            vol += find_if_ends_max(arr[first: max2+1])
            vol += find_if_ends_max(arr[max2:last+1])
        elif max2 == last:
            vol += find_if_ends_max(arr[first: max1+1])
            vol += find_if_ends_max(arr[max1:max2+1])
        else:
            vol += find_if_ends_max(arr[first: max1+1])
            vol += find_if_ends_max(arr[max1: max2+1])
            vol += find_if_ends_max(arr[max2: last+1])
        return vol
    return find_if_ends_max(arr)

print(vol_trapped([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1, 0]))