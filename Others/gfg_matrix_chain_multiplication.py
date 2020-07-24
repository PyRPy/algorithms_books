# gfg_matrix_chain_multiplication.py
# recursive method 

import sys 
def MatrixChainOrder(p, i, j):
    if i == j:
        return 0 
    _min = sys.maxsize 

    for k in range(i, j):
        count = MatrixChainOrder(p, i, k) + \
                MatrixChainOrder(p, k+1, j) + \
                p[i-1]*p[k]*p[j]

        if count < _min:
            _min = count 

    return _min 


def MatrixChainOrderDp(p, n):
    m = [[0 for x in range(n)] for x in range(n)] 
    for i in range(1, n):
        m[i][i] = 0 
    for L in range(2, n):
        for i in range(1, n-L+1):
            j = i+L-1 
            m[i][j] = sys.maxsize
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i-1]*p[k]*p[j] 
                if q < m[i][j]:
                    m[i][j] = q 
    return m[1][n-1]

arr = [1, 2, 3, 4, 3]
n = len(arr)
print('minimum number of multiplications is - recursive: ', MatrixChainOrder(arr, 1, n-1))
print('minimum number of nultiplications is - dp method: ', str(MatrixChainOrderDp(arr, n)))



