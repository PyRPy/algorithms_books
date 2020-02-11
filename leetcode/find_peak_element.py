# find peak element in a list
class Solution(object):
    def findPeakElement(self, nums):
        """
        type nums: list[int]
        rtype: int
        """

        size = len(nums)
        for x in range(1, size - 1):
            if nums[x] > nums[x - 1] and nums[x] > nums[x + 1]:
                return x 

        return[0, size - 1][nums[0] < nums[size - 1]]

nums = [1, 2, 3, 1]
sol = Solution()
print(nums)
print(sol.findPeakElement(nums))

