# find the single number in the array
import operator
from functools import reduce 

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


    def singleNumber2(self, A):
        return reduce(operator.xor, A) 

nums = [3, 2, 4, 2, 4, 0]
nums2 = [1, 1, 3, 0, 2, 4, 2, 4]
sol = Solution()
print(nums)
print(sol.singleNumber(nums))
print("second method: ", sol.singleNumber2(nums))
print("second method: ", sol.singleNumber2(nums2))