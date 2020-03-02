# move_zeros.py
class Solution:
    def moveZeroes(self, nums):
        """
        don't return anything, modify nums in-place instead
        """

        pos = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[pos] = nums[i]
                pos += 1
            # print(nums[i])
            # print(pos)
        for i in range(pos, len(nums)):
            nums[i] = 0 

nums = [0,1,0,3,12]
print(nums)
sol = Solution()
sol.moveZeroes(nums)
print(nums)

# questions, how ?