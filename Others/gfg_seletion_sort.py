# gfg_seletion_sort.py
import sys 
A = [64, 25, 12, 22, 11]
for i in range(len(A)):
    minIdx = i 
    for j in range(i+1, len(A)):
        if A[minIdx] > A[j]:
            minIdx = j 

    A[i], A[minIdx] = A[minIdx], A[i] 

# test 
print('sorted array: ', A)
# https://www.geeksforgeeks.org/selection-sort/
