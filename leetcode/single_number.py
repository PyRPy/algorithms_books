# find the single number in the array
class Solution(object):
    def singleNumber(self, nums):
        """
        type nums: list[int]
        rtype: int 
        """
        ans = 0
        for num in nums:
            ans ^= num

        return ans 

nums = [3, 2, 4, 2, 4, 0]
sol = Solution()
print(nums)
print(sol.singleNumber(nums))
