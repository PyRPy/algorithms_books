# 13_search.py
# page 460
def simpleSearch(x, nums):
    try:
        return nums.index(x) 
    except:
        return -1 

x = 9
nums = [1, 3, 5, 7, 11]
print("this is from simple search: ", simpleSearch(x, nums))


def linearSearch(x, nums):
    for i in range(len(nums)):
        if nums[i] == x:
            return i 
    return -1 

print("this is from linear search: ", linearSearch(x, nums))

def binarySearch(x, nums):
    low = 0 
    high = len(nums) - 1 
    while low <= high:
        mid = (low + high) // 2 
        item = nums[mid] 
        if x == item:
            return mid 
        elif x < item:
            high = mid - 1 
        else:
            low = mid + 1

    return -1

print('this is from binary search: ', binarySearch(x, nums))
