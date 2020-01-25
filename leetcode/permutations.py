# permutations
class Solution:
    def permuate(self, nums):
        """
        type nums: list[int]
        rtype: list[list[int]]
        """

        if len(nums) <= 1:
            return [nums]

        answer =[]
        for i, num in enumerate(nums):
            n = nums[:i] + nums[i+1: ]
            for y in self.permuate(n):
                answer.append([num] + y)
        return answer

nums = [2, 4, 8]
sol =  Solution()
print(nums)
print(sol.permuate(nums))