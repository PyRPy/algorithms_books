# intersection_two_arrays2.py
import collections
class Solution:
    def intersection(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1)

        lookup = collections.defaultdict(int) # need to specify input type
        for i in nums1:
            lookup[i] += 1

        result = []
        for i in nums2:
            if lookup[i] > 0:
                result += i,
                lookup[i] -= 1
        return result 

nums1 = [1,2,2,1]
nums2 = [2,2]

sol = Solution()
print(nums1, " ", nums2)
print(sol.intersection(nums1, nums2))
