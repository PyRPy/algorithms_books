# maximum subarray
class Solution:
	def maxSubArray(self, nums):
		"""
		type nums: list[int]
		rtype: int
		"""

		if max(nums) < 0:
			return max(nums)

		local_max, global_max = 0, 0
		for num in nums:
			local_max = max(0, local_max + num)
			global_max = max(global_max, local_max)

		return global_max

sol = Solution()
nums = [1, 3, -1 -4, 5, -2, 9]
print(nums)
print(sol.maxSubArray(nums))
