# intercection_two_arrays.py
class Solution:
    def intersection(self, nums1, nums2):
        if len(nums1) > len(nums2):
            return self.intersection(nums2, nums1) 
        
        lookup = set()
        for i in nums1:
            lookup.add(i) 

        result = []
        for i in nums2:
            if i in lookup:
                result += i, # subtle difference here
                lookup.discard(i) 

        return result 

nums1 = [1, 2, 2, 1]
nums2 = [2, 2]
sol = Solution()
print(nums1, " ", nums2)
print(sol.intersection(nums1, nums2))
