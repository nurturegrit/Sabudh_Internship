# Custom Test Case for visualizing the indexes after rotation
n = 5
matrix = [[f'{j}{i}' for i in range(n)] for j in range(n)]

import numpy as np

def rotate_right(matrix):
    """
    Approach : Shifting elements starting from Corner for each sub_matrix/layer in matrix
    """
    for sub_matrix in range(len(matrix)//2):
        for i in range(sub_matrix, len(matrix) - 1 - sub_matrix):
            # Each subsequent lower layer, the row_index, col index starts from the sub_matrix
            j, r = sub_matrix, i
            sav = matrix[j][r]
            for _ in range(4):
                temp = matrix[j][r]
                matrix[j][r] = sav
                sav = temp
                j, r = r, (len(matrix) - 1 - j)
            matrix[sub_matrix][i] = sav
    return matrix

print(np.array(matrix))
print()
print(np.array(rotate_right(matrix)))

# Checking Solution for Test Case using numpy
print(np.array(rotate_right([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])) == np.array([[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]))

# Another Solution
def rotate_90(matrix):
    for sub_layer in range(len(matrix)//2):
        for i in range(sub_layer, len(matrix) - 1 - sub_layer):
            j, r = sub_layer, i
            sav = matrix[j][r]
            for _ in range(4):
                j, r = r, len(matrix) - 1 - j
                temp = matrix[j][r]
                matrix[j][r] = sav
                sav = temp
    return matrix

print(np.array(rotate_90([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]])) == np.array([[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]))