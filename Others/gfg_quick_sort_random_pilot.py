# gfg_quick_sort_random_pivot.py
# lomuto's partition scheme 

import random 
def quicksort(arr, start, end):
    if start < end:
        pivotindex = partition_rand(arr, start, end) 
        quicksort(arr, start, pivotindex - 1) 
        quicksort(arr, pivotindex + 1, end) 

def partition_rand(arr, start, end):
    randpivot = random.randrange(start, end) 
    arr[start], arr[randpivot] = arr[randpivot], arr[start] 
    return partition(arr, start, end) 

def partition(arr, start, end):
    pivot = start 
    i = start + 1 
    for j in range(start + 1, end + 1):
        if arr[j] <= arr[pivot]:
            arr[i], arr[j] = arr[j], arr[i] 
            i = i + 1 
    arr[pivot], arr[i-1] = arr[i-1], arr[pivot] 
    pivot = i - 1 
    return pivot 

# test 
if __name__ == "__main__":
    array = [10, 7, 8, 9, 1, 5] 
    print(array)
    quicksort(array, 0, len(array) -1) 
    print('after quick sort: ')
    print(array) 
# https://www.geeksforgeeks.org/quicksort-using-random-pivoting/