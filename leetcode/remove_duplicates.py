# remove duplicates in a sorted list
class Solution:
    def removeDuplicates(self, nums):
        """
        type nums : List[int]
        rtype : int
        """
        if not nums:
            return 0

        count = 0
        for i in range(len(nums)):
            if nums[count] != nums[i]:
                count += 1
                nums[count] = nums[i]
        return count + 1

# example
nums = [1, 0, 3, 1, 5, 3]
sol = Solution()
print("nums before removal: ", nums)
print(sol.removeDuplicates(nums))

nums2 = [0, 1, 1, 3, 3, 5]
print("nums2 before removal: ", nums2)
print(sol.removeDuplicates(nums2))
