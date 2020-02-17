# rotate array like a cycle
class Solution(object):
    def rotate(self, nums, k):
        """
        type nums: list[int]
        type k: int
        rtype: void, don't return anything, modify nums in-place instead
        """

        k = k % len(nums)

        nums[:k], nums[k:] = nums[len(nums) - k: ], nums[: len(nums) - k]

sol = Solution()
nums = [1, 2, 3, 4, 5, 6, 7]
k = 3
print(nums)
print(k)
sol.rotate(nums, k)
print(nums)