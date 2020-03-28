# spriral_matrix.py
class Solution:
    def spiralOrder(self, matrix):
        row = len(matrix)
        if row == 0 or len(matrix[0]) == 0:
            return []
        col = len(matrix[0]) 

        res = matrix[0]

        if row > 1:
            for i in range(1, row):
                res.append(matrix[i][col-1])

            for j in range(col-2, -1, -1):
                res.append(matrix[row-1][j])

            if col > 1:
                for i in range(row-2, 0, -1):
                    res.append(matrix[i][0])

        M = []
        for k in range(1, row-1):
            t = matrix[k][1:-1]
            M.append(t)

        return res + self.spiralOrder(M)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

sol = Solution()
print(matrix)
print(sol.spiralOrder(matrix))
