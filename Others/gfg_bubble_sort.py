# gfg_bubble_sort.py
def bubbleSort(arr):
    n = len(arr) 
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 


# have a swap flag
def bubbleSort2(arr):
    n = len(arr) 
    for i in range(n):
        swapped = False 
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] 
                swapped = True
        if swapped == False:
            break 

# test 
arr = [64, 34, 25, 12, 22, 11, 90] 
arr2 = [64, 34, 25, 12, 22, 11, 90] 

bubbleSort(arr) 
print('sorted array is: ', arr)

bubbleSort2(arr2)
print('second method: ', arr2)
# https://www.geeksforgeeks.org/bubble-sort/