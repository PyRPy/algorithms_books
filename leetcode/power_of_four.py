# power_of_four.py
class Solution:
    def isPowerOfFour(self, num):
        while num >= 4:
            if num % 4 == 0:
                num /= 4
            else:
                return False 

        if num == 1:
            return True 
        else:
            return False

num = 64
sol = Solution()
print(num)
print(sol.isPowerOfFour(num))
