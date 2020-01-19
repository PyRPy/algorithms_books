# two sum - different approaches - brutal force
class Solution:
    def two_sum(self, nums, target):
        """
        :type nums : list[int]
        :type target: int
        :rtype: list[int]
        """
        for i in nums:
            j = target - i
            start_index = nums.index(i)
            next_index = start_index + 1
            temp_nums = nums[next_index: ]
            if j in temp_nums:
                return(nums.index(i), next_index + temp_nums.index(j))


    def two_sum2(self, nums, target):
        dict = {}
        for i in range(len(nums)):
            if target - nums[i] not in dict:
                dict[nums[i]] = i
            else:
                return [dict[target - nums[i]], i]
import time
nums = [2, 7, 11, 15]
target = 9
sol = Solution()
start = time.time()
print('brutal force: ', sol.two_sum(nums, target))
end = time.time()
print('time used: ', end - start)

start = time.time()
print('second method: ', sol.two_sum2(nums, target))
end = time.time()
print('time used: ', end - start)

# ref: https://www.youtube.com/watch?v=OTtbG8lNNW8&list=PL2rWx9cCzU84eBz9Xfp9Rah5Fexq5yrh8
