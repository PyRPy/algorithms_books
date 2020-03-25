# rotate_matrix_clockwise.py
def rotate90Clockwise(A):
    N = len(A[0])
    for i in range(N // 2):
        for j in range(i, N - i -1):
            temp = A[i][j]
            A[i][j] = A[N-1-i][N-1-j]
            A[N-1-i][N-1-j] = A[j][N-1-i]
            A[j][N-1-i] = temp

# print matrix 
def printMatrix(A):
    N = len(A[0])
    for i in range(N):
        print(A[i])

# driver code 
A = [[1, 2, 3, 4], 
     [5, 6, 7, 8],  
     [9, 10, 11, 12],  
     [13, 14, 15, 16]] 

print("A prior to rotation: ")
printMatrix(A)
rotate90Clockwise(A)

print("A after rotation: ")
printMatrix(A)