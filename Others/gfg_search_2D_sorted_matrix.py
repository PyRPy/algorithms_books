# gfg_search_2D_sorted_matrix.py
M = 3 
N = 4 
def binarySearch1D(arr, K):
    low = 0 
    high = N -1 
    while low <= high:
        mid = low + int((high - low) / 2)
        if arr[mid] == K:
            return True 

        if arr[mid] < K:
            low = mid + 1 
        else:
            high = mid - 1 
    return False 

def searchMatrix(matrix, K):
    low = 0 
    high = M - 1 
    while low <= high:
        mid = low + int((high-low)/2) 
        if K > matrix[mid][0] and K <= matrix[mid][N-1]:
            return binarySearch1D(matrix[mid], K) 
        if K < matrix[mid][0]:
            high = mid - 1 
        else:
            low = mid + 1 
    return False 

# test 
matrix = [  [1, 3, 5, 7], 
            [10, 11, 16, 20], 
            [23, 30, 34, 50]] 
K = 30 
if searchMatrix(matrix, K):
    print('found')
else:
    print('not found')
# https://www.geeksforgeeks.org/search-in-a-sorted-2d-matrix-stored-in-row-major-order/
