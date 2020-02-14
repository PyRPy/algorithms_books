# two sum 2
class Solution(object):
    def twoSum(self, numbers, target):
        """
        type numbers: List[int]
        type target: int 
        rtype: list[int]
        """
        start = 0 
        end = len(numbers) - 1
        sum = 0 
        
        while start != end:
            sum = numbers[start] + numbers[end]
            if sum > target:
                end -= 1 
            elif sum < target:
                start += 1
            else:
                return [start + 1, end + 1]

numbers = [2, 7, 11, 15]
target = 9
sol = Solution()
print(numbers)
print(target)
print(sol.twoSum(numbers, target))