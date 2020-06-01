# gfg_find_max_average_subarray.py
# return the beginning index of max average subarray of length 'k'
def findMaxAverage(arr, n, k):
    # check k is valid or not 
    if k > n: 
        return -1 
    
    # get the sum of first k elements in subarray 
    sum = arr[0] 

    for i in range(1, k):
        sum += arr[i] 

    max_sum = sum 
    max_end = k - 1 

    # get the sum of remaining subarrays 
    for i in range(k, n):
        sum = sum + arr[i] - arr[i-k] 
        if sum > max_sum:
            max_sum = sum 
            max_end = i 
    return max_end - k + 1 

# test 
arr = [1, 12, -5, -6, 50, 3]
k = 4 
n = len(arr) 

print('the max average subarray of length', k, 'beginning at index', \
    findMaxAverage(arr, n, k)) 

# ref : https://www.geeksforgeeks.org/find-maximum-average-subarray-of-k-length/