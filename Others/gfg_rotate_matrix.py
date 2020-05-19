# gfg_rotate_matrix.py
def rotateMatrix(mat):
    """
    top: starting row index
    bottom: ending row index 
    right: ending column index
    """
    if not len(mat):
        return 

    top = 0 
    bottom = len(mat) -1 

    left = 0 
    right = len(mat[0]) - 1 

    while left < right and top < bottom:
        # to replace the first element of currnt row
        prev = mat[top+1][left] 
        # top row to right by one step
        for i in range(left, right+1):
            curr = mat[top][i] 
            mat[top][i] = prev 
            prev = curr 

        top += 1 
        # move column one step down - rightmost 
        for i in range(top, bottom+1):
            curr = mat[i][right] 
            mat[i][right] = prev 
            prev = curr 

        right -= 1 

        # move element of bottom row one step left 
        for i in range(right, left-1, -1):
            curr = mat[bottom][i] 
            mat[bottom][i] = prev 
            prev = curr 

        bottom -= 1 

        # move element of leftmost column one step up 
        for i in range(bottom, top-1, -1):
            curr = mat[i][left] 
            mat[i][left] = prev 
            prev = curr 
        left += 1 

    return mat 

# helper function 
def printMatrix(mat):
    for row in mat:
        print(row) 

# test 
mat = [
    [1, 2, 3, 4], 
	[5, 6, 7, 8], 
	[9, 10, 11, 12], 
	[13, 14, 15, 16] 
]

mat = rotateMatrix(mat) 

printMatrix(mat) 

def printColumn(matrix, i):
    return [row[i] for row in matrix] 

import numpy as np 
A = np.array(mat) 
print('the column to print: \n', A[:, 1])
# https://www.geeksforgeeks.org/rotate-matrix-elements/
# https://stackoverflow.com/questions/903853/how-do-you-extract-a-column-from-a-multi-dimensional-array