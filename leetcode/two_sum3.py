# two_sum.py
class Solution:
    def twoSum(self, nums, target):
        mapping = {} 

        for index , val in enumerate(nums):
            diff = target - val 
            print(index, val, diff)
            if diff in mapping:
                return [mapping[diff], index] # swtich positions
            else:
                mapping[val] = index 

nums = [2,7,11,15]
target = 17
sol = Solution()
print(sol.twoSum(nums, target))
# ref https://github.com/Garvit244/Leetcode