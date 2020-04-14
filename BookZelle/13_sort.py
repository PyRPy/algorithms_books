# 13_sort.py
# bubble sort
def selectSort(nums):
    # sort nums into ascending order
    n = len(nums)

    # for each position in the list (except the very last)
    for bottom in range(n-1):
        # find the smallest item in nums[bottom] .. nums[n-1] 

        mp = bottom                         # bottom is smallest initially
        for i in range(bottom + 1, n):      # look at each position
            if nums[i] < nums[mp]:          # this one is smaller
                mp = i                      # remember its index

        # swap smallest item to the bottom
        nums[bottom], nums[mp] = nums[mp], nums[bottom] 

nums = [1, 3, 2, 8, 5, 4]

print(nums)
selectSort(nums)
print(nums)

# merge sort
def merge(lst1, lst2, lst3):
    i1, i2, i3 = 0, 0, 0 
    n1, n2 = len(lst1), len(lst2) 

    while i1 < n1 and i2 < n2:
        if lst1[i1] < lst2[i2]:
            lst3[i3] = lst1[i1] 
            i1 = i1 + 1 

        else:
            lst3[i3] = lst2[i2] 
            i2 = i2 + 1 
        i3 = i3 + 1 

    while i1 < n1:
        lst3[i3] = lst1[i1] 
        i1 = i1 + 1 
        i3 = i3 + 1 
    while i2 < n2:
        lst3[i3] = lst2[i2] 
        i2 = i2 + 1 
        i3 = i3 + 1 

def mergeSort(nums):
    n = len(nums)
    if n > 1:
        m = n // 2 
        nums1, nums2 = nums[:m], nums[m:] 
        mergeSort(nums1)
        mergeSort(nums2)
        merge(nums1, nums2, nums)

nums = nums = [1, 3, 2, 8, 5, 4]
print(nums) 
mergeSort(nums)
print(nums)