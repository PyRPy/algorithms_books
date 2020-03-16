# find_all_numbers_disappeared.py
class Solution:
    def findDisapparedNumbers(self, nums):
        len_array = len(nums) + 1 
        a = set([i for i in range(1, len_array)])
        b = set(nums)
        return list(a - b)

nums = [4, 3, 2, 7, 8, 2, 3, 1]
# [1, n]

sol = Solution()
print(nums)
print(sol.findDisapparedNumbers(nums))
