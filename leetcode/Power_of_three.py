# Power_of_three.py
class Solution:
    def isPowerOfThree(self, n):
        if n == 1:
            return True 
        elif n <= 2:
            return False 

        while n > 3:
            if n % 3 == 0:
                n /= 3 
            else:
                return False 

        if n == 3:
            return True 
        else:
            return False 

n = 27 
sol = Solution()
print(n)
print(sol.isPowerOfThree(n))
