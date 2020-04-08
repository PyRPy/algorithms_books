# find_minimum_in_rotated_sorted_array.py
class Solution:
    def findMin(self, nums):
        if nums == []:
            return 

        left = 0 
        right = len(nums) - 1 
        result = nums[0] 

        while left <= right:
            mid = (left + right) // 2 
            if nums[mid] >= nums[left]:
                result = min(result, nums[left])
                left = mid + 1
            else:
                result = min(result, nums[mid])
                right = mid - 1 

        return result 

nums = [3,4,5,1,2]
sol = Solution() 
print(nums)
print(sol.findMin(nums))
