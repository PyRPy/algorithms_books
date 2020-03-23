# search_in_rotated_sorted_array.py
class Solution:
    def search(self, nums, target):
        left, right = 0, len(nums) -1 
        while left <= right:
            mid = (left + right) // 2 
            if nums[mid] == target:
                return mid 

            if target >= nums[0]:
                if nums[mid] >= nums[0] and target > nums[mid]:
                    left = mid + 1 
                else:
                    right = mid - 1 
            else:
                if nums[mid] >= nums[0] or target > nums[mid]:
                    left = mid + 1
                else:
                    right = mid - 1

        return -1

nums = [4,5,6,7,0,1,2]
target = 0
sol = Solution()
print(nums, " ", target)
print(sol.search(nums, target))
