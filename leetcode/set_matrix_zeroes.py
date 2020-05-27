# set_zeros_matrix.py
class Solution:
    def setZeroes(self, matrix):
        """
        do not return anything, modify matrix in-place instead 
        """ 
        m, n = len(matrix), len(matrix[0]) 
        zero_row, zero_col = False, False 

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    matrix[i][0] = matrix[0][j] = 0 
                    zero_row = True if i == 0 else zero_row 
                    zero_col = True if j == 0 else zero_col 
        
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(1, m):
                    matrix[i][j] = 0 

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(1,n):
                    matrix[i][j] = 0 
        
        if zero_row:
            for j in range(n):
                matrix[0][j] = 0 

        if zero_col:
            for i in range(m):
                matrix[i][0] = 0 

        return 

mat = [
    [1,1,1],
    [1,0,1],
    [1,1,1]
]

print('before set zeroes: ', mat)
sol = Solution() 
sol.setZeroes(mat)
print('after change: ', mat)
