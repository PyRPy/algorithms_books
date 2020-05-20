# gfg_dp_LIS.py
# lis returns length of the longest 
# increasing subsequence in arr of size n 

def calc_LIS(arr):
    n = len(arr) 
    # initialize LIs value for all indices
    lis = [1] * n 

    for i in range(1, n):
        for j in range(0, i):
            if arr[i] > arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j] + 1 
        print('i: ', i, 'lis ', lis)
    # initialize max to 0 to get max of all LIS 
    maximum = 0 

    for i in range(n):
        maximum = max(maximum, lis[i]) 
    return maximum 

# test 
arr = [10, 22, 9, 33, 21, 50, 41, 60] 
print('length of the longest increasing subsequences: ',calc_LIS(arr)) 
