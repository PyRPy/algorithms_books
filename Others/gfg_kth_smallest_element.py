# gfg_kth_smallest_element.py
# to find the k'th smallest element 
def kthSmallest(arr, n, k):
    arr.sort() 
    return arr[k-1]

arr = [12, 3, 5, 7, 19]
n = len(arr) 
k = 3
print("array is: ", arr)
print("k'th smallest element is ", kthSmallest(arr, n, k))

# method 2 quick selection 
import sys 
def kthSmallestQuick(arr, l, r, k):
    if k > 0 and k <= k-l + 1:
        pos = partition(arr, l, r) 
        if pos - 1 == k - 1:
            return arr[pos] 
        if pos - 1 > k - 1:
            return kthSmallestQuick(arr, l, pos - 1, k) 
        return kthSmallestQuick(arr, pos + 1, r, k - pos + l - 1) 
    return sys.maxsize 

def partition(arr, l, r):
    x = arr[r] 
    i = l 
    for j in range(l, r):
        if arr[j] <= x:
            arr[i], arr[j] = arr[j], arr[i] 
            i += 1 
    arr[i], arr[r] = arr[r], arr[i] 
    return i 

print("k'th smallest elelent is: ", kthSmallestQuick(arr, 0, n-1, k-1)) # k changed to k-1

# https://www.geeksforgeeks.org/kth-smallestlargest-element-unsorted-array/