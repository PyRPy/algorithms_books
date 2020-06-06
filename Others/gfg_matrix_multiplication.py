# gfg_matrix_multiplication.py
def matrix_mult(M, N):
    R = [[0, 0, 0, 0], 
		[0, 0, 0, 0], 
		[0, 0, 0, 0], 
		[0, 0, 0, 0]] 

    for i in range(0, 4):
        for j in range(0, 4):
            for k in range(0, 4):
                R[i][j] += M[i][k] * N[k][j]  # element x element 

    for i in range(0, 4):
        for j in range(0, 4):
            print(R[i][j], end = " ") 
        print("\n", end = "")

# test 
M = [[1, 1, 1, 1], 
	[2, 2, 2, 2], 
	[3, 3, 3, 3], 
	[4, 4, 4, 4]] 

N = [[1, 1, 1, 1], 
	[2, 2, 2, 2], 
	[3, 3, 3, 3], 
	[4, 4, 4, 4]] 

matrix_mult(M, N)

# https://www.geeksforgeeks.org/c-program-multiply-two-matrices/