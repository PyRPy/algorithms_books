# max_average_subarray.py
class Solution:
    def findMaxAverage(self, nums, k):
        tmp = 0 
        result = float('-inf') 
        
        for i, x in enumerate(nums):
            print(i, x) # take a look at process 

            tmp += x 
            if i >= k:
                tmp -= nums[i-k] 
            if i >= k - 1:
                result = max(result, tmp) 
        result = result / k 
        return result 

nums = [1, 12, -5, -6, 50, 3]
k = 4 
sol = Solution() 
print(nums) 
print(sol.findMaxAverage(nums, k)) 
