# contains duplicates
class Solution:
    def containsNearbyDuplicate(self, nums: 'List[int]', k: 'int') -> 'bool':
        lookup = {}
        for i, num in enumerate(nums):
            if num not in lookup:
                lookup[num] = i 
            else:
                if i - lookup[num] <= k:
                    return True
                lookup[num] = i 
        return False 

nums = [1, 0, 1, 1]
k = 1
sol = Solution()
print(nums)
print(k)
print(sol.containsNearbyDuplicate(nums, k))
