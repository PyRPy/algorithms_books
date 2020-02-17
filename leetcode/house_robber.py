# house robber
class Solution:
    def rob(self, nums):
        """
        type nums: list[int]
        rtype: int 
        """

        last, now = 0, 0 
        for num in nums:
            last, now = now, max(last + num, now)

        return now 

nums = [2, 7, 9, 3, 1]
sol = Solution()
print(nums)
print(sol.rob(nums))

