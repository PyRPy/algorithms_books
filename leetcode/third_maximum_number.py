# third_maximum_number.py
class Solution:
    def thirdMax(self, nums):
        nums = sorted(list(set(nums)))

        if len(nums) < 3:
            return max(nums)
        else:
            return nums[-3]

nums = [2, 2, 3, 1]
sol = Solution()
print(nums)
print(sol.thirdMax(nums))
