# gfg_is_a_heap.py
# check if an array is a max heap or not 

def isHeap(arr, i, n):
    if i > int((n-2) /2):
        return True 
    if arr[i] > arr[2*i+1] and arr[i] >= arr[2*i+2] \
        and isHeap(arr, 2*i + 2, n)\
        and isHeap(arr, 2*i + 2, n):
        return True 
    return False 


def isHeap2(arr, n):
    
    for i in range(int((n-2)/2) + 1):
        # if left child is greater
        if arr[2*i + 1] > arr[i]:
            return False 
        # if the right child is greater
        if 2 * i + 2 < n and arr[2*i + 2] > arr[i]:
            return False 
    return True 

# test 
arr = [90, 15, 10, 7, 12, 2, 7, 3] 
n = len(arr) -1 
print(arr, ' ', 'is a Heap or not ?')
if isHeap(arr, 0, n):
    print('yes') 
else:
    print('no')

print('the second method :')
if isHeap2(arr, n):
    print('yes') 
else:
    print('no')
# https://www.geeksforgeeks.org/how-to-check-if-a-given-array-represents-a-binary-heap/?ref=rp