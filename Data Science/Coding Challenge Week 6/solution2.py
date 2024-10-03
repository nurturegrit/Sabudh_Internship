def search_sorted_matrix(matrix, target):
    #  Starting Col is top right, row is first
    cols = len(matrix[0])
    rows = len(matrix)
    r, c = 0, cols - 1

    # Search ZigZag
    # untill it it out bounds of matrix
    while r < rows and c >= 0:
        
        if matrix[r][c] == target:
            return True
        elif matrix[r][c] > target:
            c -= 1 # go to prev col 
        else:
            r += 1 # go to next row

    return False

matrix = [
    [1, 4, 7, 11, 15],
    [2, 5, 8, 12, 19],
    [3, 6, 9, 16, 22],
    [10, 13, 14, 17, 24],
    [18, 21, 23, 26, 30]
]
target = 20
print(search_sorted_matrix(matrix, target))

matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]
target = 10

print(search_sorted_matrix(matrix, target))