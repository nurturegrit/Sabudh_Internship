def trapped_water(elevation_map):
    if not elevation_map:
        return 0

    trapped = 0
    left, right = 0, len(elevation_map) - 1
    left_max, right_max = 0, 0

    while left <= right:
        if elevation_map[left] < elevation_map[right]:
            if elevation_map[left] > left_max:
                left_max = elevation_map[left]
            else:
                trapped += left_max - elevation_map[left]
            left += 1
        else:
            if elevation_map[right] > right_max:
                right_max = elevation_map[right]
            else:
                trapped += right_max - elevation_map[right]
            right -= 1

    return trapped

# Example usage:
elevation_map = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trapped_water(elevation_map))  # Output: should account for all trapped water correctly

print(trapped_water([4,2,0,3,2,5]))