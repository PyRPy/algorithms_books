# how t rotate a matrix by 90 degree clockwise

import numpy as np

m = np.array([[1,2,3],
              [4,5,6],
              [7,8,9]])

def rotate_matrix(mat):
    return np.rot90(mat, -1)

print(rotate_matrix(m)) # this is not right first
