# majority element
class Solution(object):
    def majorityElement(self, nums):
        """
        type nums: list[int] 
        rtype: int
        """
        index , cnt = 0, 1
        for i in range(1, len(nums)):
            if nums[index] == nums[i]:
                cnt += 1
            else:
                cnt -= 1 
                if cnt == 0:
                    index = i 
                    cnt = 1
        return nums[index]

sol = Solution()
nums = [1, 3, 1, 1, 1, 3]
print(nums)
print(sol.majorityElement(nums))
