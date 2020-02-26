# container_most_water.py
class Solution:
    def maxArea(self, height):
        left = 0 
        right = len(height) - 1
        result = 0 

        while left < right:
            water = min(height[left], height[right]) * (right - left)

            if water > result:
                result = water 
            if height[left] < height[right]:
                left += 1 

            else: 
                right -= 1 

        return result 

height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
sol = Solution()
print(height)
print(sol.maxArea(height))
