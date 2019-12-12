# selection sort - simple but slow O(n2)
# ref : grokking algorithms
# find the smallest number
def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index
# selection sort
def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        newArr.append(arr.pop(smallest))
        print(newArr)
    return newArr
print(selectionSort([5, 3, 6, 2, 10]))
arr = [5, 3, 6, 2, 10]
print(arr.pop(findSmallest(arr)))
