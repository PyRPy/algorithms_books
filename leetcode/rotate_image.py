# rotate_image.py
class Solution:
    def rotate(self, matrix):
        """
        don't return anything, modify matrix in-place instead
        """
        h = len(matrix)
        n = h - 1

        for i in range(h//2):
            for j in range(i, n - i):
                tmp = matrix[i][j] 
                matrix[i][j] = matrix[n-j][i]
                matrix[n-j][i] = matrix[n-i][n-j]
                matrix[n-i][n-j] = matrix[j][n-i]
                matrix[j][n-i] = tmp 

matrix = [[1,2,3],
        [4,5,6],
        [7,8,9]]

print(matrix)
sol = Solution()
print(sol.rotate(matrix))
print(matrix)