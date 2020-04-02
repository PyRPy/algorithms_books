# sort_colors.py
class Solution:
    def sortColors(self, nums):
        """
        don't return anything, modify nums in-place
        """

        p, q = 0, 0 
        k = len(nums) - 1 

        while q <= k:
            if p < q and nums[q] == 0:
                nums[p], nums[q] = nums[q], nums[p]
                p += 1
            elif nums[q] == 2:
                nums[q], nums[k] = nums[k], nums[q]
                k -= 1 
            else:
                q += 1 

nums = [2,0,2,1,1,0]
print(nums)
sol = Solution()
sol.sortColors(nums)
print(nums)