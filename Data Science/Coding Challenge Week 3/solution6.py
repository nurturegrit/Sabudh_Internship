def spiral_arr_for(matrix):
    n = len(matrix[0])  # Number of columns
    m = len(matrix)  # Number of rows
    arr = []  # Solution array
    
    col_limit = n  # Current column limit
    row_limit = m  # Current row limit
    r = 0  # Starting row index
    c = 0  # Starting column index
    
    while r < row_limit and c < col_limit:
        # Traverse the top row from left to right
        for col in range(c, col_limit):
            arr.append(matrix[r][col])
        r += 1  # Move down to the next row
        
        # Traverse the rightmost column from top to bottom
        for row in range(r, row_limit):
            arr.append(matrix[row][col_limit - 1])
        col_limit -= 1  # Move the column limit leftward
        
        # Traverse the bottom row from right to left
        if r < row_limit:
            for col in range(col_limit - 1, c - 1, -1):
                arr.append(matrix[row_limit - 1][col])
            row_limit -= 1  # Move the row limit upward
        
        # Traverse the leftmost column from bottom to top
        if c < col_limit:
            for row in range(row_limit - 1, r - 1, -1):
                arr.append(matrix[row][c])
            c += 1  # Move the column limit rightward
    
    return arr


print(spiral_arr_for([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
print(spiral_arr_for([[1,2,3],[4,5,6],[7,8,9]]))