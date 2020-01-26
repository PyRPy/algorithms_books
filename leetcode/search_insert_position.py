# search insert position
class Solution:
    def searchInsert(self, nums, target):
        
        """
        type nums: list[int]
        type target: int
        rtype: int
        """
    
        if target > nums[len(nums) - 1]:
            return len(nums)

        for i in range(len(nums)):
            if nums[i] >= target:
                return i

sol = Solution()
nums = [1, 3, 5, 7, 10]
target = 6
print(nums, target)
print(sol.searchInsert(nums, target))
