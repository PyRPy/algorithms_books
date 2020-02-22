# contains duplicates
class Solution:
    def containsDuplicate(self, nums):
        """
        type nums: list[int]
        rtype: bool
        """
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i+1]:
                return True

        return False

nums = [1, 2, 3, 1]
sol = Solution()
print(nums)
print(sol.containsDuplicate(nums))

