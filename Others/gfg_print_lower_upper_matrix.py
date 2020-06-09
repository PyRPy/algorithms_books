# gfg_print_lower_upper_matrix.py
def lower(matrix, row, col): 
    for i in range(0, row):
        for j in range(0, col):
            if i < j:
                print("0", end = " ")  
            else:
                print(matrix[i][j]) 
        print(" ")

def upper(matrix, row, col): 
    for i in range(0, row):
        for j in range(0, col): 
            if i > j:
                print("0", end = " ")
            else:
                print(matrix[i][j], end = " ")
        print(" ")

# test 
matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]
row = len(matrix)
col = len(matrix[0])
# print(row)

print("lower triangular matrix: ")
lower(matrix, row, col)

print("upper triangular matrix: ")
upper(matrix, row, col)

# code: https://www.geeksforgeeks.org/program-print-lower-triangular-upper-triangular-matrix-array/
                